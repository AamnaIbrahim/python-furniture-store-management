import tkinter as tk
from tkinter import ttk, messagebox

import module1
import module2
import sales as sales_module


BG = "#0d0a12"          # near-black background
CARD_BG = "#1a1424"     # dark purple-black cards
ACCENT = "#b98cff"      # light purple accent
ACCENT_DARK = "#8a5ce6" # deeper purple for hover/active
TEXT = "#ffffff"        # white text
SUBTEXT = "#c9b8e8"     # soft light purple for secondary text
ENTRY_BG = "#120e1a"    # entry field background
SUCCESS = "#4caf50"
DANGER = "#e05561"


class FurnitureStoreApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Furniture Store Management System")
        self.geometry("1000x650")
        self.configure(bg=BG)
        self.minsize(900, 600)

        self._build_style()
        self._build_header()
        self._build_tabs()

    # ---------------- STYLE ----------------
    def _build_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("TNotebook", background=BG, borderwidth=0)
        style.configure("TNotebook.Tab", background=CARD_BG, foreground=SUBTEXT,
                         padding=(20, 10), font=("Segoe UI", 11, "bold"))
        style.map("TNotebook.Tab", background=[("selected", ACCENT)],
                  foreground=[("selected", "#0d0a12")])

        style.configure("Treeview", background=CARD_BG, fieldbackground=CARD_BG,
                         foreground=TEXT, rowheight=28, font=("Segoe UI", 10),
                         borderwidth=0)
        style.configure("Treeview.Heading", background=ACCENT_DARK, foreground="white",
                         font=("Segoe UI", 10, "bold"), padding=6)
        style.map("Treeview", background=[("selected", ACCENT)],
                  foreground=[("selected", "#0d0a12")])

        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8,
                         background=CARD_BG, foreground=TEXT)
        style.map("TButton", background=[("active", "#2a2036")])
        style.configure("Accent.TButton", background=ACCENT, foreground="#0d0a12")
        style.map("Accent.TButton", background=[("active", ACCENT_DARK)],
                  foreground=[("active", "white")])

    # ---------------- HEADER ----------------
    def _build_header(self):
        header = tk.Frame(self, bg=BG, pady=15)
        header.pack(fill="x")

        tk.Label(header, text="Furniture Store Manager", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(side="left", padx=20)

    # ---------------- TABS ----------------
    def _build_tabs(self):
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.furniture_tab = FurnitureTab(notebook)
        self.customer_tab = CustomerTab(notebook)
        self.sales_tab = SalesTab(notebook, self.customer_tab, self.furniture_tab)

        notebook.add(self.furniture_tab, text="  Furniture  ")
        notebook.add(self.customer_tab, text="  Customers  ")
        notebook.add(self.sales_tab, text="  Sales  ")

        # Refresh sales dropdowns whenever the tab is clicked
        notebook.bind("<<NotebookTabChanged>>", lambda e: self.sales_tab.refresh_dropdowns())


# FURNITURE TAB

class FurnitureTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG)
        self._build_form()
        self._build_table()
        self.refresh_table()

    def _build_form(self):
        card = tk.Frame(self, bg=CARD_BG, padx=20, pady=15)
        card.pack(fill="x", padx=15, pady=15)

        tk.Label(card, text="Add / Update Furniture", bg=CARD_BG, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 10))

        labels = ["ID", "Type", "Material", "Price"]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(card, text=label, bg=CARD_BG, fg=SUBTEXT,
                     font=("Segoe UI", 10)).grid(row=1, column=i, sticky="w")
            ent = tk.Entry(card, width=16, font=("Segoe UI", 10), bg=ENTRY_BG,
                            fg=TEXT, insertbackground=TEXT, relief="flat")
            ent.grid(row=2, column=i, padx=8, pady=5, ipady=4)
            self.entries[label] = ent

        btn_frame = tk.Frame(card, bg=CARD_BG)
        btn_frame.grid(row=3, column=0, columnspan=4, sticky="w", pady=(10, 0))

        ttk.Button(btn_frame, text="➕ Add Record", style="Accent.TButton",
                   command=self.add_record).pack(side="left", padx=(0, 8))
        ttk.Button(btn_frame, text="✏️ Update Selected", style="Accent.TButton",
                   command=self.update_record).pack(side="left", padx=(0, 8))
        ttk.Button(btn_frame, text="🗑️ Clear Form", command=self.clear_form).pack(side="left")

    def _build_table(self):
        card = tk.Frame(self, bg=CARD_BG)
        card.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        search_frame = tk.Frame(card, bg=CARD_BG, pady=8, padx=10)
        search_frame.pack(fill="x")
        tk.Label(search_frame, text="🔍 Search by ID:", bg=CARD_BG, fg=SUBTEXT,
                 font=("Segoe UI", 10)).pack(side="left")
        self.search_entry = tk.Entry(search_frame, width=15, bg=ENTRY_BG, fg=TEXT,
                                      insertbackground=TEXT, relief="flat")
        self.search_entry.pack(side="left", padx=8, ipady=3)
        ttk.Button(search_frame, text="Search", command=self.search_record).pack(side="left", padx=4)
        ttk.Button(search_frame, text="Show All", command=self.refresh_table).pack(side="left")

        columns = ("ID", "Type", "Material", "Price")
        self.tree = ttk.Treeview(card, columns=columns, show="headings", height=14)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        for i in range(0, len(module1.furniture), 4):
            self.tree.insert("", "end", values=(module1.furniture[i], module1.furniture[i+1],
                                                  module1.furniture[i+2], module1.furniture[i+3]))

    def search_record(self):
        query = self.search_entry.get().strip()
        if not query:
            self.refresh_table()
            return
        try:
            query_id = int(query)
        except ValueError:
            messagebox.showerror("Invalid input", "ID must be a number.")
            return

        self.tree.delete(*self.tree.get_children())
        for i in range(0, len(module1.furniture), 4):
            if module1.furniture[i] == query_id:
                self.tree.insert("", "end", values=(module1.furniture[i], module1.furniture[i+1],
                                                      module1.furniture[i+2], module1.furniture[i+3]))
                return
        messagebox.showinfo("Not found", f"No furniture with ID {query_id}")

    def on_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        self.entries["ID"].delete(0, "end"); self.entries["ID"].insert(0, values[0])
        self.entries["Type"].delete(0, "end"); self.entries["Type"].insert(0, values[1])
        self.entries["Material"].delete(0, "end"); self.entries["Material"].insert(0, values[2])
        self.entries["Price"].delete(0, "end"); self.entries["Price"].insert(0, values[3])

    def clear_form(self):
        for ent in self.entries.values():
            ent.delete(0, "end")

    def add_record(self):
        try:
            fid = int(self.entries["ID"].get())
            ftype = self.entries["Type"].get().strip()
            material = self.entries["Material"].get().strip()
            price = float(self.entries["Price"].get())
        except ValueError:
            messagebox.showerror("Invalid input", "ID must be a number and Price must be a number.")
            return

        if fid < 0:
            messagebox.showerror("Invalid input", "ID cannot be negative.")
            return
        if price < 0:
            messagebox.showerror("Invalid input", "Price cannot be negative.")
            return

        if not ftype or not material:
            messagebox.showerror("Invalid input", "Type and Material cannot be empty.")
            return

        if fid in module1.furniture:
            messagebox.showerror("Duplicate ID", "This ID is already assigned to another item.")
            return

        module1.furniture.extend([fid, ftype, material, price])
        messagebox.showinfo("Success", "Furniture record added!")
        self.clear_form()
        self.refresh_table()

    def update_record(self):
        try:
            fid = int(self.entries["ID"].get())
        except ValueError:
            messagebox.showerror("Invalid input", "ID must be a number.")
            return

        if fid not in module1.furniture:
            messagebox.showerror("Not found", "No furniture record with this ID.")
            return

        try:
            ftype = self.entries["Type"].get().strip()
            material = self.entries["Material"].get().strip()
            price = float(self.entries["Price"].get())
        except ValueError:
            messagebox.showerror("Invalid input", "Price must be a number.")
            return

        if price < 0:
            messagebox.showerror("Invalid input", "Price cannot be negative.")
            return

        for i in range(0, len(module1.furniture), 4):
            if module1.furniture[i] == fid:
                module1.furniture[i+1] = ftype
                module1.furniture[i+2] = material
                module1.furniture[i+3] = price
                break

        messagebox.showinfo("Success", "Furniture record updated!")
        self.clear_form()
        self.refresh_table()


