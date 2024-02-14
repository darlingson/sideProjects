#!/bin/bash

CONFIG_DIRS=("/etc/application" "/path/to/another/config/directory")
BACKUP_DIR="/vol-a/application-backup"

while true; do
    for dir in "${CONFIG_DIRS[@]}"; do
        change=$(inotifywait -e modify,create,delete -r "$dir" --format "%w%f")
        rel_path=${change#${dir}}
        dest_path="${BACKUP_DIR}${rel_path}"
        mkdir -p "$(dirname "$dest_path")"
        cp "$change" "$dest_path"
        echo "$(date): Copied $change to $dest_path"
    done
done
