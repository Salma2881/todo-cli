# todo-cli

A lightweight command-line task manager built with Python and SQLite. No external dependencies required.

## Features

- Add, list, complete, and delete tasks
- Persistent storage with SQLite
- Color-coded terminal output
- Filter between active and all tasks

## Usage

```bash
# Add a task
python todo.py add "Buy groceries"

# List active tasks
python todo.py list

# List all tasks (including completed)
python todo.py list --all

# Mark a task as done
python todo.py done 1

# Delete a task
python todo.py delete 1
```

## Installation

```bash
git clone https://github.com/Salma2881/todo-cli.git
cd todo-cli
python todo.py list
```

No dependencies to install — uses only Python's standard library.

## Tech stack

- **Python 3.10+**
- **SQLite** via `sqlite3` (stdlib)
- **argparse** for CLI parsing (stdlib)

## License

MIT