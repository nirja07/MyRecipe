from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
import io
def display_recipes():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="miniprojectprp"
        )
    cursor = conn.cursor()

    # Clear previous content if any
    

    # Fetch data from the database
    cursor.execute("SELECT * FROM recipe")
    recipes = cursor.fetchall()

    idl=Label(adminhomeroot,text="Id",font=font_style2,bg='#FFFCF5').grid(row=1,column=0,padx=20,pady=20)
    namel=Label(adminhomeroot,text="Recipe Name",font=font_style2,bg='#FFFCF5').grid(row=1,column=1,padx=20,pady=20)
    authorl=Label(adminhomeroot,text="Author",font=font_style2,bg='#FFFCF5').grid(row=1,column=2,padx=20,pady=20)
    button1l=Label(adminhomeroot,text="Edit",font=font_style2,bg='#FFFCF5').grid(row=1,column=3,padx=20,pady=20)
    button2l=Label(adminhomeroot,text="Delete",font=font_style2,bg='#FFFCF5').grid(row=1,column=4,padx=20,pady=20)

    i=2
    for recipe in recipes:
        id_label=Label(adminhomeroot,text=recipe[0],font=font_style3,bg='#FFFCF5')
        id_label.grid(row=i,column=0,padx=20,pady=20)
        recipe_name_label = Label(adminhomeroot, text=recipe[1].title(), font=font_style3,bg='#FFFCF5')
        recipe_name_label.grid(row=i,column=1,padx=20,pady=20)
        author_label = Label(adminhomeroot, text=recipe[4].title(), font=font_style3,bg='#FFFCF5')
        author_label.grid(row=i,column=2,padx=20,pady=20)
        button1=Button(adminhomeroot,text='Edit',font=font_style,bd=0,bg='#895159',fg='#FFFCF5',command=lambda r=recipe: edit_recipe(r[0])).grid(row=i, column=3,padx=20, pady=10)
        button2=Button(adminhomeroot,text='Delete',font=font_style,bd=0,bg='#895159',fg='#FFFCF5',command=lambda r=recipe: delete_recipe(r[0])).grid(row=i, column=4,padx=20, pady=10)
        
        i=i+1

# Call this function to display recipes on page load

    conn.commit()
    conn.close()

    adminhomeroot.mainloop()
def edit_recipe(r):
    # Implement the functionality for editing a recipe
    # You can use the recipe_id parameter to identify which recipe to edit
    adminhomeroot.destroy()
    global recipe_id
    recipe_id=r
    from editrecipe import editreciperoot
    editreciperoot.mainloop()

def delete_recipe(recipe_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="miniprojectprp"
        )
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM recipe WHERE recipeid='%s'",(recipe_id,))
        conn.commit()
        messagebox.askokcancel("Successful","Deletion is successful")

       
    except Exception as e:
        messagebox.askokcancel("Error","unable to delete recipe.")
        print(e)
    finally:
          # Close the current instance of adminhomeroot
        adminhomeroot.mainloop()
    
def open_addpage():
    adminhomeroot.destroy()
    from addrecipe import addreciperoot
    addreciperoot.mainloop()
adminhomeroot=Tk()
adminhomeroot.title('Admin Home')
adminhomeroot.geometry('784x750')
navbar_frame = Frame(adminhomeroot,bg='#374375')
navbar_frame.grid(columnspan=5,sticky=EW,ipadx=20)
adminhomeroot.configure(bg='#FFFCF5')
font_style = ("Arial", 24)
font_style2 = ("Arial", 20)
font_style3 = ("Arial", 18)
add_button = Button(navbar_frame,font=font_style, text="Add recipe",bd=0, command=open_addpage,bg='#374375',fg='#FFFCF5')
add_button.pack(side=LEFT, padx=10, pady=5)
display_recipes()
