import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("Login System")
app.geometry("300x300")

# Save user data to file
def register():
    username = entry_user.get()
    password = entry_pass.get()
    
    if username == "" or password == "":
        messagebox.showwarning("Error", "Please enter all fields")
        return
    
    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")
    
    messagebox.showinfo("Success", "Account Created ✅")

# Login check
def login():
    username = entry_user.get()
    password = entry_pass.get()
    
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
            
            for user in users:
                u, p = user.strip().split(",")
                if username == u and password == p:
                    messagebox.showinfo("Login", "Login Successful ✅")
                    return
            
        messagebox.showerror("Login", "Invalid Username or Password ❌")
    
    except FileNotFoundError:
        messagebox.showerror("Error", "No users registered yet")

# UI
tk.Label(app, text="Login System", font=("Arial", 16)).pack(pady=10)

tk.Label(app, text="Username").pack()
entry_user = tk.Entry(app)
entry_user.pack()

tk.Label(app, text="Password").pack()
entry_pass = tk.Entry(app, show="*")
entry_pass.pack()

tk.Button(app, text="Register", command=register).pack(pady=5)
tk.Button(app, text="Login", command=login).pack(pady=5)

app.mainloop()