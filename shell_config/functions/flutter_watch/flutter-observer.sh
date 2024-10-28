#!/bin/bash

PID_PATH="/tmp/running_flutter.pid"
WATCH_PATH=${1:-"./lib"}
MAIN_DART="$WATCH_PATH/main.dart"

if [ ! -e "$MAIN_DART" ]; then
  echo "Error: $MAIN_DART does not exist."
  exit 0
fi

if [ ! -e "$PID_PATH" ]; then
  printf "\nError: $PID_PATH does not exist."
  echo "run this command first."
  printf " flutter run --pid-file=/tmp/running_flutter.pid\n\n"
  exit 0
fi

cleanup() {
  if [ -e "$PID_PATH" ]; then
    cat "$PID_PATH" | xargs kill
  fi
  printf "\nObserver finished.\n"
  exit 0
}

# Execute a command upon an event
# SIGINT (Ctrl+C)
trap cleanup SIGINT

# move_from, move_to, modify adalah event-event yang vim lakukan ketika user melakukan save file
inotifywait \
  --include '.*\.dart$' \
  -m -r -e modify $WATCH_PATH | while read path action file; do

  # TODO: check if PID_PATH still exist or not

  printf "\n\n'$path$file' modified. \n\nSend signal to trigger hot reload."

  if [ -e $PID_PATH ]; then
    cat $PID_PATH | xargs kill -s USR1
  fi
done
