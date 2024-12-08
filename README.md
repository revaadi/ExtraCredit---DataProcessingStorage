# In-Memory Database with Transaction Support

## Overview
This project implements an in-memory key-value database with transaction support. It provides methods to:
- `begin_transaction()`: Start a transaction.
- `put(key, value)`: Insert or update key-value pairs during a transaction.
- `get(key)`: Retrieve the value of a key (works outside a transaction as well).
- `commit()`: Save transaction changes permanently.
- `rollback()`: Revert all changes made during the transaction.

## How to Run
1. Install Python 3 on your computer.
2. Save the `db.py` file to your local machine.
3. Open a terminal, navigate to the folder containing `db.py`, and run:
   ```bash
   python3 db.py

## Improvemenets
The assignment instructions should clearly state whether a separate file for testing should be included 
or if testing should be done within the main file.The assignment instructions should clearly state whether a separate testing file is needed or if testing can be done within the main file. 
It would also help to explain how the get() method should behave during a transaction—whether it should show uncommitted changes or not. 
Adding examples for edge cases, like handling nested transactions or invalid keys, would make the task more comprehensive. Providing sample outputs for test cases or automated grading scripts could make grading easier and more consistent.
Encouraging students to create their own test cases could also help them better understand the assignment. 
