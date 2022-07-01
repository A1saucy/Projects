#Libraries needed to run the app
from tkinter import *
from PIL import ImageTk,Image
import tkinter as tk

#Tkinter window and title
root = Tk()
root.title("Danny's Donuts")
root.geometry('900x575')
# Icon image location and code
ico = Image.open('C:/Users/mrapp/OneDrive/Documents/Software development Final Project/chocolate donut.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Text for the maple donut image.
maple_label = Label (root, text = "Maple Donut $0.99", font = ('helvetica',10))
maple_label.grid(row = 0, column = 0, sticky = N)

# Import maple donut image with location and resize.
photo = Image.open ('C:/Users/mrapp/OneDrive/Documents/Software development Final Project/maple donut.png')
resized_image = photo.resize((200,200),Image.ANTIALIAS)
converted_image = ImageTk.PhotoImage(resized_image)

# Label for converted maple donut image.
label = tk.Label (root, image = converted_image, width = 300, height = 150)
label.grid(row = 1, column = 0 , sticky = W)

# Text for asking the user how many donuts they want.
quantity = Label (root, text = 'Enter the quantity of maple donuts you want:', font = ('helvetica',10))
quantity.grid(row = 2, column = 0, sticky = N)
# Label to display def number function text.
result = Label(root, text = '')
result.grid(row = 5, column = 0, sticky = N)
# Error handling of user entry.
def number():
    try:
        int(entry.get())
        result.config(text = 'Please pay at our location.', font = ('helvetica',10))
    except ValueError:
        result.config(text = 'You must enter a whole number for your donut quantity.', font = ('helvetica',10))

# Submit button
submit = Button(root, text = 'Submit', command = number, font = ('helvetica',10))
submit.grid(row = 4, column = 0, sticky = N)

# Taking user input for number of donuts.

entry = Entry(root)
entry.grid(row = 3, column = 0, sticky = N)
def maple_delete():
    entry.delete(0,END)
    result.config(text = '')
maple_Delete = Button(root, text = 'Clear',command = maple_delete, font = ('helvetica',10))
maple_Delete.grid(row = 6, column = 0, sticky = S)
# End of maple donut

# Text for the chocolate donut image.
chocolate_label = Label (root, text = "Chocolate Donut $0.99", font = ('helvetica',10))
chocolate_label.grid(row = 0 , column = 1, sticky = N)

# Import chocolate donut image and resize.
photo2 = Image.open ('C:/Users/mrapp/OneDrive/Documents/Software development Final Project/chocolate donut with sprinkles.png')
photo2_resized = photo2.resize((200,200),Image.ANTIALIAS )
converted_photo2 = ImageTk.PhotoImage(photo2_resized)

# Label for converted chocolate donut image.
label2 = tk.Label (root, image = converted_photo2, width = 300, height = 150  )
label2.grid(row = 1 , column = 1 , sticky = W)

# Text for asking the user how many donuts they want.
quantity1 = Label (root, text = 'Enter the quantity of chocolate donuts you want:', font = ('helvetica',10))
quantity1.grid(row = 2, column = 1, sticky = N)
# Label to display def number funtion text.
result1 = Label(root, text = '')
result1.grid(row = 5, column = 1, sticky = N)
# Error handling of user entry.
def number():
    try:
        int(entry1.get())
        result1.config(text = 'Please pay at our location.', font = ('helvetica',10))
    except ValueError:
        result1.config(text = 'You must enter a whole number for your donut quantity.', font = ('helvetica',10))

# Submit button
submit1 = Button(root, text = 'Submit', command = number, font = ('helvetica',10))
submit1.grid(row = 4, column = 1, sticky = N)

# Taking user input for number of donuts

entry1 = Entry(root)
entry1.grid(row = 3, column = 1, sticky = N)
# Function and button to delete entry and label text.
def chocolate_delete():
    entry1.delete(0,END)
    result1.config(text = '')
chocolate_Delete = Button(root, text = 'Clear',command = chocolate_delete, font = ('helvetica',10))
chocolate_Delete.grid(row = 6, column = 1, sticky = S)
# End of chocolate donut.

# Text for the glazed donut image.
glazed_label = Label (root, text = "Glazed Donut $0.99", font = ('helvetica',10))
glazed_label.grid(row =  0 , column = 2, sticky = N)

# Import glazed donut image and resize.
photo3 = Image.open ('C:/Users/mrapp/OneDrive/Documents/Software development Final Project/glazed donut.png')
photo3_resized = photo3.resize((200,200),Image.ANTIALIAS )
converted_photo3 = ImageTk.PhotoImage(photo3_resized)

# Label for converted glazed donut image.
label3 = tk.Label (root, image = converted_photo3, width = 300, height = 150  )
label3.grid(row = 1, column = 2, sticky = W)

# Text for asking the user how many donuts they want.
quantity2 = Label (root, text = 'Enter the quantity of maple donuts you want:', font = ('helvetica',10))
quantity2.grid(row = 2, column = 2, sticky = N)
# Label to display result of def number function.
result2 = Label(root, text = '')
result2.grid(row = 5, column = 2, sticky = N)
# Error handling of user entry.
def number():
    try:
        int(entry2.get())
        result2.config(text = 'Please pay at our location.', font = ('helvetica',10))
    except ValueError:
        result2.config(text = 'You must enter a whole number for your donut quantity.', font = ('helvetica',10))

# submit button
submit2 = Button(root, text = 'Submit', command = number, font = ('helvetica',10))
submit2.grid(row = 4, column = 2, sticky = N)

# Taking user input for number of donuts.
entry2 = Entry(root)
entry2.grid(row = 3, column = 2, sticky = N)

# Glazed donut delete function and button.
def glazed_delete():
    entry2.delete(0,END)
    result2.config(text = '')
glazed_Delete = Button(root, text = 'Clear',command = glazed_delete, font = ('helvetica',10))
glazed_Delete.grid(row = 6, column = 2, sticky = S)
# End of glazed donut.


# Button to let user exit the program.
button_quit= Button(root, text='Exit', command = root.quit, font = ('helvetica',10))
button_quit.grid(row = 7, column = 1 , sticky = S)

# Entire code for second window.
def open():
    global coffee_converted
    global milk_converted
    global cappuccino_converted
    top = Toplevel() # Name of second window.
    top.title("Danny's Donuts")
    top.geometry('900x575')
    # Icon image.
    ico = Image.open('C:/Users/mrapp/OneDrive/Documents/Software development Final Project/chocolate donut.png')
    photo = ImageTk.PhotoImage(ico)
    top.wm_iconphoto(False, photo)

    # Coffee image name and price.
    coffee_Name_Price = Label (top, text = 'Fresh Coffee $0.99', font = ('helvetica',10))
    coffee_Name_Price.grid(row = 0, column = 0, sticky = N)
    # Second window images.
    coffee =  Image.open( 'C:/Users/mrapp/OneDrive/Documents/Software development Final Project/coffee cup.png'  )
    coffee_resized = coffee.resize((200,200), Image.ANTIALIAS)
    coffee_converted = ImageTk.PhotoImage(coffee_resized)
    # Cappuccino image name and price.
    cappuccino_Name_Price = Label (top, text = 'Fresh Cappuccinos $2.99', font = ('helvetica',10))
    cappuccino_Name_Price.grid(row = 0, column = 1, sticky = N)
    # Cappuccino image.
    cappuccino = Image.open( 'C:/Users/mrapp/OneDrive/Documents/Software development Final Project/cappuccino.png')
    cappuccino_resized = cappuccino.resize((200,200), Image.ANTIALIAS)
    cappuccino_converted = ImageTk.PhotoImage(cappuccino_resized)
    # Milk cup image name and price.
    milk_Name_Price = Label (top, text = 'Fresh milk $1.50', font = ('helvetica',10))
    milk_Name_Price.grid(row = 0, column = 2, sticky = N)
    # Milk cup image.
    milk = Image.open( 'C:/Users/mrapp/OneDrive/Documents/Software development Final Project/milk cup.png')
    milk_resized = milk.resize((200,200), Image.ANTIALIAS)
    milk_converted = ImageTk.PhotoImage(milk_resized)
    # Coffee image label.
    coffeelabel = Label(top, image = coffee_converted, width = 300, height = 150)
    coffeelabel.grid(row = 1, column = 0, sticky = W)
    # Coffee quantity text.
    quantity = Label (top, text = 'Enter the quantity of Coffees you want:', font = ('helvetica',10))
    quantity.grid(row = 2, column = 0, sticky = N)
    # Coffee quantity entry box
    coffee_Entry = Entry(top)
    coffee_Entry.grid(row = 3, column = 0, sticky = N)
    # Label for result of coffee user submission.
    coffee_Result = Label(top)
    coffee_Result.grid(row = 5, column = 0, sticky = N)
    # Error handling of user entry.
    def number():
        try:
            int(coffee_Entry.get())
            coffee_Result.config(text = 'Please pay at our location.', font = ('helvetica',10))
        except ValueError:
            coffee_Result.config(text = 'You must enter a whole number for your donut quantity.', font = ('helvetica',10))

    # Submit button.
    submit = Button(top, text = 'Submit', command = number, font = ('helvetica',10))
    submit.grid(row = 4, column = 0, sticky = N)
    
    # Cappuccino image label.
    cappuccinolabel = Label(top, image = cappuccino_converted, width = 300, height = 150)
    cappuccinolabel.grid(row = 1, column = 1, sticky = W)
    # Cappuccino quantity text.
    quantity1 = Label (top, text = 'Enter the quantity of Cappuccinos you want:', font = ('helvetica',10))
    quantity1.grid(row = 2, column = 1, sticky = N)
    # Cappuccino entry box.
    cappuccino_Entry = Entry(top)
    cappuccino_Entry.grid(row = 3, column = 1, sticky = N)
    # Label for result of cappuccino user submission.
    cappuccino_Result = Label(top)
    cappuccino_Result.grid(row = 5, column = 1, sticky = N)
    # Error handling of user entry.
    def number():
        try:
            int(cappuccino_Entry.get())
            cappuccino_Result.config(text = 'Please pay at our loaction.', font = ('helvetica',10))
        except ValueError:
            cappuccino_Result.config(text = 'You must enter a whole number for your donut quantity.', font = ('helvetica',10))

    # Submit button.
    cappuccino_Submit = Button(top, text = 'Submit', command = number, font = ('helvetica',10))
    cappuccino_Submit.grid(row = 4, column = 1, sticky = N)

    # Milk cup image label.
    milklabel = Label(top, image = milk_converted, width = 300, height = 150)
    milklabel.grid(row = 1, column = 2, sticky = W)
     # Milk cup quantity text.
    quantity2 = Label (top, text = 'Enter the quantity of Milk cups you want:', font = ('helvetica',10))
    quantity2.grid(row = 2, column = 2, sticky = N)
    milk_Entry = Entry(top)
    milk_Entry.grid(row= 3, column = 2, sticky = N)
    # Label to display def number function text
    milk_Result = Label(top)
    milk_Result.grid(row = 5, column = 2, sticky = N)
    # Error handling of user entry.
    def number():
        try:
            int(milk_Entry.get())
            milk_Result.config(text = 'Please pay at our location.', font = ('helvetica',10))
        except ValueError:
            milk_Result.config(text = 'You must enter a whole number for your donut quantity.', font = ('helvetica',10))

    # Submit button.
    milk_Submit = Button(top, text = 'Submit', command = number, font = ('helvetica',10))
    milk_Submit.grid(row = 4, column = 2, sticky = N)

    # Button to let user exit the program.
    button_Quit = Button(top, text='Exit', command = top.quit, font = ('helvetica',10))
    button_Quit.grid(row = 6, column = 1 , sticky = S)
    # Button to go back to first tab.
    button_Back = Button(top, text= 'Back', command = top.destroy, font = ('helvetica',10))
    button_Back.grid(row = 7, column = 0, sticky = S)
    # Function for deleting the text in the entry box and coffee_Result label.
    def coffee_Delete():
        coffee_Entry.delete(0, END)
        coffee_Result.config(text = '')
    # Coffee Entry delete button.
    button_Delete = Button(top, text = 'Clear', command = coffee_Delete, font = ('helvetica',10))
    button_Delete.grid(row = 6, column = 0, sticky = S)
    # Function for deleting the text in the entry box and cappuccino_Result label.
    def cappuccino_Delete():
        cappuccino_Entry.delete(0, END)
        cappuccino_Result.config(text = '')
    # Cappuccino Entry delete button.
    cappuccino_Entry_Delete = Button(top, text = 'Clear', command = cappuccino_Delete, font = ('helvetica',10))
    cappuccino_Entry_Delete.grid(row = 6, column = 1, sticky = S)

    # Function for deleting the text in the entry box and milk_Result label.
    def milk_Delete():
        milk_Entry.delete(0, END)
        milk_Result.config(text = '')
    # Milk Entry delete button.
    milk_Entry_Delete = Button(top, text = 'Clear', command = milk_Delete, font = ('helvetica',10))
    milk_Entry_Delete.grid(row = 6, column = 2, sticky = S)
    



# Button to open the second window to Danny's Donuts.
next_Btn = Button (root, text = 'Next', command = open, font = ('helvetica',10))
next_Btn.grid(row = 7, column = 2, sticky = N)

root.mainloop()