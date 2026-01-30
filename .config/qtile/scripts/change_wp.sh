#!/usr/bin/env bash
set -euo pipefail

# TARGET_DIR="$HOME/.config/qtile/assets"
TARGET_DIR="$HOME/eos-dotfiles/.config/qtile/assets"
TARGET_FILE="$TARGET_DIR/wallpaper.png"

WALLPAPER=$(yad --file --add-preview --large-preview \
  --title="Select Wallpaper" \
  --file-filter="Images | *.png *.jpg *.jpeg *.webp" \
  --width=900 --height=600)

[[ -z "$WALLPAPER" ]] && exit 0

mkdir -p "$TARGET_DIR"
cp "$WALLPAPER" "$TARGET_FILE"
feh --no-fehbg --bg-scale "$TARGET_FILE"

