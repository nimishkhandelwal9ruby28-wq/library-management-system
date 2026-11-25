# Library Management System

A menu-driven, command-line Library Management System built with Python and text-file storage.

## Features

- Admin login (demo defaults: `admin` / `1234`; optional environment-variable overrides)
- Add, view, edit, search, and delete users
- Add, view, search, and delete books
- Borrow and return books with transaction records
- View books borrowed by a user
- Recommend books by genre
- Collect feedback and rate books
- Display basic library statistics
- Persist users, books, and transactions in local text files

## Technology

- Python 3
- File handling
- Python data structures (lists and dictionaries)

## Project structure

```text
library-management-system/
├── library_management.py
├── books.txt
├── users.txt
├── transactions.txt
├── feedback.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3.9 or later
- No third-party packages required

## Run locally

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the program:

```bash
python library_management.py
```

On some systems, use `python3 library_management.py`.

**Demo admin login (works by default):**
- Username: `admin`
- Password: `1234`

For a private local setup, you can override the demo credentials before starting the program.

**Windows PowerShell**
```powershell
$env:LIBRARY_ADMIN_USERNAME = "your-admin-name"
$env:LIBRARY_ADMIN_PASSWORD = "your-local-password"
python library_management.py
```

**macOS / Linux**
```bash
export LIBRARY_ADMIN_USERNAME="your-admin-name"
export LIBRARY_ADMIN_PASSWORD="your-local-password"
python3 library_management.py
```

The program reads and writes its text files in the same directory as `library_management.py`.

## Data and privacy

The included text files contain demonstration/sample data only. Do not commit real names, addresses, passwords, or other personal information. The data files are plain text and are intended for learning/demo use, not production deployment.

## Notes

This is an educational console project. The demo login is `admin` / `1234`. Change it for private use with environment variables; this is a learning/demo project, not production authentication.
