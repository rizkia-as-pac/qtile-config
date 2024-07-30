#!/usr/bin/env bash
brightness_max="$(brightnessctl m)"

case $1 in
    brightness_up)
    # Increases brightness
    brightnessctl set 5+ 
    ;;

    brightness_down)
    # Decreases brightness
    brightnessctl set 5- 
    ;;
esac

brightness="$(brightnessctl g)"
# echo "$brightness_percentage"
brightness_percentage=$(echo "scale=2; ($brightness / $brightness_max) * 100" | bc)

# displays the notification
dunstify -t 1000 -r 2593 -u normal " $brightness_percentage%" -h int:value:$brightness_percentage -h string:hlcolor:"#7f7fff"
