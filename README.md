# Expense Tracker

To get started with the **Expense Tracker** project, follow these steps:

### 1\. Clone the Repository

First, clone the repository from GitHub using the following command:

git clone <https://github.com/ROHANDAS2003/expense-tracker>

(Replace your-username with your actual GitHub username if needed.)

This will create a folder named expense-tracker in your current directory. Inside this folder, you'll find the following files:

- expense_tracker.py: The main script to run the expense tracker.
- expenses.csv: The CSV file where expenses will be stored.

### 2\. Navigate to the Project Directory

After cloning the repository, navigate to the project folder using the command:

cd expense-tracker

### 3\. Dependencies

There are no external Python libraries or dependencies for this project, as it uses only Python's standard library (csv, os). Therefore, you don't need to install any external packages.

However, make sure you have Python 3.x installed on your system. You can check if Python is installed by running:

python --version

If Python is not installed, [download and install Python from here](https://www.python.org/downloads/).

### 4\. Run the Expense Tracker

To start the expense tracker, use the following command in the terminal:

python expense_tracker.py

The application will present you with a menu where you can add, edit, delete, and display expenses.

## Folder Structure

After cloning, the folder structure will look like this:

expense-tracker/

│
├── expense_tracker.py # Main Python script for the application
├── expenses.csv # CSV file storing expenses
├── README.md # (Optional) A file for documenting the project
└── LICENSE # (Optional) License information

- expense_tracker.py: The script containing the core logic of the expense tracker.
- expenses.csv: A CSV file that will store your expenses. If it does not exist, the program will create it the first time an expense is added.

## Setting Up the CSV File

You don't need to manually create the expenses.csv file. The program will automatically generate this file when you first add an expense. However, if you'd like to start with an empty expenses.csv file, you can create one with this format:

date,category,description,amount

This CSV file will grow as you add more expenses.