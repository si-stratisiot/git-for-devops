#!/bin/bash

if [ ! -f ~/.zshrc ]; then
  touch ~/.zshrc
  echo "Created ~/.zshrc file."
fi

# Get the current directory
current_dir=$(pwd)

# Check if the current directory is already in the PATH
if ! grep -q "$current_dir" ~/.zshrc; then
  # If not, add it
  echo "export PATH=\"\$PATH:$current_dir\"" >> ~/.zshrc
fi
