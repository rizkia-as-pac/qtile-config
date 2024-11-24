import os

from libqtile import qtile
from libqtile.config import Key
from libqtile.lazy import lazy

from constant import ALTERKEY, MOD, SECONDARY_TERMINAL, TERMINAL


def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name.isdigit():
            # qtile.focus_screen(1)
            qtile.groups_map[name].toscreen(1)
        else:
            # qtile.focus_screen(0)
            qtile.groups_map[name].toscreen(0)

    return _inner


def get_my_keybinding(groups):
    HOME = os.path.expanduser("~")

    keys = [
        Key([], "Print", lazy.spawn("flameshot gui"), desc="Launch screenshot"),
        Key([ALTERKEY], "Return", lazy.spawn(
            TERMINAL), desc="Launch terminal"),
        # Key(
        #     [ALTERKEY], "Return",
        #     lazy.spawn(f"{HOME}/.config/qtile/urxvtc.sh"),
        # ),
        Key([ALTERKEY], "slash", lazy.spawn(
            SECONDARY_TERMINAL), desc="Launch terminal"),
        Key([ALTERKEY], "delete", lazy.window.kill(), desc="Kill focused window"),
        Key(
            [ALTERKEY],
            "backslash",
            lazy.spawncmd(),
            desc="Spawn a command using a prompt widget",
        ),
        Key(
            [ALTERKEY],
            "f",
            lazy.window.toggle_fullscreen(),
            desc="Toggle fullscreen on the focused window",
        ),
        Key([ALTERKEY], 'space', lazy.next_screen(), desc='Next monitor'),

        Key([ALTERKEY], "escape", lazy.next_layout(),
            desc="Toggle between layouts"),
        # Rofi
        Key([MOD], "r", lazy.spawn("rofi -show drun"), desc="spawn rofi"),
        #
        Key([MOD], "equal", lazy.layout.grow(), desc="Grow window"),
        Key([MOD], "minus", lazy.layout.shrink(), desc="Shrink window"),
        # Cycle through windows
        Key(
            [ALTERKEY],
            "tab",
            lazy.layout.next(),
            desc="Move window focus to other window",
        ),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key(
            [MOD, "shift"],
            "left",
            lazy.layout.shuffle_left(),
            desc="Move window to the left",
        ),
        Key(
            [MOD, "shift"],
            "right",
            lazy.layout.shuffle_right(),
            desc="Move window to the right",
        ),
        Key([MOD, "shift"], "down", lazy.layout.shuffle_down(),
            desc="Move window down"),
        Key([MOD, "shift"], "down", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Toggle between different layouts as defined below
        Key([MOD, "shift"], "space", lazy.layout.flip()),
        # Utility
        Key(
            ["control"],
            "Escape",
            lazy.spawn("playerctl play-pause"),
            desc="Media play/pause",
        ),
        Key([ALTERKEY], "n", lazy.spawn(
            "playerctl position 10-"), desc="back 10 second"),
        Key([ALTERKEY], "m", lazy.spawn(
            "playerctl position 10+"), desc="forward 10 second"),
        Key([MOD, "control"], "r", lazy.restart(), desc="Restart Qtile"),
        Key([MOD, "control"], "delete", lazy.shutdown(), desc="Shutdown Qtile"),
        Key(
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn(f"{HOME}/.config/qtile/scripts/volume.sh volume_up"),
        ),
        Key(
            [],
            "XF86AudioLowerVolume",
            lazy.spawn(f"{HOME}/.config/qtile/scripts/volume.sh volume_down"),
        ),
        Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
        Key(
            [],
            "XF86MonBrightnessUp",
            lazy.spawn(
                f"{HOME}/.config/qtile/scripts/brightness.sh brightness_up"),
            desc="brightness UP",
        ),
        Key(
            [],
            "XF86MonBrightnessDown",
            lazy.spawn(
                f"{HOME}/.config/qtile/scripts/brightness.sh brightness_down"),
            desc="brightness Down",
        ),
    ]

    for group in groups:
        keys.extend(
            [
                # ALTERKEY + group name = switch to group
                Key([ALTERKEY], group.name, lazy.function(
                    go_to_group(group.name))),
                # MOD + shift + number of group = move focused window to group
                Key(
                    [MOD, "shift"],
                    group.name,
                    lazy.window.togroup(group.name),
                    desc="move focused window to group {}".format(group.name),
                ),
            ]
        )

    return keys
