
import tkinter as tk

root = tk.Tk()
root.title("StudyGenie")
root.geometry("400x600")
root.configure(bg="#f5f7fa")

tasks = []

# 🎨 Subject Colors
color_map = {
    "Math": "#4A90E2",
    "Science": "#50E3C2",
    "English": "#FFD93D"
}

# ---------- FUNCTIONS ----------

def clear_main():
    for widget in main.winfo_children():
        widget.destroy()


def toggle_complete(index):
    tasks[index]["done"] = not tasks[index]["done"]
    refresh_tasks()


def delete_task(index):
    tasks.pop(index)
    refresh_tasks()


def create_card(task, index):
    color = color_map.get(task["subject"], "#FF6B6B")

    card = tk.Frame(main, bg="white", width=340, height=90, bd=1, relief="solid")
    card.pack(pady=10)

    text = f"{task['subject']} - {task['topic']}"
    label = tk.Label(card, text=text, bg="white",
                     font=("Arial", 12, "bold"))
    label.place(x=10, y=15)

    # Status
    status_text = "Done ✔" if task["done"] else "Pending"
    status_color = "#2ECC71" if task["done"] else color

    status = tk.Label(card, text=status_text, bg=status_color,
                      fg="white", font=("Arial", 9))
    status.place(x=250, y=15)

    # ✔ Complete Button
    complete_btn = tk.Button(card, text="✔", bg="#2ECC71", fg="white",
                            command=lambda: toggle_complete(index))
    complete_btn.place(x=200, y=50)

    # 🗑 Delete Button
    delete_btn = tk.Button(card, text="🗑", bg="#E74C3C", fg="white",
                          command=lambda: delete_task(index))
    delete_btn.place(x=260, y=50)


def refresh_tasks():
    clear_main()
    if not tasks:
        tk.Label(main, text="No tasks yet", bg="#f5f7fa",
                 font=("Arial", 12)).pack()
    else:
        for i, task in enumerate(tasks):
            create_card(task, i)


def add_task():
    win = tk.Toplevel(root)
    win.title("Add Task")
    win.geometry("300x300")

    tk.Label(win, text="Subject").pack(pady=5)
    subject_entry = tk.Entry(win)
    subject_entry.pack(pady=5)

    tk.Label(win, text="Topic").pack(pady=5)
    topic_entry = tk.Entry(win)
    topic_entry.pack(pady=5)

    def save():
        subject = subject_entry.get()
        topic = topic_entry.get()

        if subject and topic:
            tasks.append({
                "subject": subject,
                "topic": topic,
                "done": False
            })
            refresh_tasks()
            win.destroy()

    tk.Button(win, text="Save", command=save, bg="#4A90E2",
              fg="white").pack(pady=20)


# ---------- HEADER ----------
header = tk.Frame(root, bg="#4A90E2", height=80)
header.pack(fill="x")

tk.Label(header, text="StudyGenie", fg="white", bg="#4A90E2",
         font=("Arial", 18, "bold")).pack(pady=20)

# ---------- MAIN ----------
main = tk.Frame(root, bg="#f5f7fa")
main.pack(pady=10)

# ---------- ADD BUTTON ----------
btn = tk.Button(root, text="➕ Add Task", command=add_task,
                bg="#4A90E2", fg="white", width=20, height=2)
btn.pack(pady=20)

refresh_tasks()

root.mainloop()