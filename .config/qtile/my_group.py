from libqtile.config import Group, Match
from libqtile import layout


def get_my_groups():
    groups = [
        # Screen affinity here is used to make
        # sure the groups startup on the right screens
        # Main screen
        Group(name="q", screen_affinity=0, label="Q"),
        Group(name="w", screen_affinity=0, label="W",
              matches=[Match(wm_class="code")]),
        Group(name="e", screen_affinity=0, label="E"),
        Group(name="r", screen_affinity=0, label="R"),
        # Secondary screen
        Group(
            name="1",
            screen_affinity=1,
            label="1",
            layouts= [
                 layout.MonadTall(margin=10, border_focus="#c3e88d", border_width=3, align=layout.MonadTall._right),
                 layout.Max( border_focus="#c3e88d", margin=10, border_width=3,),
                 layout.Floating( border_focus="#c3e88d", border_width=3,),
            ]
        ),
        Group(
            name="2",
            screen_affinity=1,
            label="2",
            matches=[Match(wm_class="google-chrome-stable")],
            layouts= [
                 layout.MonadTall(margin=10, border_focus="#c3e88d", border_width=3, align=layout.MonadTall._right),
                 layout.Max( border_focus="#c3e88d", margin=10, border_width=3,),
                 layout.Floating( border_focus="#c3e88d", border_width=3,),
            ]
        ),
        Group(name="3", screen_affinity=1, label="3", ),
        Group(name="4", screen_affinity=1, label="4"),
        Group(name="5", screen_affinity=1, label="5"),
        Group(name="6", screen_affinity=1, label="6"),
        Group(name="0", screen_affinity=0, label="0"),
    ]

    return groups
