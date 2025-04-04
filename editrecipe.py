from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import mysql.connector
from adminhome import recipe_id as r
recipe_id=int(r)

    
def browse_image():
    filename = filedialog.askopenfilename()
    image_path.set(filename)

def submit_form():
    name = name_entry.get().lower()
    author = author_entry.get().lower()
    ingredients = ingredients_text.get("1.0", END)
    instructions = instructions_text.get("1.0", END)
    image = image_path.get()

    if name and author and ingredients and image:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="miniprojectprp"
            )
            cursor = conn.cursor()

            with open(image, 'rb') as file:
                image_data = file.read()

            update_query = "UPDATE recipe SET name=%s, author=%s, ingredients=%s, instructions=%s, imager=%s WHERE recipeid=%s"
            cursor.execute(update_query, (name, author, ingredients, instructions, image_data, recipe_id))

            conn.commit()
            conn.close()
            messagebox.askokcancel("Successful", "Recipe updated successfully!")
            editreciperoot.destroy()
            from adminhome import adminhomeroot
            adminhomeroot.mainloop()

            

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showerror("Error", "All fields are required")

# Fetch data for editing
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="miniprojectprp"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM recipe WHERE recipeid=%s", (recipe_id,))
result = cursor.fetchone()
conn.close()

editreciperoot = Tk()
editreciperoot.title("Recipe Form")
editreciperoot.configure(bg='#FFFCF5')
font_style = ("Arial", 24)
font_style2 = ("Arial", 20)
editreciperoot.geometry("1080x800")

# Labels
Label(editreciperoot, text="Name:", font=font_style, bg='#FFFCF5', fg='#374375').grid(row=0, column=0, sticky="w", padx=20, pady=20)
Label(editreciperoot, text="Author:", font=font_style, bg='#FFFCF5', fg='#374375').grid(row=1, column=0, sticky="w", padx=20, pady=20)
Label(editreciperoot, text="Ingredients:", font=font_style, bg='#FFFCF5', fg='#374375').grid(row=2, column=0, sticky="w", padx=20, pady=20)
Label(editreciperoot, text="Instructions:", font=font_style, bg='#FFFCF5', fg='#374375').grid(row=3, column=0, sticky="w", padx=20, pady=20)
Label(editreciperoot, text="Image Path:", font=font_style, bg='#FFFCF5', fg='#374375').grid(row=4, column=0, sticky="w", padx=20, pady=20)

# Entry fields
name_entry = Entry(editreciperoot,text=result[0], font=font_style2, bg='#FFFCF5', fg='#374375', width=50)
name_entry.grid(row=0, column=1, sticky='E')
name_entry.insert(END, result[1])

author_entry = Entry(editreciperoot, font=font_style2,text=result[4], bg='#FFFCF5', fg='#374375', width=50)
author_entry.grid(row=1, column=1, sticky='E')
author_entry.insert(END, result[4])

ingredients_text = Text(editreciperoot, height=6, width=50, font=font_style2, bg='#FFFCF5', fg='#374375')
ingredients_text.grid(row=2, column=1, padx=5, pady=5)

ingredients_text.insert(1.0,result[2])

instructions_text = Text(editreciperoot, height=6, width=50 ,font=font_style2, bg='#FFFCF5', fg='#374375')
instructions_text.grid(row=3, column=1, padx=5, pady=5)
instructions_text.insert(1.0, result[3])

# Button to browse image
image_path = StringVar()
Entry(editreciperoot, textvariable=image_path, state="readonly", font=font_style2, bg='#FFFCF5', fg='#374375', width=30).grid(row=4, column=1, padx=20, pady=5)
Button(editreciperoot, text="Browse", command=browse_image, font=font_style, bd=0, bg='#895159', fg='#FFFCF5').grid(row=4, column=1, padx=5, pady=5, sticky='E')

# Submit button
Button(editreciperoot, text="Submit", command=submit_form, font=font_style, bd=0, bg='#895159', fg='#FFFCF5').grid(row=5, column=0, sticky='W', padx=20, pady=10)


