from tkinter import *
def click():
    print("i clicked the button")
window = Tk()

# label=Label(window,
#             text="shailu",
#             font=('Arial',40,'bold'),
#             fg="#0A0A76",
#             bg='black',
#             relief=RAISED,
#             bd=10,
#             padx=60,
#             pady=30
        
#             )
# label.pack()

button=Button(window,
              text="click me",
              command=click,
              font=("Arial",30),
              fg="white",
              bg="black")
button.pack()
window.mainloop()