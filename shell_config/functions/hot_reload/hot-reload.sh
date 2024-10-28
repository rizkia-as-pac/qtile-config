#!/bin/bash

clear

WATCH_PATH=${1:-"./lib"}
INCLUDE=${2:-".dart"}
RUN_COMMAND=${3:-"dart"}

echo "Start observing ${WATCH_PATH} directory."
echo "Observing all ${INCLUDE} files within: ".*\\${INCLUDE}$"."
printf "Run command: ${RUN_COMMAND} <changed_file>${INCLUDE}.\n\n"

# move_from, move_to, modify adalah event-event yang vim lakukan ketika user melakukan save file
inotifywait \
  --include ".*\\${INCLUDE}$" \
  -m -r -e modify $WATCH_PATH | while read path action file; do

  clear
  printf "Performing hot reload on $file file... \n\n"
  $RUN_COMMAND $path$file

done
