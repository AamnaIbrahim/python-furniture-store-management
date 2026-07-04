# Furniture Store Management System

A **Python desktop application** (with both a Tkinter GUI and a command-line interface) to manage a furniture store's operations including furniture inventory, customer records, and sales transactions. Built using core Python concepts like lists, loops, functions, and modules (no external libraries or database required).

## Desktop GUI

The app now includes a dark-themed **Tkinter GUI** (`gui.py`) with a **Purple / White / Black** color scheme:

- Tabbed interface — Furniture, Customers, Sales
- Add/Update forms with input validation (no crashes on bad input)
- Searchable, sortable-looking tables (Treeview) instead of raw console text
- Click a row to auto-fill the form for quick editing
- Dropdown selectors in the Sales tab — no need to remember IDs

> Prefer the terminal? The original CLI (`main.py`) still works exactly the same way.

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
├── gui.py         # Tkinter desktop GUI (recommended entry point)
├── main.py        # Command-line menu-driven program (alternative entry point)
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

**Desktop GUI (recommended):**
```bash
python gui.py
```

**Command-line version:**
```bash
python main.py
```

## Usage

### GUI
Launch `gui.py` to open the dark purple-themed desktop app. Use the tabs at the top (Furniture / Customers / Sales) to add, update, and search records through forms and tables — no typing raw menu numbers required.

### CLI
When you run `main.py`, you'll see a menu like this:

```
***MENU***
1.Furniture info   2.Customer info   3.Sales info
```

Follow the on-screen prompts to add, view, update, or search records.

Know that the data is not saved to a file or database — everything is lost when the program closes (or the GUI window closes).

## Future Improvements

- Add persistent storage (file handling or SQLite database) so records survive a restart
- Convert to an object-oriented design (classes for Furniture, Customer, Sale)
- Add data export (CSV/PDF invoice generation) from the GUI
- Package the GUI as a standalone `.exe` using PyInstaller

