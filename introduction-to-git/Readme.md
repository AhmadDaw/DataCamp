## Introduction to Git (Datacamp)

### Find Git Version:
`git --version`

### Add a file to staging area:
`git add file.txt`

### Add all files in the dierctory to staging area:
`git add .`

### Commit files in staging area:
`git commit -m 'Commit Message'`

### Show files in staging area:
`git status`

### Compare the differences between 2 files:
`git diff file.txt`

### Compare the differences between file in staging area and last commit:
`git diff -r HEAD file.txt`

### Compare the differences between all files in staging area and last commit:
`git diff -r HEAD`

- `HEAD` Last Commit
- `HEAD~1` Second most recent Commit
- `HEAD~2` Third most recent Commit

### Show commit history:
`git log`

### Viewing changes in a specific commit:
`git show HEAD~2`

### Compare 2 commits:
`git diff HEAD~2 HEAD~3`

### Show chnges line by line:
`git annotate file.txt`

### Remove file from staging area:
`git reset HEAD file.txt`

### Remove all files from staging area:
`git reset HEAD`

### Undo changes to unstaged file:
`git checkout -- file.txt`

### Undo changes to all unstaged files:
`git checkout .`

### Restrict the number of displayed commits 
`git log -3`

### Look at commit history for one file
`git log -3 file.txt`

### Show commits since a date
`git log -since="Apr 2 2022"`

### Show commits between two dates
`git log -since="Apr 2 2022" --until="Apr 11 2022"`

### Revert file to a version from a specific commit (2 ways)
- `git checkout dc9d8fac file.txt`
- `git checkout HEAD~1 file.txt`

### Revert all files (repo) to a version from a specific commit (2 ways)
- `git checkout dc9d8fac`
- `git checkout HEAD~1`

### See what files are not being tracked
`git clean -n`

### Delete files are not being tracked (can't be undone)
`git clean -f`


## Chapter 3

### List settings all types
`git config --list`

### List settings specific type
- `git config --list --global`
- `git config --list --local`
- `git config --list --system`

### change email address
`git config --global user.email johnsmith@datacamp.com`

### change user name
`git config --global user.name 'John Smith'`

### using an alias ci for the command `'commit -m'`
`git config --global alias.ci 'commit -m'`

### Identify branches
`git branch`

### Create new branch
`git checkout -b branch-name`

### Compare 2 branches
`git diff main report`

### Merge 2 branches (source: branch-name) (destination: main)
`git merge branch-name main`

### Compare 2 branches
`git diff main report`

## Chapter 4

### Create a new Repo
- `git init folder-name`
- `cd folder-name`
- `git status`

### Clone a Repo locally
`git clone /home/ahmad/repo`

### Clone a Repo locally and name it repo-name
`git clone /home/ahmad/repo repo-name`

### Clone a Repo remotly
`git clone https://datacamp.com/project`

### Show the name of a remotly cloned repo 
`git remote`

### Show the name of a remotly cloned repo with more information
`git remote -v`

### Add a Repo remotly
`git remote add repo-name https://datacamp.com/project`

### Fetching from a remote main branch
`git fetch origin main`

### Fetching from a remote specific branch (report)
`git fetch origin report`

### Syncronize a localy repo with a remote repo
`git merge origin main`

### Pulling (fetch + merge) from a remote repo to a local repo
`git pull origin main`

### Comapre local repo with remote repo
`git diff origin main`

### Pushing from a local repo (main) to a remote repo (origin)
`git push origin main`

