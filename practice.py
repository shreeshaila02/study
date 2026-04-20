# double=[]
# for x in range (1, 20):
#     double.append(x*2)

# print(double)



# i=1
# while i<=10:
#     print("i love coding")
#     i+=1



# doubles = [x*2 for x in range(1,11)]
# doubles = [x*x for x in range(1,11)]
# print (doubles)


# numbers=[1,-2,3,-4,5,-6,8,-7,9]
# positive_nums=[num for num in numbers if num>=0]
# negetive_nums=[num for num in numbers if num<0]
# even_nums=[num for num in numbers if num %2==0]
# print(even_nums)


import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title ("login page")
root.geometry("300x250")

def login():
    username = entry_user.get()
    password = entry_pass.get()
    if username == "shailu" and password == "9636":
        messagebox.showinfo("login succesfull","welcome")
    else:
        messagebox.showerror("login failed","error")
tk.Label(root,text="username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack(pady=5)

tk.Label(root,text="password").pack(pady=5)
entry_pass = tk.Entry(root)
entry_pass.pack(pady=5)
tk.Button(root,text="login",command=login).pack(pady=20)
root.mainloop()
