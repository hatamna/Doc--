import tkinter
from tkinter import font
from tkinter import ttk
import sv_ttk

app = tkinter.Tk()

# Code what the 'B' button does
def bolding():
    #create font
    boldfont=font.Font(my_text, my_text.cget("font"))
    boldfont.configure(weight="bold")
    #configure a tag
    my_text.tag_configure("bold", font=boldfont)
    #if statement to see if tag has been set
    current_tags = my_text.tag_names("sel.first")

    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")

# Code what the 'I' button does
def italicising():
    #create font
    italfont=font.Font(my_text, my_text.cget("font"))
    italfont.configure(slant="italic")
    #configure a tag
    my_text.tag_configure("italic", font=italfont)
    #if statement to see if tag has been set
    current_tags = my_text.tag_names("sel.first")
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

# Code what the 'Complete Sentence' button does (using Gemini)
def compSent():
    pass

# Code what the 'Complete Paragraph' button does (using Gemini)
def compPara():
    pass

app.title("Doc-- Simple AI-Powered Document Editor")
app.geometry('700x450')

button_frame = ttk.Frame(app)
button_frame.pack()

bold_button = ttk.Button(button_frame, text="B", command=bolding)
bold_button.grid(row=0, column = 0, padx=5)

italic_button = ttk.Button(button_frame, text=' I ', command=italicising)
italic_button.grid(row=0, column = 1)

my_text = tkinter.Text(app, width=85, height=20)
my_text.pack(pady=20)

button_frame2 = ttk.Frame(app)
button_frame2.pack()

cs_button = ttk.Button(button_frame2, text="Complete Sentence")
cs_button.grid(row=0, column = 0)

cpara_button = ttk.Button(button_frame2, text="Complete Paragraph")
cpara_button.grid(row=0, column = 1, padx=5)

sv_ttk.set_theme("dark")
app.mainloop()
