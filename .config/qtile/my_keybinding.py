import os

from libqtile.config import Key
from libqtile.lazy import lazy


def get_my_keybinding(groups):
    mod = "mod4"
    alterkey = "mod1"
    terminal = "kitty"
    # terminal = "xfce4-terminal"

    HOME = os.path.expanduser("~")

    keys = [
        Key([], "Print", lazy.spawn("flameshot gui"), desc="Launch screenshot"),
        Key(
            ["control"],
            "Escape",
            lazy.spawn("playerctl play-pause"),
            desc="Media play/pause",
        ),
        Key([alterkey], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([alterkey], "delete", lazy.window.kill(), desc="Kill focused window"),
        Key(
            [alterkey],
            "backslash",
            lazy.spawncmd(),
            desc="Spawn a command using a prompt widget",
        ),
        Key(
            [alterkey],
            "f",
            lazy.window.toggle_fullscreen(),
            desc="Toggle fullscreen on the focused window",
        ),
        Key(
            [alterkey],
            "tab",
            lazy.layout.next(),
            desc="Move window focus to other window",
        ),
        Key([alterkey], "escape", lazy.next_layout(), desc="Toggle between layouts"),
        # Rofi
        # Key([mod], "r", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
        Key([mod], "r", lazy.spawn("rofi -modi drun -show drun"), desc="spawn rofi"),
        #
        Key([mod], "equal", lazy.layout.grow(), desc="Grow window"),
        Key([mod], "minus", lazy.layout.shrink(), desc="Shrink window"),
        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key(
            [mod, "shift"],
            "h",
            lazy.layout.shuffle_left(),
            desc="Move window to the left",
        ),
        Key(
            [mod, "shift"],
            "l",
            lazy.layout.shuffle_right(),
            desc="Move window to the right",
        ),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        # Toggle between different layouts as defined below
        Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
        Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
        Key([mod, "shift"], "space", lazy.layout.flip()),
        # Utility
        Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
        Key([mod, "control"], "delete", lazy.shutdown(), desc="Shutdown Qtile"),
        # Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
        Key(
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn(f"{HOME}/.config/qtile/scripts/volume.sh volume_up"),
        ),
        # Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
        Key(
            [],
            "XF86AudioLowerVolume",
            lazy.spawn(f"{HOME}/.config/qtile/scripts/volume.sh volume_down"),
        ),
        Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
        Key(
            [],
            "XF86MonBrightnessUp",
            lazy.spawn(f"{HOME}/.config/qtile/scripts/brightness.sh brightness_up"),
            desc="brightness UP",
        ),
        Key(
            [],
            "XF86MonBrightnessDown",
            lazy.spawn(f"{HOME}/.config/qtile/scripts/brightness.sh brightness_down"),
            desc="brightness Down",
        ),
    ]

    for i in groups:
        keys.extend(
            [
                # mod1 + number of group = switch to group
                Key(
                    [alterkey],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                ),
                # mod1 + shift + number of group = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                ),
                # Or, use below if you prefer not to switch to that group.
                # # mod1 + shift + number of group = move focused window to group
                # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                #     desc="move focused window to group {}".format(i.name)),
            ]
        )

    return keys
