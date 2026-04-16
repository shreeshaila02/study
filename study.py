
import tkinter as tk

# ---------- WINDOW ----------
root = tk.Tk()
root.title("Study Planner")
root.geometry("400x500")
root.configure(bg="#f5f7fa")

# ---------- BACKEND ----------
tasks = []

def add_task():
    task = entry.get()
    if task.strip() != "":
        tasks.append(task)
        update_list()
        entry.delete(0, tk.END)

def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_list()

# ---------- UI ----------
# Title
title = tk.Label(root, text="📚 Study Planner", font=("Arial", 18, "bold"), bg="#f5f7fa")
title = tk.Label(root, text="📚 Study wellr", font=("Arial", 18), bg="#f5f7fa")
title.pack(pady=10)

# Entry
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=20, fill="x")

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f5f7fa")
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add", command=add_task, bg="#4CAF50", fg="white", width=10)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete", command=delete_task, bg="#f44336", fg="white", width=10)
delete_btn.grid(row=0, column=1, padx=5)

# Task List
listbox = tk.Listbox(root, font=("Arial", 12))
listbox.pack(pady=15, padx=20, fill="both", expand=True)

# Footer
footer = tk.Label(root, text="Stay Consistent 💪", bg="#f5f7fa", fg="gray")
footer.pack(pady=10)

# ---------- RUN ----------
root.mainloop()