import os

from libqtile import qtile, widget
from libqtile.config import Screen


def get_my_bar():

    colors = [
        ["#282c34", "#282c34"],  # panel background
        ["#3d3f4b", "#434758"],  # background for current screen tab
        ["#ffffff", "#ffffff"],  # font color for group names
        ["#ff5555", "#ff5555"],  # border line color for current tab
        [
            "#74438f",
            "#74438f",
        ],  # border line color for 'other tabs' and color for 'odd widgets'
        ["#4f76c7", "#4f76c7"],  # color for the 'even widgets'
        ["#e1acff", "#e1acff"],  # window name
        ["#ecbbfb", "#ecbbfb"],  # backbround for inactive screens
    ]

    bar = [
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.Image(
            filename="~/.config/qtile/assets/icon.png",
            margin=6,
            background="#2f343f",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show combi")},
        ),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.GroupBox(
            highlight_method="line",
            highlight_color="#2f343f",
            this_screen_border="#5294e2",
            this_current_screen_border="#5294e2",
            active="#ffffff",
            inactive="#848e96",
            background="#2f343f",
            font="Cantarell",
            fontsize=16,
            padding=4,
            margin_y=4,
        ),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.Prompt(
            fontsize=16,
            font="Cantarell",
            # foreground="#2f343f",
            foreground="#99c0de",
            # background="#404552",
            scroll=True,
            width=400,
            prompt=" Spawn : ",
            scroll_fixed_width=False,
            # scroll_clear=True,
            # scroll_hide=True,
        ),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.WindowName(
            # foreground="#99c0de",
            # background="#2f343f",
            fmt="{}",
            font="Cantarell",
            fontsize=13,
            padding=3,
        ),
        widget.WindowCount(
            fontsize=16,
        ),
        widget.CurrentLayoutIcon(scale=0.70),
        widget.Sep(padding=4, linewidth=0),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Arch_yay",
            display_format="{updates} Updates",
            foreground="#ffffff",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(terminal + " -e yay -Syu")
            },
            background="#2f343f",
            font="Cantarell",
            fontsize=15,
            padding=8,
        ),
        widget.Sep(padding=5, linewidth=0),
        widget.Volume(
            fontsize=16,
            padding=3,
            # foreground=colors[4],
            # background="#2f343f",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("pavucontrol")},
            font="Cantarell",
        ),
        widget.Volume(
            fontsize=16,
            padding=3,
            # foreground=colors[4],
            # background="#2f343f",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("pavucontrol")},
            font="Cantarell",
            emoji=True,
        ),
        widget.Sep(padding=0, linewidth=5, foreground="#2f343f", size_percent=100),
        widget.Clock(
            format="󰥔  %Y-%m-%d %a %I:%M %p",
            # background="#2f343f",
            # foreground="#9bd689",
            padding=8,
            font="Cantarell",
            fontsize=15,
        ),
        widget.Battery(
            format="{percent:2.0%} {char}",
            font="Cantarell",
            fontsize=15,
            update_interval=2,
        ),
        widget.Sep(padding=5, linewidth=0),
        widget.Sep(padding=5, linewidth=0),
        widget.Systray(icon_size=20),
        widget.Sep(padding=5, linewidth=0),
        widget.Sep(padding=5, linewidth=0),
        widget.TextBox(
            text="⏻",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    os.path.expanduser("~/.config/rofi/powermenu.sh")
                )
            },
            # foreground="#e39378",
            font="Cantarell",
            fontsize=20,
            padding=3,
        ),
        widget.Sep(padding=4, linewidth=0),
    ]

    return bar
