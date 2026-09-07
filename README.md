# Git Repo Auditor

A Python CLI tool for analyzing Git repositories directly from the terminal.

## Features

* View commit history
* Compare branches
* Analyze repository statistics
* Analyze contributor and commit activity
* Check repository health
* Analyze local or remote Git repositories
* Limit commit history results

## Tech Stack

* Python
* GitPython
* argparse
* Git

## Usage

### Run the CLI help

```bash
python -m git_repo_auditor.main --help
```

### View commit history

```bash
python -m git_repo_auditor.main --repo https://github.com/user/repository.git history
```

Limit the number of commits displayed:

```bash
python -m git_repo_auditor.main --repo https://github.com/user/repository.git history --limit 5
```

### Analyze a remote repository

```bash
python -m git_repo_auditor.main --repo https://github.com/user/repository.git history
```

### View repository statistics

```bash
python -m git_repo_auditor.main --repo https://github.com/user/repository.git stats
```

### Compare two branches

```bash
python -m git_repo_auditor.main --repo https://github.com/user/repository.git compare main feature
```

### Analyze repository activity

```bash
python -m git_repo_auditor.main --repo https://github.com/user/repository.git activity
```

### Check repository health

```bash
python -m git_repo_auditor.main --repo https://github.com/user/repository.git health
```

## Installation

Clone the repository and create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

```text
git_repo_auditor/
├── __init__.py
├── main.py
├── parsers.py
├── handlers.py
├── validation.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Commands

| Command    | Description                             |
| ---------- | --------------------------------------- |
| `history`  | Display commit history                  |
| `compare`  | Compare two branches                    |
| `stats`    | Display repository statistics           |
| `activity` | Analyze contributor and commit activity |
| `health`   | Check repository health                 |

## Status

This project was built as a learning project to practice Python CLI development, Git, `argparse`, subprocesses, and repository analysis.

