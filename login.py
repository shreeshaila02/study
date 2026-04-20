
import tkinter as tk
from tkinter import messagebox

# ---------- LOGIN PAGE ----------
root = tk.Tk()
root.title("Login Page")
root.geometry("300x250")

def login():
    if entry_user.get() == "shailu" and entry_pass.get() == "9636":
        messagebox.showinfo("Success", "Login Successful")
        root.destroy()
        open_sports_page()
    else:
        messagebox.showerror("Error", "Login Failed")

tk.Label(root, text="Username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=20)

# ---------- SPORTS PAGE ----------
def open_sports_page():
    sports_win = tk.Tk()
    sports_win.title("Select Sport")
    sports_win.geometry("300x250")

    tk.Label(sports_win, text="Select One Sport").pack(pady=10)

    sport_var = tk.StringVar()
    sports = ["Cricket", "Football", "Kabaddi"]

    for s in sports:
        tk.Radiobutton(sports_win, text=s, variable=sport_var, value=s).pack()

    def next_page():
        selected_sport = sport_var.get()
        print("Sport:", selected_sport)
        sports_win.destroy()
        open_food_page(selected_sport)

    tk.Button(sports_win, text="Next", command=next_page).pack(pady=20)

    sports_win.mainloop()

# ---------- FOOD PAGE ----------
def open_food_page(sport):
    food_win = tk.Tk()
    food_win.title("Select Food")
    food_win.geometry("300x250")

    tk.Label(food_win, text=f"Selected Sport: {sport}").pack(pady=5)
    tk.Label(food_win, text="Select One Food").pack(pady=10)

    food_var = tk.StringVar()
    foods = ["Dosa", "Biryani", "Pizza"]

    for f in foods:
        tk.Radiobutton(food_win, text=f, variable=food_var, value=f).pack()

    def submit():
        selected_food = food_var.get()
        print("Food:", selected_food)
        messagebox.showinfo("Done", f"Sport: {sport}\nFood: {selected_food}")

    tk.Button(food_win, text="Submit", command=submit).pack(pady=20)

    food_win.mainloop()

# ---------- RUN ----------
root.mainloop()