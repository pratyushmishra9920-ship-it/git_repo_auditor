# Git Repo Auditor

A Python CLI tool for analyzing Git repositories directly from the terminal.

## Features

- View commit history
- Compare branches
- Analyze repository statistics
- Analyze local or remote Git repositories
- Limit commit history results
- JSON and text output formats

## Tech Stack

- Python
- GitPython
- argparse
- Git

## Usage

Run the CLI help:

```bash
python -m git_repo_auditor.main --help
```

View commit history:

```bash
python -m git_repo_auditor.main history
```

Analyze a remote repository:

```bash
python -m git_repo_auditor.main --repo https://github.com/user/repository.git history
```

View repository statistics:

```bash
python -m git_repo_auditor.main stats
```

Compare two branches:

```bash
python -m git_repo_auditor.main compare main feature
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

```
git_repo_auditor/
├── main.py
├── parsers.py
├── handlers.py
├── validation.py
└── __init__.py
```

## Status

This project was built as a learning project to practice Python CLI development, Git, argparse, subprocesses, and repository analysis.
