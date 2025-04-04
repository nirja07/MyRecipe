from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def browse_image():
    filename = filedialog.askopenfilename()
    image_path.set(filename)

def submit_form():
    name = name_entry.get().lower()
    author = author_entry.get().lower()
    ingredients = ingredients_text.get("1.0", END)
    instructions = instructions_text.get("1.0", END)
    image = image_path.get()
    if name!=''and author!=''and ingredients!=''and image!='':
    # Connect to MySQL database
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="miniprojectprp"
        )
        cursor = conn.cursor()

    # Read image binary data
        with open(image, 'rb') as file:
            image_data = file.read()
        select_query="SELECT * from recipe where name=%s"
        cursor.execute(select_query,(name,))
        existing_recipe=cursor.fetchone()
        if (existing_recipe):
            messagebox.showerror("Error", "recipe already exists")
            conn.commit()
            conn.close()
            return

    # Insert data into the database
        insert_query = "INSERT INTO recipe (name, author, ingredients, instructions, imager) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (name, author, ingredients, instructions, image_data))

    # Commit changes and close connection
        conn.commit()
        conn.close()
        addreciperoot.destroy()
        from adminhome import adminhomeroot
        adminhomeroot.mainloop()
        messagebox.askokcancel("Successful","Recipe submitted successfully!")

addreciperoot = Tk()
addreciperoot.title("Recipe Form")
addreciperoot.configure(bg='#FFFCF5')
font_style = ("Arial", 24)
font_style2 = ("Arial", 20)
font_style3 = ("Arial", 12)
addreciperoot.geometry("1080x800")

# Labels
Label(addreciperoot, text="Name:",font=font_style,bg='#FFFCF5',fg='#374375').grid(row=0, column=0, sticky="w",padx=20,pady=20)
Label(addreciperoot, text="Author:",font=font_style,bg='#FFFCF5',fg='#374375').grid(row=1, column=0, sticky="w",padx=20,pady=20)
Label(addreciperoot, text="Ingredients:",font=font_style,bg='#FFFCF5',fg='#374375').grid(row=2, column=0, sticky="w",padx=20,pady=20)
Label(addreciperoot, text="Instructions:",font=font_style,bg='#FFFCF5',fg='#374375').grid(row=3, column=0, sticky="w",padx=20,pady=20)
Label(addreciperoot, text="Image Path:",font=font_style,bg='#FFFCF5',fg='#374375').grid(row=4, column=0, sticky="w",padx=20,pady=20)

# Entry fields
name_entry = Entry(addreciperoot,font=font_style2,bg='#FFFCF5',fg='#374375',width=50)
name_entry.grid(row=0, column=1,sticky='E')

author_entry = Entry(addreciperoot,font=font_style2,bg='#FFFCF5',fg='#374375',width=50)
author_entry.grid(row=1, column=1,sticky='E')

ingredients_text = Text(addreciperoot, height=6, width=50,font=font_style2,bg='#FFFCF5',fg='#374375')
ingredients_text.grid(row=2, column=1, padx=5, pady=5)

instructions_text = Text(addreciperoot, height=6, width=50,font=font_style2,bg='#FFFCF5',fg='#374375')
instructions_text.grid(row=3, column=1, padx=5, pady=5)

# Button to browse image
image_path = StringVar()
Entry(addreciperoot, textvariable=image_path, state="readonly",font=font_style2,bg='#FFFCF5',fg='#374375', width=30).grid(row=4, column=1, padx=20, pady=5)
Button(addreciperoot, text="Browse", command=browse_image,font=font_style,bd=0,bg='#895159',fg='#FFFCF5').grid(row=4, column=1, padx=5, pady=5,sticky='E')

# Submit button
Button(addreciperoot, text="Submit", command=submit_form,font=font_style,bd=0,bg='#895159',fg='#FFFCF5').grid(row=5, column=0,sticky='W',padx=20, pady=10)

addreciperoot.mainloop()
