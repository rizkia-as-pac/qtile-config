from libqtile import layout


def get_my_layout():
    layouts = [
        # layout.MonadTall(margin=8, border_focus="#ffffff", border_normal="#2c5380"),
        # layout.MonadTall(margin=10, border_focus="#5294E2", border_width=3).flip(),
        layout.MonadTall(margin=10, border_focus="#5294E2", border_width=3, align=layout.MonadTall._right),
        layout.Max(
            border_normal="#5294E2",
            margin=10,
            border_width=3,
        ),
        # layout.Columns(border_focus_stack='#d75f5f'),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.Matrix(),
        # layout.MonadTall(),
        # layout.MonadWide(),
        # layout.RatioTile(),
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
    ]

    return layouts
