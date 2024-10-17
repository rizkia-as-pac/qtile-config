#!/bin/bash

PID_PATH="/tmp/running_flutter.pid"
MAIN_DART="./lib/main.dart"

if [ ! -e "$MAIN_DART" ]; then
  echo "Error: $MAIN_DART does not exist."
  return 1
fi

cleanup() {
  if [ -e "$PID_PATH" ]; then
    cat "$PID_PATH" | xargs kill
  fi
  printf "\nApplication finished.\n"
  exit 0
}

# Execute a command upon an event
# SIGINT (Ctrl+C)
trap cleanup SIGINT

flutter run --pid-file=$PID_PATH >/dev/null 2>&1 &

# move_from, move_to, modify adalah event-event yang vim lakukan ketika user melakukan save file
inotifywait \
  --include '.*\.dart$' \
  -m -r -e modify ./lib | while read path action file; do

  printf "\n\n'$path$file' modified. \n\nPerforming hot reload..."

  if [ -e $PID_PATH ]; then
    cat $PID_PATH | xargs kill -s USR1
  fi
done
