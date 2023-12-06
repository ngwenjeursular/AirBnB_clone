#0x00. AirBnB clone - The console

# AirBnB Clone Project

## Welcome

Welcome to the AirBnB clone project! This project is the initial step in constructing a full-fledged web application resembling the functionality of AirBnB.
The primary focus of this phase is to develop a command interpreter for managing AirBnB objects.

## Project Overview

### Command Interpreter

The command interpreter, similar to the Shell, is designed specifically for handling objects within the AirBnB project. It allows users to create new objects, retrieve objects from various sources, perform operations on objects, update object attributes, and destroy objects.

### Learning Objectives

By the end of this project, you will gain knowledge in:

- Creating a Python package
- Developing a command interpreter using the `cmd` module
- Implementing unit testing in a large project
- Serializing and deserializing a class
- Reading and writing JSON files
- Managing datetime in Python
- Understanding UUID (Universally Unique Identifier)
- Working with `*args` and `**kwargs`
- Handling named arguments in functions

### Requirements

#### Python Scripts

- Editors: vi, vim, emacs
- Interpreter: Python 3.8.5 on Ubuntu 20.04 LTS
- File structure: Follow specific guidelines for file endings, shebang, README, and pycodestyle
- Documentation: Thorough documentation for modules, classes, and functions

#### Python Unit Tests

- Test structure: Organize tests in a 'tests' folder mirroring the project structure
- Unittest module: Use the `unittest` module for testing
- Execution: Tests should be executable using specific commands

#### GitHub Guidelines

- Repository: Each group should have one project repository. Cloning/forking existing repositories with the same name before the second deadline may result in a 0% score
- Collaboration: Encourages collaboration on test cases but emphasizes individual work on solutions

### More Information

Refer to the provided resources and execution examples for detailed information on project execution, testing, and GitHub guidelines.

## Getting Started

### Prerequisites

- Python 3.8.5
- Ubuntu 20.04 LTS
- Text editors: vi, vim, or emacs

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/AirBnB_clone.git
```

2.  Navigate to the project folder:
	```
	cd AirBnB_clone
```

3. Run the command interpreter:
     ```
     ./console.py
    ```

# Usage:
The command interpreter supports both interactive and non-interactive modes. In interactive mode, simply type commands after the prompt (hbnb). In non-interactive mode, provide commands through standard input or script files.

## Examples:
#### Interactive mode:
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

#### Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

# Tasks:
## Task 0:
Write a detailed README.md including project description, command interpreter overview, how to start and use it, and examples. Create an AUTHORS file at the root, listing all contributors.
[0. README](README.md)
[AUTHORS](AUTHORS)

## Task 1:
Write beautiful code that passes the pycodestyle checks.
