#!/usr/bin/env bash

sudo pacman -S --needed --noconfirm - < packages-repository.txt

set -euo pipefail

# =========================
# Configuration
# =========================

# Timestamp for backup file name
TS="$(date +'%Y%m%d_%H%M%S')"

# Backup file name format: backup_<time>.tar.gz
BACKUP_NAME="backup_${TS}.tar.gz"

# Directory where backups will be stored
BACKUP_DIR="${HOME}/backups"
BACKUP_PATH="${BACKUP_DIR}/${BACKUP_NAME}"

# Targets that may be overwritten by copy operations
# These will be backed up first if they exist
TARGETS=(
  "${HOME}/.config/qtile"
  "${HOME}/.config/rofi"
  "${HOME}/.config/autorandr"
  "${HOME}/.config/mimeapps.list"
  "${HOME}/shell_config"
)

# =========================
# Backup process
# =========================

# Create backup directory if it does not exist
mkdir -p "${BACKUP_DIR}"

# Collect only existing targets
EXISTING=()
for t in "${TARGETS[@]}"; do
  if [[ -e "$t" ]]; then
    EXISTING+=("$t")
  fi
done

# Create a single compressed backup file if there is anything to back up
if (( ${#EXISTING[@]} > 0 )); then
  # Change to HOME so the archive keeps clean relative paths
  (
    cd "$HOME" && tar -czf "$BACKUP_PATH" \
    $(for p in "${EXISTING[@]}"; do echo "${p#$HOME/}"; done)
  )
  echo "Backup created: $BACKUP_PATH"
else
  echo "No existing files found. Backup skipped."
fi

# =========================
# Copy process
# =========================

# Ensure ~/.config directory exists
mkdir -p "${HOME}/.config"

# Copy new configuration files
cp -R .config/qtile "${HOME}/.config/"
cp -R .config/rofi "${HOME}/.config/"
cp -R .config/autorandr "${HOME}/.config/"
cp -R .config/mimeapps.list "${HOME}/.config/"
cp -R ./shell_config "${HOME}/"

echo "Copy process completed successfully."