# CUSTOMER TAB

class CustomerTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG)
        self._build_form()
        self._build_table()
        self.refresh_table()

    def _build_form(self):
        card = tk.Frame(self, bg=CARD_BG, padx=20, pady=15)
        card.pack(fill="x", padx=15, pady=15)

        tk.Label(card, text="Add / Update Customer", bg=CARD_BG, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 10))

        labels = ["CNIC", "Name", "Phone", "Age"]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(card, text=label, bg=CARD_BG, fg=SUBTEXT,
                     font=("Segoe UI", 10)).grid(row=1, column=i, sticky="w")
            ent = tk.Entry(card, width=16, font=("Segoe UI", 10), bg=ENTRY_BG,
                            fg=TEXT, insertbackground=TEXT, relief="flat")
            ent.grid(row=2, column=i, padx=8, pady=5, ipady=4)
            self.entries[label] = ent

        btn_frame = tk.Frame(card, bg=CARD_BG)
        btn_frame.grid(row=3, column=0, columnspan=4, sticky="w", pady=(10, 0))

        ttk.Button(btn_frame, text="➕ Add Record", style="Accent.TButton",
                   command=self.add_record).pack(side="left", padx=(0, 8))
        ttk.Button(btn_frame, text="✏️ Update Selected", style="Accent.TButton",
                   command=self.update_record).pack(side="left", padx=(0, 8))
        ttk.Button(btn_frame, text="🗑️ Clear Form", command=self.clear_form).pack(side="left")

    def _build_table(self):
        card = tk.Frame(self, bg=CARD_BG)
        card.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        search_frame = tk.Frame(card, bg=CARD_BG, pady=8, padx=10)
        search_frame.pack(fill="x")
        tk.Label(search_frame, text="🔍 Search by CNIC:", bg=CARD_BG, fg=SUBTEXT,
                 font=("Segoe UI", 10)).pack(side="left")
        self.search_entry = tk.Entry(search_frame, width=15, bg=ENTRY_BG, fg=TEXT,
                                      insertbackground=TEXT, relief="flat")
        self.search_entry.pack(side="left", padx=8, ipady=3)
        ttk.Button(search_frame, text="Search", command=self.search_record).pack(side="left", padx=4)
        ttk.Button(search_frame, text="Show All", command=self.refresh_table).pack(side="left")

        columns = ("CNIC", "Name", "Phone", "Age")
        self.tree = ttk.Treeview(card, columns=columns, show="headings", height=14)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        for i in range(0, len(module2.customer), 4):
            self.tree.insert("", "end", values=(module2.customer[i], module2.customer[i+1],
                                                  module2.customer[i+2], module2.customer[i+3]))

    def search_record(self):
        query = self.search_entry.get().strip()
        if not query:
            self.refresh_table()
            return
        try:
            query_id = int(query)
        except ValueError:
            messagebox.showerror("Invalid input", "CNIC must be a number.")
            return

        self.tree.delete(*self.tree.get_children())
        for i in range(0, len(module2.customer), 4):
            if module2.customer[i] == query_id:
                self.tree.insert("", "end", values=(module2.customer[i], module2.customer[i+1],
                                                      module2.customer[i+2], module2.customer[i+3]))
                return
        messagebox.showinfo("Not found", f"No customer with CNIC {query_id}")

    def on_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        self.entries["CNIC"].delete(0, "end"); self.entries["CNIC"].insert(0, values[0])
        self.entries["Name"].delete(0, "end"); self.entries["Name"].insert(0, values[1])
        self.entries["Phone"].delete(0, "end"); self.entries["Phone"].insert(0, values[2])
        self.entries["Age"].delete(0, "end"); self.entries["Age"].insert(0, values[3])

    def clear_form(self):
        for ent in self.entries.values():
            ent.delete(0, "end")

    def add_record(self):
        try:
            cnic = int(self.entries["CNIC"].get())
            name = self.entries["Name"].get().strip()
            phone = int(self.entries["Phone"].get())
            age = int(self.entries["Age"].get())
        except ValueError:
            messagebox.showerror("Invalid input", "CNIC, Phone, and Age must be numbers.")
            return

        if cnic < 0:
            messagebox.showerror("Invalid input", "CNIC cannot be negative.")
            return
        if phone < 0:
            messagebox.showerror("Invalid input", "Phone number cannot be negative.")
            return
        if age < 0:
            messagebox.showerror("Invalid input", "Age cannot be negative.")
            return

        if not name:
            messagebox.showerror("Invalid input", "Name cannot be empty.")
            return

        if cnic in module2.customer:
            messagebox.showerror("Duplicate CNIC", "This CNIC is already registered.")
            return

        module2.customer.extend([cnic, name, phone, age])
        messagebox.showinfo("Success", "Customer record added!")
        self.clear_form()
        self.refresh_table()

    def update_record(self):
        try:
            cnic = int(self.entries["CNIC"].get())
        except ValueError:
            messagebox.showerror("Invalid input", "CNIC must be a number.")
            return

        if cnic not in module2.customer:
            messagebox.showerror("Not found", "No customer record with this CNIC.")
            return

        try:
            name = self.entries["Name"].get().strip()
            phone = int(self.entries["Phone"].get())
            age = int(self.entries["Age"].get())
        except ValueError:
            messagebox.showerror("Invalid input", "Phone and Age must be numbers.")
            return

        if phone < 0:
            messagebox.showerror("Invalid input", "Phone number cannot be negative.")
            return
        if age < 0:
            messagebox.showerror("Invalid input", "Age cannot be negative.")
            return

        for i in range(0, len(module2.customer), 4):
            if module2.customer[i] == cnic:
                module2.customer[i+1] = name
                module2.customer[i+2] = phone
                module2.customer[i+3] = age
                break

        messagebox.showinfo("Success", "Customer record updated!")
        self.clear_form()
        self.refresh_table()


