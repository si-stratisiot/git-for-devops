# Git Devops Extension

## Purpose

As we use GitOps in our organization as primary task management tool it would be nice to GitHubs ability to link to DevOps items using AB#{your work item number}. To achieve that we want to introduce a Git extension that will simplify work items tracking in terminal.

## Features

- Start working on a story or task by creating a branch with the corresponding ID.
- Create pull requests for stories and tasks directly from the terminal.
- Easy integration with GitHub's DevOps items using AB#{work item number}.
- Follows a clear pattern of naming branches and creating pull requests.


## Examples

Suppose we have a story with ID `1234` and tasks with IDs `5678` and `8765` that belong to the story `1234`.

### 1. Starting a Story
To start working on a story with ID `1234`, run the following command to create a branch named `1234` and set it as the current branch:
```
git devops story start 1234
```


### 2. Starting a Task
Then we want to start working on our first task with ID `5678` that belongs to the story `1234`, run the following command to create a branch named `1234_5678` and set it as the current branch:
```
git devops task start 5678
```


### 3. Finishing a Task
Once work on task `5678` is complete, run the following command to create a pull request for it against the story branch `1234 <- 1234_5678` and open it in the browser:

```
git devops task finish
```

### 4. Working on a Second Task
We can repeat the same steps for task `8765`.

### 5. Finishing a Story
Once work on story `1234` is complete, run the following command to create a pull request for it against the main branch `main <- 1234` and open it in the browser:
```
git devops story finish
```


**Note:** it's important to follow the pattern of naming branches and creating pull requests as described above. Otherwise, the extension won't be able to find the work item numbers in the branch names.

## Prerequisites
There are several prerequisites that need to be met before using the extension:
- Make sure you have Python 3 installed
- Git Devops extension relies on `gh` - [GitHub CLI](https://cli.github.com/) tool, and uses it for creating pull requests.
  - Install `gh` on Mac:

      ```
      brew install gh
      ```
  - [Login](https://cli.github.com/manual/gh_auth_login) with your GitHub account:

      ```
      gh auth login
      ```


## Installation
- Download the project to your local machine
- `cd` into Git Devops project folder in your terminal
- Make Makefile executable:
  ```
  chmod +x Makefile
  ```
- Run `make` command
  ```
  make
  ```
  - This will make `git-devops` file executable
  - Add the current folder to `PATH` so that git can find the git-devops file
  - Add python shebang to the `git-devops` file so it can be executed as a script (i.e. `#!/usr/bin/env python3`)


## TODO
- Add `--help` option
- Add unit tests
- Add auto-completion





