import os
import subprocess
import json

from libqtile import bar, qtile, widget
from libqtile.config import Screen

from constant import SECONDARY_TERMINAL


def get_number_of_monitors():
    try:
        output = subprocess.check_output(["xrandr", "--query"]).decode("utf-8")
        connected_monitors = [
            line for line in output.splitlines() if " connected" in line
        ]
        return len(connected_monitors)
    except subprocess.CalledProcessError:
        return 0


def check_device():
    hostname_command = ["hostnamectl", "--json=pretty"]
    result = subprocess.run(
        hostname_command, capture_output=True, text=True, check=True)

    output = result.stdout
    jsonOutput = json.loads(output)
    # print("Command output:\n", jsonOutput["Chassis"])
    return jsonOutput["Chassis"]


def main_bar(visible_groups, device):

    bar = [
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.Image(
            filename="~/.config/qtile/assets/icon.png",
            margin=6,
            background="#2f343f",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("rofi -show drun")},
        ),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.GroupBox(
            highlight_method="line",
            highlight_color="#2f343f",
            # this_screen_border="#5294e2",
            this_screen_border="#82aaff",
            # this_current_screen_border="#5294e2",
            this_current_screen_border="#82aaff",
            active="#ffffff",
            inactive="#848e96",
            background="#2f343f",
            font="Cantarell",
            fontsize=15,
            padding=4,
            margin_y=4,
            visible_groups=visible_groups,
        ),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.Prompt(
            fontsize=15,
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
            fontsize=14,
        ),
        widget.CurrentLayout(scale=0.60),
        widget.Sep(padding=5, linewidth=0),
        widget.Clock(
            format="%Y-%m-%d %a %I:%M %p",
            # background="#2f343f",
            # foreground="#9bd689",
            padding=8,
            font="Cantarell",
            fontsize=15,
        ),
        widget.CheckUpdates(
            update_interval=1800,
            distro="Arch_yay",
            display_format="{updates} updates",
            foreground="#ffffff",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(SECONDARY_TERMINAL + " -e yay -Syu")
            },
            background="#2f343f",
            font="Cantarell",
            fontsize=15,
            padding=8,
        ),
        widget.Sep(padding=5, linewidth=0),
        widget.Memory(
            format='{MemUsed: .3f} /{MemTotal: .3f}',
            measure_mem='G',
            fontsize=15,
        ),
        widget.Sep(padding=5, linewidth=0),
        widget.TextBox(
            text="dB:",
            # foreground="#e39378",
            font="Cantarell",
            fontsize=15,
            padding=3,
        ),
        widget.Volume(
            fontsize=15,
            padding=3,
            # foreground=colors[4],
            # background="#2f343f",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("pavucontrol")},
            font="Cantarell",
        ),
        widget.Sep(padding=5, linewidth=0),
        widget.Sep(padding=0, linewidth=5,
                   foreground="#2f343f", size_percent=100),
        widget.Battery(
            format="{percent:2.0%} {char}",
            font="Cantarell",
            fontsize=15,
            update_interval=2,
        ),
        widget.Sep(padding=5, linewidth=0),
        widget.Sep(padding=5, linewidth=0),
        widget.Sep(padding=5, linewidth=0),
        widget.Sep(padding=5, linewidth=0),
        widget.Systray(icon_size=17, padding=8),
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
        widget.Sep(padding=5, linewidth=0),
        widget.Sep(padding=5, linewidth=0),
        widget.Sep(padding=3, linewidth=0),
    ]

    if device == "desktop":
        battery_index = next(
            (
                i for i, wgt in enumerate(bar) if isinstance(wgt, widget.Battery)
            ), None
        )
        bar.pop(battery_index)

    return bar


def secondary_bar(visible_groups):

    bar = [
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.GroupBox(
            highlight_method="line",
            highlight_color="#2f343f",
            # this_screen_border="#5294e2",
            this_screen_border="#82aaff",
            # this_current_screen_border="#5294e2",
            this_current_screen_border="#82aaff",
            active="#ffffff",
            inactive="#848e96",
            background="#2f343f",
            font="Cantarell",
            fontsize=15,
            padding=4,
            margin_y=4,
            visible_groups=visible_groups,
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
            fontsize=14,
        ),
        widget.CurrentLayout(scale=0.60),
        widget.Sep(padding=2, linewidth=0),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
        widget.Sep(padding=5, linewidth=0, background="#2f343f"),
    ]

    return bar


def get_my_screens(groups):

    monitor_count = get_number_of_monitors()

    if monitor_count > 1:
        main_visible_groups = [
            groups[0].name,
            groups[1].name,
            groups[2].name,
            groups[3].name,
            groups[10].name,
        ]
    else:
        main_visible_groups = [
            groups[0].name,
            groups[1].name,
            groups[2].name,
            groups[3].name,
            groups[10].name,
            groups[4].name,
            groups[5].name,
            groups[6].name,
            groups[7].name,
            groups[8].name,
            groups[9].name,
        ]

    secondary_visible_groups = [
        groups[4].name,
        groups[5].name,
        groups[6].name,
        groups[7].name,
        groups[8].name,
        groups[9].name,
    ]

    screens = []

    device = check_device()

    for count in range(monitor_count):
        if count == 0:
            screens.append(
                Screen(
                    top=bar.Bar(
                        main_bar(main_visible_groups, device),
                        35,  # height in px
                        background="#2f343f",
                        # background="#404552",  # background color
                    ),
                ),
            )
        else:
            screens.append(
                Screen(
                    top=bar.Bar(
                        secondary_bar(secondary_visible_groups),
                        35,  # height in px
                        background="#2f343f",
                        # background="#404552",  # background color
                    ),
                ),
            )

    return screens
