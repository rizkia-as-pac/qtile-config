from typing import Final
import os

MOD: Final[str] = "mod4"
ALTERKEY: Final[str] = "mod1"
HOME = os.path.expanduser("~")
TERMINAL: Final[str] = f"{HOME}/.config/qtile/urxvtc.sh" # https://www.reddit.com/r/archlinux/comments/kf4aes/is_there_a_reason_i_shouldnt_use_urxvt_with/
SECONDARY_TERMINAL: Final[str] = "kitty"


# colors = [
#     ["#282c34", "#282c34"],  # panel background
#     ["#3d3f4b", "#434758"],  # background for current screen tab
#     ["#ffffff", "#ffffff"],  # font color for group names
#     ["#ff5555", "#ff5555"],  # border line color for current tab
#     [
#         "#74438f",
#         "#74438f",
#     ],  # border line color for 'other tabs' and color for 'odd widgets'
#     ["#4f76c7", "#4f76c7"],  # color for the 'even widgets'
#     ["#e1acff", "#e1acff"],  # window name
#     ["#ecbbfb", "#ecbbfb"],  # backbround for inactive screens
# ]
