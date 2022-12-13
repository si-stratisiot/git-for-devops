PYTHON_PATH = $(shell which python3 | sed 's/\//\\\//g')

# make all
all: executables path python


executables:
# create executables
	chmod +x git-devops


path:
# add folder to path
	echo '\nexport PATH="${PWD}:$$PATH"' >> ~/.zshrc


python:
# point to python executable
	sed -i '' '1s/^/\#!$(PYTHON_PATH)\n/' git-devops
