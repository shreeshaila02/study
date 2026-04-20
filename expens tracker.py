import tkinter as tk
from tkinter import ttk

expenses = []

def add_expense():
    amount = entry_amount.get()
    category = combo_category.get()

    if amount == "" or not amount.isdigit():
        return

    expense = f"{category} - ₹{amount}"
    expenses.append(expense)

    listbox.insert(tk.END, expense)
    update_total()

    entry_amount.delete(0, tk.END)

def update_total():
    total = sum(int(item.split("₹")[1]) for item in expenses)

    if total > 500:
        label_total.config(text=f"Total: ₹{total} ⚠️", fg="red")
    else:
        label_total.config(text=f"Total: ₹{total}", fg="white")


root = tk.Tk()
root.title("Expense Tracker")
root.geometry("350x500")
root.configure(bg="#1e1e2f")

# Title
tk.Label(root, text="Expense Tracker ",
         font=("Helvetica", 16, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=15)

# Card Frame
frame = tk.Frame(root, bg="#2c2c3e", bd=0)
frame.pack(pady=10, padx=10, fill="both")

entry_amount = tk.Entry(frame, font=("Arial", 12),
                        bg="#3a3a4f", fg="gray", bd=0, justify="center")
entry_amount.pack(pady=10, padx=20, fill="x")

# Default placeholder
entry_amount.insert(0, "Enter Amount")

def on_focus_in(event):
    if entry_amount.get() == "Enter Amount":
        entry_amount.delete(0, tk.END)
        entry_amount.config(fg="white")

def on_focus_out(event):
    if entry_amount.get() == "":
        entry_amount.insert(0, "Enter Amount")
        entry_amount.config(fg="gray")

# Bind events
entry_amount.bind("<FocusIn>", on_focus_in)
entry_amount.bind("<FocusOut>", on_focus_out)


combo_category = ttk.Combobox(frame,background="blue", values=["Food", "Travel", "Fun","shopping","Other"])
combo_category.pack(pady=10, padx=20, fill="x")
combo_category.set("Food")


tk.Button(frame, text="Add Expense",
          bg="#4CAF50", fg="white",
          font=("Arial", 11, "bold"),
          command=add_expense).pack(pady=15)

# Listbox (Expenses)
listbox = tk.Listbox(root,
                     bg="#2c2c3e",
                     fg="white",
                     font=("Arial", 11),
                     bd=0)
listbox.pack(pady=10, padx=15, fill="both", expand=True)
def add_expense():
    amount = entry_amount.get()
    category = combo_category.get()

    if amount == "" or amount == "Enter Amount" or not amount.isdigit():
        return

    expense = f"{category} - ₹{amount}"
    expenses.append(expense)

    listbox.insert(tk.END, expense)
    update_total()

    entry_amount.delete(0, tk.END)

# Total Label
label_total = tk.Label(root,
                       text="Total: ₹0",
                       font=("Arial", 13, "bold"),
                       bg="#1e1e2f",
                       fg="white")
label_total.pack(pady=10)

root.mainloop()