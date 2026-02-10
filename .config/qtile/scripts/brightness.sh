#!/usr/bin/env bash
brightness_max="$(brightnessctl m)"
step=$((brightness_max / 100))  # 1%

case $1 in
    brightness_up)
        brightnessctl set "${step}+"
        ;;
    brightness_down)
        brightnessctl set "${step}-"
        ;;
esac

brightness="$(brightnessctl g)"
# echo "$brightness_percentage"
brightness_percentage=$(echo "scale=2; ($brightness / $brightness_max) * 100" | bc)

# displays the notification
dunstify -t 1000 -r 2593 -u normal " $brightness_percentage%" -h int:value:$brightness_percentage -h string:hlcolor:"#7f7fff"
