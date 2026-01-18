import tkinter
from tkinter import font
from tkinter import ttk
import sv_ttk

app = tkinter.Tk()

def apply_style_tags(start, end):
    # Check what styles are currently ON at the start of selection
    tags = set(my_text.tag_names(start))
    bold_on = "bold" in tags
    italic_on = "italic" in tags

    # Always remove the combo tag first, then re-add if needed
    my_text.tag_remove("bold_italic", start, end)

    if bold_on and italic_on:
        my_text.tag_add("bold_italic", start, end)

# Code what the 'B' button does
def bolding():
    if not my_text.tag_ranges("sel"):
        return
    start, end = "sel.first", "sel.last"
    if "bold" in my_text.tag_names(start):
        my_text.tag_remove("bold", start, end)
    else:
        my_text.tag_add("bold", start, end)
    apply_style_tags(start, end)

# Code what the 'I' button does
def italicising():
    if not my_text.tag_ranges("sel"):
        return
    if not my_text.tag_ranges("sel"):
        return
    start, end = "sel.first", "sel.last"
    if "italic" in my_text.tag_names(start):
        my_text.tag_remove("italic", start, end)
    else:
        my_text.tag_add("italic", start, end)

    apply_style_tags(start, end)

# Code what the 'Complete Sentence' button does (using Gemini)
def compSent():
    pass

# Code what the 'Complete Paragraph' button does (using Gemini)
def compPara():
    pass

app.title("Doc-- Simple AI-Powered Document Editor")
app.geometry('700x500')

button_frame = ttk.Frame(app)
button_frame.pack()

bold_button = ttk.Button(button_frame, text="B", command=bolding)
bold_button.grid(row=0, column = 0, padx=5)

italic_button = ttk.Button(button_frame, text=' I ', command=italicising)
italic_button.grid(row=0, column = 1)

base_font = font.Font(family="Courier New", size=12)

my_text = tkinter.Text(app, width=85, height=20, font=base_font, exportselection=0)
my_text.pack(pady=20)

# Define text tags for styling
bold_font = font.Font(my_text, my_text.cget("font"))
bold_font.configure(weight="bold")
italic_font = font.Font(my_text, my_text.cget("font"))
italic_font.configure(slant="italic")
bold_italic_font = font.Font(my_text, my_text.cget("font"))
bold_italic_font.configure(weight="bold", slant="italic")
my_text.tag_configure("bold", font=bold_font)
my_text.tag_configure("italic", font=italic_font)
my_text.tag_configure("bold_italic", font=bold_italic_font)

button_frame2 = ttk.Frame(app)
button_frame2.pack()

cs_button = ttk.Button(button_frame2, text="Complete Sentence")
cs_button.grid(row=0, column = 0)

cpara_button = ttk.Button(button_frame2, text="Complete Paragraph")
cpara_button.grid(row=0, column = 1, padx=5)

sv_ttk.set_theme("dark")
app.mainloop()