# SALES TAB

class SalesTab(tk.Frame):
    def __init__(self, parent, customer_tab, furniture_tab):
        super().__init__(parent, bg=BG)
        self.customer_tab = customer_tab
        self.furniture_tab = furniture_tab
        self._build_form()
        self._build_table()
        self.refresh_table()

    def _build_form(self):
        card = tk.Frame(self, bg=CARD_BG, padx=20, pady=15)
        card.pack(fill="x", padx=15, pady=15)

        tk.Label(card, text="Book a Sale", bg=CARD_BG, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 10))

        tk.Label(card, text="Customer (CNIC - Name)", bg=CARD_BG, fg=SUBTEXT,
                 font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w")
        self.customer_var = tk.StringVar()
        self.customer_dropdown = ttk.Combobox(card, textvariable=self.customer_var,
                                               width=25, state="readonly")
        self.customer_dropdown.grid(row=2, column=0, padx=8, pady=5)

        tk.Label(card, text="Furniture (ID - Type)", bg=CARD_BG, fg=SUBTEXT,
                 font=("Segoe UI", 10)).grid(row=1, column=1, sticky="w")
        self.furniture_var = tk.StringVar()
        self.furniture_dropdown = ttk.Combobox(card, textvariable=self.furniture_var,
                                                width=25, state="readonly")
        self.furniture_dropdown.grid(row=2, column=1, padx=8, pady=5)

        ttk.Button(card, text="🔄 Refresh Lists", command=self.refresh_dropdowns).grid(
            row=2, column=2, padx=8)

        ttk.Button(card, text="✅ Book Sale", style="Accent.TButton",
                   command=self.book_sale).grid(row=3, column=0, pady=(10, 0), sticky="w")

    def _build_table(self):
        card = tk.Frame(self, bg=CARD_BG)
        card.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        search_frame = tk.Frame(card, bg=CARD_BG, pady=8, padx=10)
        search_frame.pack(fill="x")
        tk.Label(search_frame, text="🔍 Search by Customer CNIC:", bg=CARD_BG, fg=SUBTEXT,
                 font=("Segoe UI", 10)).pack(side="left")
        self.search_entry = tk.Entry(search_frame, width=15, bg=ENTRY_BG, fg=TEXT,
                                      insertbackground=TEXT, relief="flat")
        self.search_entry.pack(side="left", padx=8, ipady=3)
        ttk.Button(search_frame, text="Search", command=self.search_sale).pack(side="left", padx=4)
        ttk.Button(search_frame, text="Show All", command=self.refresh_table).pack(side="left")

        columns = ("Cust CNIC", "Cust Name", "Phone", "Age", "Furn ID", "Type", "Material", "Price")
        self.tree = ttk.Treeview(card, columns=columns, show="headings", height=12)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=90)
        self.tree.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    def refresh_dropdowns(self):
        cust_values = []
        for i in range(0, len(module2.customer), 4):
            cust_values.append(f"{module2.customer[i]} - {module2.customer[i+1]}")
        self.customer_dropdown["values"] = cust_values

        furn_values = []
        for i in range(0, len(module1.furniture), 4):
            furn_values.append(f"{module1.furniture[i]} - {module1.furniture[i+1]}")
        self.furniture_dropdown["values"] = furn_values

    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        for i in range(0, len(sales_module.sales), 8):
            self.tree.insert("", "end", values=tuple(sales_module.sales[i:i+8]))

    def search_sale(self):
        query = self.search_entry.get().strip()
        if not query:
            self.refresh_table()
            return
        try:
            query_id = int(query)
        except ValueError:
            messagebox.showerror("Invalid input", "CNIC must be a number.")
            return

        self.tree.delete(*self.tree.get_children())
        found = False
        for i in range(0, len(sales_module.sales), 8):
            if sales_module.sales[i] == query_id:
                self.tree.insert("", "end", values=tuple(sales_module.sales[i:i+8]))
                found = True
        if not found:
            messagebox.showinfo("Not found", f"No sales found for CNIC {query_id}")

    def book_sale(self):
        cust_choice = self.customer_var.get()
        furn_choice = self.furniture_var.get()

        if not cust_choice or not furn_choice:
            messagebox.showerror("Missing selection", "Please select both a customer and a furniture item.")
            return

        cnic = int(cust_choice.split(" - ")[0])
        fid = int(furn_choice.split(" - ")[0])

        if cnic not in module2.customer or fid not in module1.furniture:
            messagebox.showerror("Error", "Selected customer or furniture no longer exists.")
            self.refresh_dropdowns()
            return

        for i in range(0, len(module2.customer), 4):
            if module2.customer[i] == cnic:
                sales_module.sales.extend(module2.customer[i:i+4])
                break

        for i in range(0, len(module1.furniture), 4):
            if module1.furniture[i] == fid:
                sales_module.sales.extend(module1.furniture[i:i+4])
                break

        messagebox.showinfo("Success", "Sale booked successfully!")
        self.refresh_table()


if __name__ == "__main__":
    app = FurnitureStoreApp()
    app.mainloop()
