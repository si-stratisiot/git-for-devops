#!/bin/bash

PYTHON_EXECUTABLE=$(which python3)

echo PYHTON_PATH: $PYTHON_EXECUTABLE

if [ ! -f git-devops ]; then
  echo "Error: file 'git-devops' not found."
  exit 1
fi


if [ "$(head -n 1 git-devops)" != "#!$PYTHON_EXECUTABLE" ]; then
  echo "#!$PYTHON_EXECUTABLE" | cat - git-devops > temp && mv temp git-devops
  echo "Added '#!$PYTHON_EXECUTABLE' to the top of the file 'git-devops'."
fi