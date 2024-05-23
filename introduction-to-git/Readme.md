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
