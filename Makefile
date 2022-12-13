PYTHON_PATH = $(shell which python3 | sed 's/\//\\\//g')

# make all
all: executables path


executables:
# create executables
	chmod +x git-devops-story-start
	chmod +x git-devops-story-finish
	chmod +x git-devops-task-start
	chmod +x git-devops-task-finish


path:
# add folder to path
	echo "\nexport PATH="${PWD}:${PATH}"" >> ~/.zshrc


python:
# point to python executable
	sed -i '' '1s/^/\#!$(PYTHON_PATH)\n/' git-devops-story-start
