from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from io import BytesIO
font_style = ("Arial", 24)
font_style2 = ("Arial", 20)
font_style3 = ("Arial", 12)
def create_homepage():
    global homeroot, search_entry
    def search():
        global search_value
        try: 
            search_value = (search_entry.get()).lower()
        except Exception as e:
            print(e)
        conn = mysql.connector.connect(host="localhost", user="root", database="miniprojectprp")
        cursor = conn.cursor()
        query = "SELECT * FROM recipe WHERE name= %s"
        cursor.execute(query, (search_value,))
        myresult = cursor.fetchall()
        if(cursor.rowcount==0):
            messagebox.askokcancel("unsuccessful","recipe not found")
            return
        homeroot.destroy()
        from search import create_searchpage
        create_searchpage()

    def open_homepage():
        pass

    def open_aboutpage():
        homeroot.destroy()
        from about import aboutroot
        aboutroot.mainloop()

    def create_home():
        # Define all the elements inside this function
        pass

    # Create homeroot
    homeroot = Tk()
    homeroot.title('Home')
    homeroot.geometry('950x750')
    navbar_frame = Frame(homeroot, bg='#374375')
    navbar_frame.pack(side=TOP, fill=X)
    homeroot.configure(bg='#FFFCF5')
    search_frame = Frame(navbar_frame, bg='#374375')
    search_frame.pack(side=RIGHT, fill=X, padx=20, pady=10)
    search_entry = Entry(search_frame, font=font_style2, width=30)
    search_entry.pack(side=LEFT)
    home_button = Button(navbar_frame, font=font_style, text="Home", bd=0, command=open_homepage, bg='#374375', fg='#FFFCF5')
    home_button.pack(side=LEFT, padx=10, pady=5)
    about_button = Button(navbar_frame, font=font_style, text="About", bd=0, command=open_aboutpage, bg='#374375', fg='#FFFCF5')
    about_button.pack(side=LEFT, padx=10, pady=5)
    search_label = Label(search_frame, font=font_style, text="Search:", fg='#FFFCF5', bd=0, bg='#374375')
    search_label.pack(side=LEFT, padx=5)
    search_entry.bind("<Return>", search)
    search_button = Button(search_frame, font=font_style3, text="Search", fg='#FFFCF5', bg='#dfaea1', command=search, bd=0)
    search_button.pack(side=LEFT, padx=5)
    welcome_label = Label(homeroot, text="WELCOME TO MYRECIPE", font=font_style, bg='#FFFCF5', fg='#895159')
    welcome_label.pack(side=TOP, fill=X, pady=20)

    try:
        conn = mysql.connector.connect(host="localhost", user="root", database="miniprojectprp")
        cursor = conn.cursor()
        query = "SELECT * FROM recipe"
        cursor.execute(query)
        myresult = cursor.fetchmany(6)

        tk_images = []  # List to store Tkinter PhotoImage objects

        outer_frame = Frame(homeroot, bg="#FFFCF5")
        outer_frame.pack(fill=BOTH, expand=True)

        canvas = Canvas(outer_frame, bg="#FFFCF5")
        canvas.pack(side=TOP, fill=BOTH, expand=True)

        inner_frame = Frame(canvas, bg="#FFFCF5")
        canvas.create_window((0, 0), window=inner_frame, anchor='nw')

        for i, result in enumerate(myresult):
            image_data = result[5]
            image = Image.open(BytesIO(image_data))
            tk_image = ImageTk.PhotoImage(image)
            tk_images.append(tk_image)
            if i < 3:
                framer = Frame(inner_frame, bg="#374375")
                image_label = Label(framer, image=tk_image, height=200, width=200)
                image_label.grid(row=0, column=0, pady=10, padx=10)
                name_label = Label(framer, text=result[1].title(), font=font_style2, bg="#374375", fg="#FFFCF5")
                name_label.grid(row=1, column=0, padx=10, pady=10)
                framer.grid(row=0, column=i, padx=40, pady=20)
            else:
                framer = Frame(inner_frame, bg="#374375")
                image_label = Label(framer, image=tk_image, height=200, width=200)
                image_label.grid(row=0, column=0, pady=10, padx=10)
                name_label = Label(framer, text=result[1].title(), font=font_style2, bg="#374375", fg="#FFFCF5")
                name_label.grid(row=1, column=0, padx=10, pady=10)
                framer.grid(row=1, column=i-3, padx=40, pady=20)
    except mysql.connector.Error as e:
        print("MySQL Error:", e)
    except IOError as e:
        print("Image Error:", e)
    except Exception as e:
        print("Error:", e)

    # Make the variables accessible globally


    # Bind Enter key to search function
    search_entry.bind("<Return>", search)

    # Run main loop
    homeroot.mainloop()

create_homepage()
