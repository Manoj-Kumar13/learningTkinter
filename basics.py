from tkinter import *

# creating a root element
root = Tk()

# creating an input field
entry = Entry(root, bg="black", fg="green", borderwidth=5)
entry.pack()

# creating a label
myLabel = Label(root, text = "Hello World!")
label1 = Label(root, text="My Name is Baldr")
label2 = Label(root, text="I'm the son of freya")

def buttonClick():
    buttonLabel = Label(root, text="hello " + entry.get())
    buttonLabel.pack()

# creating a button
myButton = Button(root, text="Enter your name above" , command=buttonClick, fg="white", bg="purple", padx=20,  pady=10).pack()


# just for placing on the screen
myLabel.pack()
label1.pack()
label2.pack()

# creating a main loop
root.mainloop()

