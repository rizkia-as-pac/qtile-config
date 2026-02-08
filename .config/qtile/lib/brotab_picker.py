from __future__ import annotations

import subprocess
import threading
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from urllib.parse import quote_plus

DEFAULT_GROUP = "e"
BROWSER_KEYWORD = "firefox"


@dataclass(frozen=True)
class Tab:
    tab_id: str   # e.g. b.1.7
    title: str
    url: str


def _run(cmd: List[str], stdin: Optional[str] = None, timeout: Optional[int] = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        input=stdin,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=timeout,
    )


def _bt_ok() -> bool:
    p = _run(["bt", "clients"], timeout=2)
    return p.returncode == 0


def _bt_list_tabs() -> List[Tab]:
    p = _run(["bt", "list"], timeout=4)
    if p.returncode != 0:
        return []
    out: List[Tab] = []
    for line in p.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        tab_id = parts[0].strip()
        title = parts[1].strip()
        url = parts[2].strip()
        if tab_id and title:
            out.append(Tab(tab_id, title, url))
    return out


def _rofi_pick(lines: List[str]) -> str:
    # user interaction: allow long timeout
    p = _run(
        ["rofi", "-dmenu", "-i", "-p", "Firefox tab / search"],
        stdin="\n".join(lines) + "\n",
        timeout=None,
    )
    return (p.stdout or "").strip()


def _window_prefix(tab_id: str) -> str:
    # b.1.7 -> b.1
    parts = tab_id.split(".")
    return ".".join(parts[:2]) if len(parts) >= 2 else tab_id


def _qtile_firefox_windows(qtile) -> List[Tuple[str, str]]:
    """
    Return list of (group_name, window_title_full) for firefox windows.
    This reads Qtile internal state directly (no cmd-obj).
    """
    res: List[Tuple[str, str]] = []

    # qtile.windows_map: {wid: Window}
    # window has .wm_class and .name, and belongs to a group
    for w in getattr(qtile, "windows_map", {}).values():
        try:
            wm_class = w.get_wm_class() or []
        except Exception:
            wm_class = getattr(w, "wm_class", []) or []

        wm_s = ",".join(wm_class) if isinstance(wm_class, (list, tuple)) else str(wm_class)
        if BROWSER_KEYWORD not in wm_s.lower():
            continue

        group = getattr(w, "group", None)
        group_name = getattr(group, "name", "") if group else ""

        title_full = (getattr(w, "name", "") or "").replace("\n", " ").strip()
        if group_name and title_full:
            res.append((group_name, title_full))

    return res


def _build_prefix_to_group_map(qtile, tabs: List[Tab]) -> Dict[str, str]:
    """
    Match rule kamu:
    - bt tab.title harus jadi prefix dari Qtile Firefox window title
    - hasil mapping: window_prefix(tab_id) -> group_name
    """
    ff = _qtile_firefox_windows(qtile)

    mapping: Dict[str, str] = {}
    for t in tabs:
        wp = _window_prefix(t.tab_id)
        if wp in mapping:
            continue

        for g, full_title in ff:
            # case-sensitive prefix match (aman buat "\xxx")
            if full_title.startswith(t.title):
                mapping[wp] = g
                break

    return mapping


def go_to_group(name: str):
    """
    Copy dari logic kamu.
    """
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name.isdigit() and name != "0":
            qtile.groups_map[name].toscreen(1)
        else:
            qtile.groups_map[name].toscreen(0)

    return _inner


def _call_in_qtile_thread(qtile, fn) -> None:
    """
    Schedule fn to run on Qtile event loop thread safely.
    Tries multiple attributes depending on Qtile version.
    """
    # Newer Qtile often has _eventloop (asyncio loop)
    loop = getattr(qtile, "_eventloop", None)
    if loop is not None:
        try:
            loop.call_soon_threadsafe(fn)
            return
        except Exception:
            pass

    # Fallback: some builds have call_soon
    call_soon = getattr(qtile, "call_soon", None)
    if callable(call_soon):
        try:
            call_soon(fn)
            return
        except Exception:
            pass

    # Last resort (not ideal): call directly (may be wrong thread)
    try:
        fn()
    except Exception:
        pass


def brotab_rofi(qtile) -> None:
    """
    Non-blocking entry for Key(..., lazy.function(brotab_rofi))
    All heavy work runs in a thread.
    """
    def worker():
        if not _bt_ok():
            return

        tabs = _bt_list_tabs()
        if not tabs:
            return

        menu_lines = [f"{t.tab_id} {t.title} {t.url}" for t in tabs]

        # Build mapping BEFORE rofi so we don't touch Qtile state after user waits.
        # (still safe either way, but this keeps qtile access short)
        prefix_to_group = _build_prefix_to_group_map(qtile, tabs)

        chosen = _rofi_pick(menu_lines)

        # cancel/empty -> default group
        if not chosen:
            _call_in_qtile_thread(qtile, lambda: go_to_group(DEFAULT_GROUP)(qtile))
            return

        # exact match -> activate tab
        if chosen in set(menu_lines):
            tab_id = chosen.split()[0].strip()
            wp = _window_prefix(tab_id)
            target_group = prefix_to_group.get(wp, DEFAULT_GROUP)

            # 1) move to group via qtile object (main thread)
            _call_in_qtile_thread(qtile, lambda: go_to_group(target_group)(qtile))

            # 2) activate tab (external)
            _run(["bt", "activate", tab_id], timeout=3)
            return

        # otherwise: query
        query = chosen.strip()
        if not query:
            _call_in_qtile_thread(qtile, lambda: go_to_group(DEFAULT_GROUP)(qtile))
            return

        _call_in_qtile_thread(qtile, lambda: go_to_group(DEFAULT_GROUP)(qtile))

        url = f"https://www.google.com/search?q={quote_plus(query)}"

        # pick a prefix mapped to DEFAULT_GROUP
        open_prefix = ""
        for wp, g in prefix_to_group.items():
            if g == DEFAULT_GROUP:
                open_prefix = wp
                break

        if not open_prefix:
            # fallback: first bt client prefix
            p = _run(["bt", "clients"], timeout=2)
            first = (p.stdout.splitlines()[:1] or [""])[0].strip()
            cid = (first.split()[:1] or [""])[0]  # e.g b.1.33
            open_prefix = _window_prefix(cid) if cid else ""

        if not open_prefix:
            return

        _run(["bt", "open", open_prefix], stdin=url + "\n", timeout=3)

    threading.Thread(target=worker, daemon=True).start()
