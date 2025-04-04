import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk, ImageGrab
from io import BytesIO
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter, landscape

def create_searchpage():
    from home import search_value as s
    global search_value
    search_value=s
    def open_homepage():
        searchroot.destroy()
        from home import create_homepage
        create_homepage()

    def open_aboutpage():
        searchroot.destroy()
        from about import aboutroot
        aboutroot.mainloop()

    def printfun():
        try:
            # Capture the screenshot of searchroot
            searchroot.update()
            img = ImageGrab.grab(bbox=(searchroot.winfo_rootx(), searchroot.winfo_rooty(),
                                        searchroot.winfo_rootx() + searchroot.winfo_width(),
                                        searchroot.winfo_rooty() + searchroot.winfo_height()))

            # Create a PDF document
            pdf_buffer = io.BytesIO()
            c = canvas.Canvas(pdf_buffer)
            c.setPageSize((2000, 1800))  # Increase the page size

            # Calculate the position of the screenshot
            x = 0  # Margin on the left
            y = 0  # Margin on the top
            width = 1800  # Width of the screenshot
            height = 2000  # Height of the screenshot

            # Draw the screenshot onto the canvas with proper alignment
            c.drawImage(ImageReader(img), x, y, width=width, height=height)

            # Save the PDF document
            c.save()

            # Save the PDF document to a file
            with open("output.pdf", "wb") as f:
                f.write(pdf_buffer.getvalue())

            # Open the PDF file
            try:
                os.startfile("output.pdf")
            except Exception as e:
                print("Error opening PDF file:", e)

        except Exception as e:
            print("Error creating PDF:", e)

    # Create searchroot
    searchroot = Tk()
    searchroot.title('Home')
    searchroot.geometry('950x750')
    searchroot.configure(bg='#FFFCF5')
    navbar_frame = Frame(searchroot, bg='#374375')
    navbar_frame.pack(side=TOP, fill=BOTH)
    searchroot.configure(bg='#FFFCF5')
    font_style = ("Arial", 24)
    font_style2 = ("Arial", 20)
    font_style3 = ("Arial", 12)

    home_button = Button(navbar_frame, font=font_style, text="Home", bd=0, command=open_homepage, bg='#374375', fg='#FFFCF5')
    home_button.pack(side=LEFT, padx=10, pady=5)

    about_button = Button(navbar_frame, font=font_style, text="About", bd=0, command=open_aboutpage, bg='#374375', fg='#FFFCF5')
    about_button.pack(side=LEFT, padx=10, pady=5)

    # Call main function

    try:
        conn = mysql.connector.connect(host="localhost", user="root", database="miniprojectprp")
        cursor = conn.cursor()
        query = "SELECT * FROM recipe WHERE name= %s"
        cursor.execute(query, (search_value,))
        myresult = cursor.fetchall()

        image_labels = []
        for result in myresult:
            image_data = result[5]
            image = Image.open(BytesIO(image_data))
            tk_image = ImageTk.PhotoImage(image)

            framer = Frame(searchroot, bg='#FFFCF5')
            framer.pack()
            framer.columnconfigure(0, weight=1)
            framer.columnconfigure(0, weight=2)
            recipe_name = Label(framer, text=result[1].title(), bg='#FFFCF5', font=font_style, fg='#374375')
            recipe_name.grid(row=0, column=0, pady=15, sticky=W)

            author = Label(framer, text="by " + result[4].upper(), font=font_style2, bg='#FFFCF5', fg='#374375')
            author.grid(row=0, column=1, pady=15, sticky=W)

            ingtitle = Label(framer, text="Ingredients:", justify=LEFT, font=font_style3, bg='#FFFCF5', fg='#374375', anchor='w')
            ingtitle.grid(row=1, column=0, pady=20, sticky=W)

            ingredient = Text(framer, font=font_style3, width=30, height=15, bd=0, bg='#FFFCF5', fg='#374375')
            ingredient.insert(1.0, result[2])
            ingredient.grid(row=2, rowspan=1, column=0, pady=10, sticky=NW)
            ingredient.config(state=DISABLED)

            institle = Label(framer, text="Instructions:", justify=LEFT, font=font_style3, bg='#FFFCF5', fg='#374375', anchor='w')
            institle.grid(row=1, column=1, sticky=NW, padx=10)

            instruction = Text(framer, wrap=WORD, bd=0, height=30, width=52, font=font_style3, bg='#FFFCF5', fg='#374375')
            instruction.insert(1.0, result[3])
            instruction.config(state=DISABLED)
            instruction.grid(row=2, rowspan=3, column=1, sticky=NW, padx=15)

            image_label = Label(framer, image=tk_image)
            image_label.grid(row=3, column=0, rowspan=2, pady=10, sticky=W)

            b1 = Button(framer, text="Print", command=printfun, font=font_style, bd=0, bg='#895159', fg='#FFFCF5')
            b1.grid(row=4, column=2, padx=20, pady=20, sticky=SE, rowspan=1)
            framer.place()
            image_labels.append(image_label)

        conn.close()
        cursor.close()

    except mysql.connector.Error as err:
        print("Error:", err)

    searchroot.mainloop()

create_searchpage()

