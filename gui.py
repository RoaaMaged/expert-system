# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import *
from tkinter import font
from joblib import dump, load
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\Gipsy GUI\assets")

model=load("model.joblib")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1470x982")
window.configure(bg = "#ffffff")

canvas = Canvas(
    window,
    window.title("Resizable Window"),

    bg = "#1C2951",
    height = 982,
    width = 1512,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    886.0,
    497.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    767.0,
    115.0,

    image=image_image_2
)

entry_1 = Entry(
    window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=389.0,
    y=250.0,
    width=732.0,
    height=32.0
)

entry_2 = Entry(
    window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    
    x=389.0,
    y=320.0,
    width=732.0,
    height=32.0
)
entry_3 = Entry(
    window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=389.0,
    y=395.0,
    width=732.0,
    height=32.0
)

entry_4 = Entry(
    window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=389.0,
    y=470.0,
    width=732.0,
    height=32.0
)

data1 = canvas.create_text(
    390.0,
    210.0,
    anchor="nw",
    text="Data 1",
    fill="#F9F9F9",
    font=("Poppins Regular", 25 * -1)
)

data2 = canvas.create_text(
    390.0,
    280,
    anchor="nw",
    text="Data 2",
    fill="#F9F9F9",
    font=("Poppins Regular", 25 * -1)
)

data3 = canvas.create_text(
    390.0,
    352.0,
    anchor="nw",
    text="Data 3",
    fill="#F9F9F9",
    font=("Poppins Regular", 25 * -1)
)

data4 = canvas.create_text(
    390.0,
    430.0,
    anchor="nw",
    text="Data 4",
    fill="#F9F9F9",
    font=("Poppins Regular", 25 * -1)
)

feature_names_text = [data1, data2, data3, data4]

for i, feature in enumerate(model.feature_names_in_):
    canvas.itemconfig(feature_names_text[i], text=feature)

# result = model.predict([[10,50,20,22]])[0]

result_text = canvas.create_text(
    650.0,
    550.0,  
    anchor="nw",
    text='',
    fill="#FFFCFC",
    font=("Poppins Regular", 40 * -1)
)

def analyze():
    
    features = [float(entry_1.get()), float(entry_2.get()),float(entry_3.get()),float(entry_4.get())]
    result = model.predict([features])[0]
    canvas.itemconfig(result_text, text = result)
    

from termcolor import colored
button_1= Button(
    window,
    text="START!",
    bg="white", font="bold",
    borderwidth=0,
    border="4px solid",
    command=analyze,
    relief="flat",
    )

button_1.place(
    x=690.0,
    y=670.0,
    width=120.0,
    height=40
)
window.resizable(True, True)

window.mainloop()