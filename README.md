# Furniture Store Management System

A simple **Python command-line application** to manage a furniture store's operations; including furniture inventory, customer records, and sales transactions. Built using core Python concepts like lists, loops, functions, and modules (no external libraries or database required).

## Features

- **Furniture Management**
  - Add new furniture records (ID, type, material, price)
  - View all furniture records
  - Update existing furniture details
  - Search furniture by ID

- **Customer Management**
  - Add new customers (CNIC, name, phone number, age)
  - View all customer records
  - Update customer details
  - Search customer by CNIC

- **Sales Management**
  - Book a sale by linking a customer to a furniture item
  - View all sales records
  - Search sales by customer CNIC

## Project Structure

```
├── main.py        # Main menu-driven program (entry point)
├── module1.py     # Furniture inventory logic (add/view/update/search)
├── module2.py     # Customer records logic (add/view/update/search)
├── sales.py       # Sales logic (linking customers to furniture)
└── README.md      # Project documentation
```

## How It Works

The system stores all data **in-memory** using Python lists (data resets every time the program restarts). Each module handles one part of the store's operations, and `main.py` ties them together through an interactive text menu.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Installation

```bash
git clone https://github.com/your-username/furniture-store-management-system.git
cd furniture-store-management-system
```

### Run the Program

```bash
python main.py
```

## Usage

When you run the program, you'll see a menu like this:

```
***MENU***
1.Furniture info   2.Customer info   3.Sales info
```

Follow the on-screen prompts to add, view, update, or search records.
