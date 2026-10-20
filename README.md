# ModularDOS

A lightweight, single-file DOS-inspired operating system simulator written in Python.

ModularDOS is designed around one core idea:

> If you can write a Python function, you can add a command.

Unlike many DOS clones that use plugins, multiple files, or complex architectures, ModularDOS keeps everything in a single script while remaining easy to expand and maintain.

---

## Features

- DOS-style command prompt
- Virtual filesystem
- File creation and editing
- File viewing
- File copying
- File renaming
- File deletion
- Directory creation and removal
- Built-in calculator
- Automatic HELP menu
- Single-file architecture
- Beginner-friendly codebase

---

## Installation

```bash
git clone https://github.com/yourusername/ModularDOS.git
cd ModularDOS
python ModularDOS.py
```

## Requirements

- Python 3.8+
- No external dependencies

## Design Philosophy

### One File
The entire operating system lives in a single Python file.

### One Function Per Command
Each command is a separate function.

### One Command Registry
All commands are registered in one dictionary.

## Adding Commands

Create a function:

```python
def cmd_hello():
    print("Hello from ModularDOS!")
```

Register it:

```python
COMMANDS["HELLO"] = {
    "function": cmd_hello,
    "description": "Print a greeting"
}
```

That's it.

## License

MIT License
