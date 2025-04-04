from tkinter import *
from tkinter import messagebox
font_style = ("Arial", 24)
font_style2 = ("Arial", 20)
font_style3 = ("Arial", 12)
def go_to_home():
    aboutroot.destroy()
    with open('home.py', 'r') as file:
        code = file.read()
    exec(code)
    from home import homeroot
    homeroot.mainloop()
def go_to_admin_login():
    aboutroot.destroy()
    from adminlogin import adminroot
    adminroot.mainloop()
    
aboutroot =Tk()
aboutroot.configure(bg="#374375")
aboutroot.title("About")

made=Label(aboutroot,text='Made by:Nirja Raut',bg="#374375",fg="#FFFCF5",font=font_style2)
made.grid(row=0,column=0,padx=20,pady=0,sticky=W)



other=Label(aboutroot,text='A041 CSE 4 A',bg="#374375",fg="#FFFCF5",font=font_style2)
other.grid(row=1,column=0,padx=20,pady=20,sticky=W)
# Contact Details
contact_label = Label(aboutroot,bg="#374375",fg="#FFFCF5",font=font_style2, text="Contact Details:")
contact_label.grid(row=2,column=0,padx=20,pady=20,sticky=W)

phone_label = Label(aboutroot,bg="#374375",fg="#FFFCF5",font=font_style2, text="Phone: +1234567890")
phone_label.grid(row=3,column=0,padx=20,pady=20,sticky=W)

email_label = Label(aboutroot,bg="#374375",fg="#FFFCF5",font=font_style2, text="Email: yourrecipe@gmail.com")
email_label.grid(row=3,column=1,padx=20,pady=20,sticky=W)

# Buttons
home_button = Button(aboutroot,bg="#374375",bd=0,fg="#FFFCF5",font=font_style2, text="Home", command=go_to_home)
home_button.grid(row=4,column=0,padx=20,sticky=W)

admin_button = Button(aboutroot,bg="#374375",bd=0,fg="#FFFCF5", font=font_style2,text="Admin Login", command=go_to_admin_login)
admin_button.grid(row=5,column=0,padx=20,pady=20,sticky=W)
aboutroot.mainloop()

