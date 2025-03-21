# Git Auto Committer

A Python script that automates Git commits using `gitpython`.

## Features
- Commits a specified number of times (up to 100).
- Uses a predefined local file for committing.

## Requirements
- Python 3.x
- `gitpython` (`pip install gitpython`)

## Setup
Before running the script, set up your Git user details:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Usage

```bash
python machine.py
```

## Notes

- Ensure the script is inside a Git-tracked repository.
- The local file used for commits must be set in the script.

---

Just made this for fun because I saw this package on Twitter.
Have some moral values 😆. Don't use this and ruin your code life :)