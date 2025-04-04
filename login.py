from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


def signfun():
    root.destroy()
    from signup import root1
    
    
    root1.mainloop()  # Ensure the signup window remains open
def adminsignfun():
    root.destroy()
    from adminlogin import adminroot
    
    adminroot.mainloop()
def submitfun():
    u=username.get()
    p=password.get()
    logintodb(u,p)
def logintodb(u,p):
    conn=mysql.connector.connect(host="localhost",user="root",database="miniprojectprp")
    cursor=conn.cursor()
    query="select * from login where userid=%s and pass=%s"
    try:
        cursor.execute(query,(u,p))
        myresult=cursor.fetchall()
        if myresult:
            messagebox.askokcancel("Login","Successful Login")
            username.delete(0,END)
            password.delete(0,END)
            root.destroy()
            from home import create_homepage
            create_homepage()
        else:
            messagebox.askokcancel("Login","Login Unsuccessful")
    except Exception as e:
        print("Connection failed",e)
    finally:
        
        if conn:
            cursor.close()
            conn.close()
root=Tk()

font_style = ("Arial", 24)
font_style2 = ("Arial", 20)
font_style3 = ("Arial", 12)
root.geometry("580x300")
root.title('Login')
root.configure(bg="#FFFCF5")
l1=Label(root,text='Username:',font=font_style,bg='#FFFCF5',fg='#374375')
l2=Label(root,text='Password:',font=font_style,bg='#FFFCF5',fg='#374375')
username=Entry(root,font=font_style2,bg='#FFFCF5',fg='#374375')
password=Entry(root,font=font_style2,bg='#FFFCF5',fg='#374375')
l1.grid(row=0, column=0, padx=20, pady=20)
username.grid(row=0, column=1, padx=20, pady=20)
l2.grid(row=1, column=0, padx=20, pady=20)
password.grid(row=1, column=1, padx=20, pady=20)
b1=Button(root,text="Login",command=submitfun,font=font_style,bd=0,bg='#895159',fg='#FFFCF5')
b1.grid(row=2, column=1,padx=20, pady=20,sticky=E,rowspan=2)
b2=Button(root,text="new here? Sign up",command=signfun,font=font_style3,bg='#FFFCF5',fg='#5f6ca3',bd=0)
b2.grid(row=2, column=0,padx=20, pady=1,sticky=SW)
b3=Button(root,text="Log in as admin",fg='#5f6ca3',command=adminsignfun,font=font_style3,bg='#FFFCF5',bd=0)
b3.grid(row=3, column=0,padx=20, pady=0,sticky=NW)
root.mainloop()