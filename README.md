TODO: what's the git requirements for --help option

## Purpose

As we use GitOps in our organization as primary task management tool it would be nice to GitHubs ability to link to DevOps items using AB#{your work item number}. To achieve that we want to introduce a Git extension that will simplify work items tracking in terminal.

## Examples

Suppose you have a story with ID 1234 and tasks with IDs 5678 and 8765 that belong to the story 1234.

This is how you can start working on the story. It's going to create a branch with the name `1234` and set the branch as a current one.
```
git devops story start 1234
```

Then we want to start working on a task that belongs to the story. It's going to create a branch with the name `1234_5678` and set the branch as a current one.
```
git devops task start 5678
```

Once we are done with working on task 5678 we want to create a pull request for it.
```
git devops task finish
```
It will create a pull request for us against the story branch `1234 <- 1234_5678` and open it in the browser.

We can repeat the same steps for task 8765.

Once we are done with working on story 1234 we want to create a pull request for it against main branch.
```
git devops story finish
```
A new pull request will be created `main <- 1234` and browser will open it.

Note: it's important to follow this pattern of naming branches and creating pull requests. Otherwise, the extension won't be able to find the work item numbers in the branch names.


## Requirements:

Make sure you have Python 3 installed


Git Devops extension relies on `gh` - [GitHub CLI](https://cli.github.com/) tool. And uses it for creating pull requests.

Install `gh` on Mac:

```brew install gh```

[Login](https://cli.github.com/manual/gh_auth_login) with your GitHub account:

```gh auth login```


## Installation:

1. `cd` into Git Devops project folder in your terminal
2. Make makefiles executable:
```
chmod +x Makefile
```
3. Run `make` command
```
make
```
 - This will make `git-devops` file executable
 - Add the current folder to PATH
 - Adds python shebang to the `git-devops` file so it can be executed as a script


TODO: add --help option