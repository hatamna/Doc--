from tkinter import *

app = Tk()

def bolding():
    pass

def italicising():
    pass

def compSent():
    pass

def compPara():
    pass

app.title("Doc-- Simple AI-Powered Document Editor")
app.geometry('700x450')

button_frame = Frame(app)
button_frame.pack()

bold_button = Button(button_frame, text="B", padx=5)
bold_button.grid(row=0, column=0)

italic_button = Button(button_frame, text=' I ')
italic_button.grid(row=0, column=1, padx=5)

my_text = Text(app, width=85, height=20)
my_text.pack(pady=20)

button_frame2 = Frame(app)
button_frame2.pack()

cs_button = Button(button_frame2, text="Complete Sentence")
cs_button.grid(row=0, column=0, padx=5)

cpara_button = Button(button_frame2, text="Complete Paragraph")
cpara_button.grid(row=0, column=1, padx=5)

app.mainloop()
