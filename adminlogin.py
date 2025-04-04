from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
def submitfun():
    u=username.get()
    p=password.get()
    logintodb(u,p)
def logintodb(u,p):
    conn=mysql.connector.connect(host="localhost",user="root",database="miniprojectprp")
    cursor=conn.cursor()
    query="select * from admin  where useradmin=%s and passadmin=%s"
    try:
        cursor.execute(query,(u,p))
        myresult=cursor.fetchall()
        if myresult:
            messagebox.askokcancel("Admin Login","Successful Login")
            username.delete(0,END)
            password.delete(0,END)
            adminroot.destroy()
            from adminhome import adminhomeroot
            adminhomeroot.mainloop()
        else:
            messagebox.askokcancel("Login","Login Unsuccessful")
    except:
        print("Connection failed")
    

        if conn:
            cursor.close()
            conn.close()
def signfun():
    adminroot.destroy()
    from adminsignup import adminsignuproot
    adminsignuproot.mainloop()

adminroot=Tk()
adminroot.configure(bg='#FFFCF5')
font_style = ("Arial", 24)
font_style2 = ("Arial", 20)
font_style3 = ("Arial", 12)
adminroot.geometry("580x300")
adminroot.title('Admin Login')
l1=Label(adminroot,text='Username:',font=font_style,bg='#FFFCF5',fg='#374375')
l2=Label(adminroot,text='Password:',font=font_style,bg='#FFFCF5',fg='#374375')
username=Entry(adminroot,font=font_style2,bg='#FFFCF5',fg='#374375')
password=Entry(adminroot,font=font_style2,bg='#FFFCF5',fg='#374375')
l1.grid(row=0, column=0, padx=20, pady=20)
username.grid(row=0, column=1, padx=20, pady=20)
l2.grid(row=1, column=0, padx=20, pady=20)
password.grid(row=1, column=1, padx=20, pady=20)
b1=Button(adminroot,text="Login",command=submitfun,font=font_style,bd=0,bg='#895159',fg='#FFFCF5')
b1.grid(row=2, column=1,padx=20, pady=20,sticky=E,rowspan=2)
b2=Button(adminroot,text="new here? Sign up",command=signfun,font=font_style3,bg='#FFFCF5',fg='#5f6ca3',bd=0)
b2.grid(row=2, column=0,padx=20, pady=1,sticky=SW)

adminroot.mainloop()