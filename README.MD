# Virtual Library CLI - README

A fully-featured command-line interface (CLI) for managing a virtual library. Built using Python and SQLAlchemy ORM, this tool lets you manage authors, books, users, and book loans smoothly through an intuitive menu.

---

## 🚀 Features

* **Manage Authors**: Add, update, delete, and list authors
* **Manage Books**: Add, update, delete, and list books (linked to authors)
* **Manage Users**: Add and list users (with auto-generated card numbers)
* **Track Loans**: Borrow books, return them, and view loan history
* **Smart Book Adding**: Automatically prompt to create an author if their ID doesn't exist during book creation
* **Timestamps**: Loans are timestamped on borrow and return
* **Data Persistence**: Uses SQLite for saving your data (`library.db`)

---

## ⚙️ Setup

### Prerequisites

* Python 3.10+
* Pipenv (recommended)

### Installation

1. Clone the repository:

```bash
git clone <repo-url>

```

2. Navigate to your directory:
```bash
cd virtual-library-cli

```
3. Install dependencies and activate the virtual environment:

```bash
pipenv install
pipenv shell
```

4. Run the application:

```bash
python main.py
```

---

## Complete Usage Guide

### Main Menu

When you start the app, you'll see:

```
--- Virtual Library CLI ---
1. Add record
2. Update record
3. Delete record
4. List records
5. Return a loan
6. Exit
```

---

### Adding Records

#### 1. Add an Author

* Select `1` (Add) → `1` (Author)
* Input:

  ```
  First name: George
  Last name: Orwell
  Birth year: 1903
  ```

#### 2. Add a Book

* Select `1` (Add) → `2` (Book)
* Input:

  ```
  Book title: 1984
  Author ID: 5
  ```
* If the Author ID does not exist, you'll be prompted:

  ```
  Author ID not found.
  Enter author first name: George
  Enter author last name: Orwell
  Enter birth year: 1903
  ```
* A new author will be created and used for the book.

#### 3. Add a User

* Select `1` (Add) → `3` (User)
* Input:

  ```
  Username: reader_jane
  ```
* The system auto-generates a unique 6-digit card number.

#### 4. Add a Loan

* Select `1` (Add) → `4` (Loan)
* Input:

  ```
  Book ID: 2
  User ID: 1
  ```
* Loan is timestamped with the current date and time.

---

### Updating Records

1. Select `2` (Update)
2. Choose the entity (Author, Book, etc.)
3. Example for a Book:

   ```
   Enter Book ID to update: 2
   New title (or blank to skip): Animal Farm
   New author ID (or blank to skip): 6
   ```

---

###  Deleting Records

1. Select `3` (Delete)
2. Choose the entity
3. Input the corresponding ID:

   ```
   Enter Book ID to delete: 2
   ```

---

###  Listing Records

1. Select `4` (List)
2. Choose one:

   * `1` = Authors (with count of books)
   * `2` = Books (title + author name)
   * `3` = Users (username + card number)
   * `4` = Loans (borrow + return dates)

---

### Returning Books

1. Select `5` from the main menu
2. Enter:

   ```
   Enter loan ID to return: 3
   ```
3. The system sets the return timestamp automatically.

---

## Database Schema Overview

| Table       | Fields                                                   |
| ----------- | -------------------------------------------------------- |
| **authors** | `id`, `first_name`, `last_name`, `birth_year`            |
| **books**   | `id`, `title`, `author_id` (foreign key)                 |
| **users**   | `id`, `username`, `card_number`                          |
| **loans**   | `id`, `book_id`, `user_id`, `borrowed_at`, `returned_at` |

---

## Just For Your Information(FYI) 
* Use **List** before updating/deleting to get correct IDs
* Users get **auto-generated 6-digit card numbers**
* All data is safely stored in `library.db`

---

Made with ❤️ using Python 🐍 and SQLAlchemy ⚙️
Simple. Elegant. Functional.

---
