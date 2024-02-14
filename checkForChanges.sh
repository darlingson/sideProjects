#!/bin/bash

CONFIG_DIRS=("/etc/application" "/path/to/another/config/directory")
BACKUP_DIR="/vol-a/application-backup"

function handle_error {
  error_msg="$1"
  echo "Error: $error_msg" >&2
  exit 1
}

while true; do
  for dir in "${CONFIG_DIRS[@]}"; do
    change=$(inotifywait -e modify,create,delete -r "$dir" --format "%w%f" 2>&1) || {
      handle_error "Error running inotifywait on $dir: $change"
      continue
    }

    rel_path=${change#${dir}}
    dest_path="${BACKUP_DIR}${rel_path}"
    mkdir -p "$(dirname "$dest_path")" || {
      handle_error "Failed to create directory $dest_path"
      continue
    }

    cp "$change" "$dest_path" || {
      handle_error "Failed to copy $change to $dest_path"
      continue
    }

    echo "$(date): Copied $change to $dest_path"
  done
done
