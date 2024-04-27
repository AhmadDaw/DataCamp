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
