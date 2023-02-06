PYTHON_PATH = $(shell which python3 | sed 's/\//\\\//g')

# make all
all: executables path


executables:
# create executables
	chmod +x git-devops
	find installation_scripts -type f -iname "*.sh" -exec chmod +x {} \;


path:
# add folder to path
	installation_scripts/add_to_path.sh


python:
# point to python executable
	installation_scripts/add_shebang.sh

