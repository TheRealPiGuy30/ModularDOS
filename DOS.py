import os
from pathlib import Path

# ============================================================
# ModularDOS
#
# A lightweight DOS-inspired operating system simulator.
#
# HOW TO ADD A COMMAND:
#
# 1. Create a function:
#
# def cmd_hello():
#     print("Hello World!")
#
# 2. Register it:
#
# COMMANDS["HELLO"] = {
#     "function": cmd_hello,
#     "description": "Print Hello World"
# }
#
# That's it.
# ============================================================

VERSION = "1.0"

# ============================================================
# FILESYSTEM SETUP
# ============================================================

ROOT = Path("virtual_drive")

DIRECTORIES = {
    "GENERAL": ROOT / "GENERAL",
    "DOCUMENTS": ROOT / "DOCUMENTS",
    "HOME": ROOT / "HOME"
}

for directory in DIRECTORIES.values():
    directory.mkdir(parents=True, exist_ok=True)

current_directory = DIRECTORIES["GENERAL"]

# ============================================================
# COMMAND FUNCTIONS
# ============================================================

def cmd_help():
    print("\nAvailable Commands")
    print("-" * 40)

    for name, info in sorted(COMMANDS.items()):
        print(f"{name:<10} {info['description']}")

    print()


def cmd_dir():
    items = sorted(current_directory.iterdir())

    print(f"\n Directory of {current_directory.name}\n")

    if not items:
        print("No files found.")

    for item in items:
        if item.is_dir():
            print(f"<DIR>     {item.name}")
        else:
            print(f"          {item.name}")

    print(f"\n{len(items)} item(s)\n")


def cmd_cd():
    global current_directory

    print("\nAvailable Directories:")

    for name in DIRECTORIES:
        print(f" - {name}")

    target = input("\nDirectory: ").strip().upper()

    if target in DIRECTORIES:
        current_directory = DIRECTORIES[target]
        print(f"Current directory changed to {target}")
    else:
        print("Directory not found.")


def cmd_edit():
    filename = input("Filename: ").strip()

    if not filename:
        return

    filepath = current_directory / filename

    print("\nEnter text below.")
    print("Type EOF on its own line to save.\n")

    lines = []

    while True:
        line = input()

        if line.upper() == "EOF":
            break

        lines.append(line)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f"\nSaved {filename}\n")


def cmd_type():
    filename = input("Filename: ").strip()

    filepath = current_directory / filename

    if not filepath.exists():
        print("File not found.")
        return

    print()

    with open(filepath, "r", encoding="utf-8") as file:
        print(file.read())

    print()


def cmd_copy():
    source = input("Source filename: ").strip()
    destination = input("Destination filename: ").strip()

    source_path = current_directory / source
    destination_path = current_directory / destination

    if not source_path.exists():
        print("Source file not found.")
        return

    with open(source_path, "rb") as src:
        data = src.read()

    with open(destination_path, "wb") as dst:
        dst.write(data)

    print("1 file(s) copied.")


def cmd_del():
    filename = input("Filename: ").strip()

    filepath = current_directory / filename

    if not filepath.exists():
        print("File not found.")
        return

    filepath.unlink()

    print("File deleted.")


def cmd_ren():
    old_name = input("Old filename: ").strip()
    new_name = input("New filename: ").strip()

    old_path = current_directory / old_name
    new_path = current_directory / new_name

    if not old_path.exists():
        print("File not found.")
        return

    old_path.rename(new_path)

    print("File renamed.")


def cmd_mkdir():
    folder_name = input("Folder name: ").strip()

    if not folder_name:
        return

    (current_directory / folder_name).mkdir(exist_ok=True)

    print("Directory created.")


def cmd_rmdir():
    folder_name = input("Folder name: ").strip()

    path = current_directory / folder_name

    if not path.exists():
        print("Directory not found.")
        return

    if not path.is_dir():
        print("Not a directory.")
        return

    if any(path.iterdir()):
        print("Directory is not empty.")
        return

    path.rmdir()

    print("Directory removed.")


def cmd_echo():
    text = input("Text: ")
    print(text)


def cmd_calc():
    expression = input("Expression: ")

    try:
        result = eval(expression)
        print(result)

    except Exception:
        print("Invalid expression.")


def cmd_cls():
    os.system("cls" if os.name == "nt" else "clear")


def cmd_about():
    print(f"""
ModularDOS {VERSION}

A DOS-inspired operating system simulator.

Design Goals:
 - Single file
 - Easy to modify
 - Easy to document
 - Beginner friendly
""")


# ============================================================
# COMMAND REGISTRY
# ============================================================

COMMANDS = {
    "HELP": {
        "function": cmd_help,
        "description": "Show help menu"
    },
    "DIR": {
        "function": cmd_dir,
        "description": "List directory contents"
    },
    "CD": {
        "function": cmd_cd,
        "description": "Change directory"
    },
    "EDIT": {
        "function": cmd_edit,
        "description": "Create or edit a text file"
    },
    "TYPE": {
        "function": cmd_type,
        "description": "Display file contents"
    },
    "COPY": {
        "function": cmd_copy,
        "description": "Copy a file"
    },
    "DEL": {
        "function": cmd_del,
        "description": "Delete a file"
    },
    "REN": {
        "function": cmd_ren,
        "description": "Rename a file"
    },
    "MKDIR": {
        "function": cmd_mkdir,
        "description": "Create a directory"
    },
    "RMDIR": {
        "function": cmd_rmdir,
        "description": "Remove a directory"
    },
    "CLS": {
        "function": cmd_cls,
        "description": "Clear screen"
    },
    "ECHO": {
        "function": cmd_echo,
        "description": "Print text"
    },
    "CALC": {
        "function": cmd_calc,
        "description": "Simple calculator"
    },
    "ABOUT": {
        "function": cmd_about,
        "description": "Display system information"
    }
}

# ============================================================
# BOOT SCREEN
# ============================================================

BOOT_SCREEN = r"""
███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗      █████╗ ██████╗
████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔══██╗██╔══██╗
██╔████╔██║██║   ██║██║  ██║██║   ██║██║     ███████║██████╔╝
██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══██║██╔══██╗
██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗██║  ██║██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

Version 1.0

Volume in drive A has no label.
Directory of A:\

COMMAND.COM
CONFIG.SYS
AUTOEXEC.BAT

3 file(s)

Type HELP for commands.
"""

print(BOOT_SCREEN)

# ============================================================
# MAIN LOOP
# ============================================================

while True:

    prompt = f"A:\\{current_directory.name}> "

    user_input = input(prompt).strip()

    if not user_input:
        continue

    command = user_input.upper()

    if command == "EXIT":
        print("System halted.")
        break

    if command in COMMANDS:
        try:
            COMMANDS[command]["function"]()

        except Exception as error:
            print(f"Error: {error}")

    else:
        print("Bad command or file name.")
