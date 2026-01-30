from libqtile import layout
from libqtile.config import Match


def get_my_floating_layout():
    return layout.Floating(
        border_focus="#c3e88d",
        border_width=3,
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
            # custom
            # run to get string : xprop | grep WM_CLASS
            Match(wm_class="yad"),
            Match(wm_class="Eog"),
            Match(wm_class="Xarchiver"),
            Match(wm_class="Meld"),
            Match(wm_class="pavucontrol"),
        ],
    )
