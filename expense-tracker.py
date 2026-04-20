import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import os

# ---------------- ROOT ----------------
root = tk.Tk()
root.title("Login System 🔐")
root.geometry("350x400")

# ---------------- FILE FUNCTIONS ----------------
def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(username.strip() + "," + password.strip() + "\n")

def check_user(username, password):
    if not os.path.exists("users.txt"):
        return False

    with open("users.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if username.strip() == u and password.strip() == p:
                return True
    return False

# ---------------- LOGIN ----------------
def login():
    username = entry_user.get().strip()
    password = entry_pass.get().strip()

    if username == "Username" or password == "Password":
        messagebox.showerror("Error", "Enter valid details")
        return

    if check_user(username, password):
        messagebox.showinfo("Success", "Login Successful!")
        open_tracker()
    else:
        messagebox.showerror("Error", "Invalid credentials")

# ---------------- SIGNUP ----------------
def signup():
    username = entry_user.get().strip()
    password = entry_pass.get().strip()

    if username == "Username" or password == "Password":
        messagebox.showerror("Error", "Enter valid details")
        return

    if len(password) < 6 or not password.isdigit():
        messagebox.showerror("Error", "Password must be at least 6 digits")
        return

    save_user(username, password)
    messagebox.showinfo("Success", "Account Created!")

# ---------------- TRACKER ----------------
expenses = []

def add_expense():
    amount = entry_amount.get()
    category = combo_category.get()

    if not amount.isdigit():
        return

    expense = f"{category} - ₹{amount}"
    expenses.append(expense)
    listbox.insert(tk.END, expense)

    update_total()
    entry_amount.delete(0, tk.END)

def update_total():
    total = sum(int(item.split("₹")[1]) for item in expenses)
    label_total.config(text=f"Total: ₹{total}")

def show_graph():
    if not expenses:
        messagebox.showinfo("Info", "No data to show")
        return

    category_totals = {}

    for item in expenses:
        category, amount = item.split(" - ₹")
        amount = int(amount)
        category_totals[category] = category_totals.get(category, 0) + amount

    labels = list(category_totals.keys())
    values = list(category_totals.values())

    plt.figure()
    plt.bar(labels, values)
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.tight_layout()
    plt.show(block=True)

# ---------------- OPEN TRACKER ----------------
def open_tracker():
    tracker = tk.Toplevel(root)
    tracker.title("Expense Tracker 💸")
    tracker.geometry("400x500")

    global entry_amount, combo_category, listbox, label_total

    tk.Label(tracker, text="Expense Tracker 💸", font=("Arial", 16, "bold")).pack(pady=10)

    entry_amount = tk.Entry(tracker)
    entry_amount.pack(pady=5)

    combo_category = ttk.Combobox(tracker, values=["Food", "Travel", "Fun", "Other"])
    combo_category.set("Food")
    combo_category.pack(pady=5)

    tk.Button(tracker, text="Add Expense", command=add_expense).pack(pady=10)

    listbox = tk.Listbox(tracker)
    listbox.pack(pady=10, fill="both", expand=True)

    label_total = tk.Label(tracker, text="Total: ₹0", font=("Arial", 12, "bold"))
    label_total.pack(pady=10)

    tk.Button(tracker, text="Show Graph 📊", command=show_graph).pack(pady=10)

# ---------------- PLACEHOLDER LOGIC ----------------

# USERNAME
entry_user = tk.Entry(root, fg="gray")
entry_user.pack(pady=10)
entry_user.insert(0, "Username")

def clear_user(event):
    if entry_user.get() == "Username":
        entry_user.delete(0, tk.END)
        entry_user.config(fg="black")

def restore_user(event):
    if entry_user.get() == "":
        entry_user.insert(0, "Username")
        entry_user.config(fg="gray")

entry_user.bind("<FocusIn>", clear_user)
entry_user.bind("<FocusOut>", restore_user)

# PASSWORD
entry_pass = tk.Entry(root, fg="gray")
entry_pass.pack(pady=10)
entry_pass.insert(0, "Password")

def clear_pass(event):
    if entry_pass.get() == "Password":
        entry_pass.delete(0, tk.END)
        entry_pass.config(fg="black", show="*")

def restore_pass(event):
    if entry_pass.get() == "":
        entry_pass.config(show="")
        entry_pass.insert(0, "Password")
        entry_pass.config(fg="gray")

entry_pass.bind("<FocusIn>", clear_pass)
entry_pass.bind("<FocusOut>", restore_pass)

# ---------------- BUTTONS ----------------
tk.Button(root, text="Login", width=15, command=login).pack(pady=10)
tk.Button(root, text="Signup", width=15, command=signup).pack(pady=5)

# ---------------- RUN ----------------
root.mainloop()