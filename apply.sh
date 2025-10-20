# echo -e "\e[33mEnabling Login Manager (SDDM)\e[0m"
# sudo systemctl enable sddm.service
# sudo systemctl start sddm.service
sudo pacman -S --needed --noconfirm - < packages-needed.txt



cp -R .config/qtile ~/.config/
cp -R .config/rofi ~/.config/
cp -R .config/mimeapps.list ~/.config/
