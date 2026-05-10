#!/usr/bin/env python3
import sys
import subprocess

# Commit hash to fix
target_hash = "5f71e48"

# Read the rebase todo file
if len(sys.argv) > 1:
    todo_file = sys.argv[1]
    with open(todo_file, 'r') as f:
        lines = f.readlines()
    
    # Find the target commit and change it from 'pick' to 'reword'
    modified = False
    for i, line in enumerate(lines):
        if line.startswith(target_hash):
            # Replace 'pick' with 'reword'
            parts = line.split(' ', 1)
            if parts[0] in ['pick', 'p']:
                lines[i] = f'reword {parts[1]}'
                modified = True
                print(f"Marked {target_hash} for reword", file=sys.stderr)
                break
    
    if modified:
        with open(todo_file, 'w') as f:
            f.writelines(lines)
    else:
        print(f"Warning: could not find {target_hash} in rebase todo", file=sys.stderr)
