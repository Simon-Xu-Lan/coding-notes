from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
# Padding
# Background color
window.config(padx=20, pady=30, bg="white")

#Labels
label = Label(text="This is old text", fg="white", bg="blue")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    input_text = text.get(1.0, END)
    print(input_text)
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

# Add images to buttons
my_image = PhotoImage(file="path/to/image_file.png")
button = Button(image=my_image, highlightthickness=0)

# disable button
button.config(state="disabled")

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
# END means last position
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# layout management
# place the label at position from top left corner, 10 right and 200 down
label.place(x=10,y=200)

# grid
# pack and grid are exclusive, you can only use either one
button2 = Button(text="Click Me 2")
button2.grid(column=2, row=0)

# Delete from start to end
entry.delete(0, END)


# mainloop must and always stay at bottom
window.mainloop()

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.gif")
canvas.create_image((100, 100), image=logo_img)
    # add text to canvas
quote_text = canvas.create_text(
    150, 
    207, 
    width =180,   # set the text width, then the text will wrap automatically
    text="Kanye Quote Goes HERE",
    font=("Arial", 30, "bold"), 
    fill="white"
)

canvas.grid(row=0, column=0, padx=10, pady=20)

canvas.itemconfig(quote_text, text=f"{data['quote']}")
