from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import re
def submitfun():
    u=username.get()
    p=password.get()
    cp=confirmpassword.get()
    logintodb(u,p,cp)
def logintodb(u,p,cp):
    checking=re.fullmatch(r'\w[A-Za-z]*@\w+\.\w+',u)
    if not u or not p or not cp :
        messagebox.showerror("Error", "Please fill in all fields")
        return
    elif checking==None:
        messagebox.showerror("Error", "username should be gmail")
        return
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="miniprojectprp"
        )
        cursor = mydb.cursor()

   
        cursor.execute("SELECT * FROM admin WHERE useradmin = %s ", (u,))
        existing_user = cursor.fetchone()
        if existing_user:
            messagebox.showerror("Error", "Username or email already exists")
            return

        if(cp==p):
            cursor.execute("INSERT INTO admin (useradmin,passadmin) VALUES (%s, %s)", (u,p))
            mydb.commit()
            messagebox.showinfo("Success", "Registration successful")
            adminsignuproot.destroy()
            from adminhome import adminhomeroot
            adminhomeroot.mainloop()
    except Exception as e:
        messagebox.showerror("Error", e)  
    finally:
        cursor.close()
        mydb.close()
adminsignuproot=Tk()
adminsignuproot.configure(bg='#FFFCF5')
font_style = ("Arial", 24)
font_style2 = ("Arial", 20)
font_style3 = ("Arial", 12)
adminsignuproot.geometry("680x400")
adminsignuproot.title('Signup')
l1=Label(adminsignuproot,text='Username:',font=font_style,bg='#FFFCF5',fg='#374375')
l2=Label(adminsignuproot,text='Password:',font=font_style,bg='#FFFCF5',fg='#374375')
l3=Label(adminsignuproot,text='Confirm Password:',font=font_style,bg='#FFFCF5',fg='#374375')
username=Entry(adminsignuproot,font=font_style2,bg='#FFFCF5',fg='#374375')
password=Entry(adminsignuproot,font=font_style2,bg='#FFFCF5',fg='#374375')
confirmpassword=Entry(adminsignuproot,font=font_style2,bg='#FFFCF5',fg='#374375')
l1.grid(row=0, column=0, padx=20, pady=20,sticky=W)
username.grid(row=0, column=1, padx=20, pady=20)
l2.grid(row=1, column=0, padx=20, pady=20,sticky=W)
password.grid(row=1, column=1, padx=20, pady=20)
l3.grid(row=2, column=0, padx=20, pady=20,sticky=W)
confirmpassword.grid(row=2, column=1, padx=20, pady=20)
b1=Button(adminsignuproot,text="Sign up",command=submitfun,font=font_style,bd=0,bg='#895159',fg='#FFFCF5')
b1.grid(row=3, column=1,padx=20, pady=20,sticky=E)

adminsignuproot.mainloop()