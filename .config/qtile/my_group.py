from libqtile.config import Group, Match


def get_my_groups():
    groups = [
        # Screen affinity here is used to make
        # sure the groups startup on the right screens
        # Main screen
        Group(name="q", screen_affinity=0, label="Q"),
        Group(name="w", screen_affinity=0, label="W", matches=[Match(wm_class="code")]),
        Group(name="e", screen_affinity=0, label="E"),
        Group(name="r", screen_affinity=0, label="R"),
        # Secondary screen
        Group(name="1", screen_affinity=1, label="1"),
        Group(
            name="2",
            screen_affinity=1,
            label="2",
            matches=[Match(wm_class="google-chrome-stable")],
        ),
        Group(name="3", screen_affinity=1, label="3"),
        Group(name="4", screen_affinity=1, label="4"),
        Group(name="5", screen_affinity=1, label="5"),
        Group(name="6", screen_affinity=1, label="6"),
    ]

    return groups
