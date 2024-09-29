from libqtile.config import Group, Match


def get_my_groups():
    groups = [
        # Screen affinity here is used to make
        # sure the groups startup on the right screens
        # Main screen
        Group(name="q", screen_affinity=0, label=""),
        Group(name="w", screen_affinity=0, label="", matches=[Match(wm_class="code")]),
        Group(name="e", screen_affinity=0, label=""),
        Group(name="r", screen_affinity=0, label=""),
        # Secondary screen
        Group(name="1", screen_affinity=1, label=" ₁"),
        Group(
            name="2",
            screen_affinity=1,
            label=" ₂",
            matches=[Match(wm_class="google-chrome-stable")],
        ),
        Group(name="3", screen_affinity=1, label=""),
        Group(name="4", screen_affinity=1, label=" ₄"),
        Group(name="5", screen_affinity=1, label=" ₅"),
        Group(name="6", screen_affinity=1, label="&"),
    ]

    return groups
