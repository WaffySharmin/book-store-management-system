# 📚 Book Store Management System

A simple command-line based book store management system written in Python. The project follows a modular structure where each feature is separated into its own file for easy maintenance and readability.

## 📁 Project Structure

book_store/
├── main.py       # Entry point — holds books list and main while loop
├── menu.py       # Displays the main menu
├── heading.py    # Prints section title/header
├── message.py    # Common messages (closing, found, not found, nav)
├── create.py     # Add a new book
├── list.py       # Display all books
├── sell.py       # Sell a book (reduce quantity)
├── update.py     # Update book quantity (add stock)
├── delete.py     # Delete quantity from a book
└── README.md     # Project documentation




## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Create Book** | Add a new book with name and initial quantity |
| 2 | **List Books** | View all books in a formatted table |
| 3 | **Sell Book** | Reduce stock when a book is sold |
| 4 | **Update Book** | Add more stock to an existing book |
| 5 | **Delete** | Remove a specific quantity from a book |


##  Setup Instructions

### Requirements
- Python 3.14.4 or higher
- No external libraries required

### Installation

1. Clone or download the project folder:
  git clone https://github.com/WaffySharmin/book-store-management-system.git
   
2. Verify Python is installed:
   python --version

3. Run the application:
   python main.py
   

## 🚀 Usage

When you run main.py, the following menu appears:


1. Create new book
2. List of books
3. Sell a book
4. Update book qty
5. Delete
0. Exit


### Example — Adding a book


Enter your choice: 1
**************************************************************
--------------------- Create new book ---------------------
**************************************************************
Enter Book Name: Python Basics
Enter Initial Book Quantity: 10
Book Name: Python Basics Successfully Added
1. Back
0. Exit


### Example — Listing books


Enter your choice: 2
---------------------------------------------
|     Book Name       |       Quantity      |
---------------------------------------------
|   Python Basics     |         10          |
---------------------------------------------


### Example — Selling a book


Enter your choice: 3
Enter Book Name: Python Basics
The requested book Found!
Enter Sell Quantity: 3




## 🧩 Module Responsibilities

### menu.py
Contains `print_menu()` — prints the main navigation menu.

### heading.py
Contains `print_title(title)` — prints a decorative section header for each operation.

### message.py
Contains shared message functions used across modules:
- `closing_msg()` — prints exit message
- `back_or_exit()` — prints Back/Exit navigation options
- `book_found_msg()` — prints success message when a book is found
- `book_not_found_msg()` — prints error message when a book is not found

### create.py
Contains `print_create(books)` — handles taking user input and appending a new book to the list.

### list.py
Contains `print_list(books)` — displays all books in a formatted table.

### sell.py
Contains `print_sell(books)` — searches for a book and reduces its quantity after a sale.

### update.py
Contains `print_update(books)` — searches for a book and increases its stock quantity.

### delete.py
Contains `print_delete(books)` — searches for a book and removes a specified quantity.



## 📌 Notes 

- All book data is stored in memory (a Python list). Data will reset when the program exits.
- Each module imports only what it needs from `heading.py` and `message.py` keeping dependencies minimal.
- The `books` list lives in `main.py` and is passed as an argument to each function — no global database file is used.



## Author

Sharmin- sharminmollik12@gmail.com
