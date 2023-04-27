from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\github\Complex\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1000")
window.configure(bg = "#1E1E1E")


canvas = Canvas(
    window,
    bg = "#1E1E1E",
    height = 1000,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    284.0,
    542.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1011.0,
    501.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(n),
    relief="flat"
)
button_1.place(
    x=675.0,
    y=651.0,
    width=168.0,
    height=64.0
)

canvas.create_text(
    682.0,
    371.0,
    anchor="nw",
    text="username ",
    fill="#666666",
    font=("Poppins Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    949.0,
    430.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=694.0,
    y=402.0,
    width=510.0,
    height=54.0
)

canvas.create_text(
    682.0,
    483.0,
    anchor="nw",
    text="Password",
    fill="#666666",
    font=("Poppins Regular", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    949.0,
    542.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=694.0,
    y=514.0,
    width=510.0,
    height=54.0
)
n =str(entry_bg_1)
canvas.create_text(
    682.0,
    574.0,
    anchor="nw",
    text="Use 8 or more characters with a mix of letters, numbers & symbols",
    fill="#666666",
    font=("Poppins Regular", 14 * -1)
)

canvas.create_text(
    682.0,
    303.0,
    anchor="nw",
    text="LOGIN",
    fill="#333333",
    font=("Poppins Medium", 32 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1370.0,
    82.0,
    image=image_image_3
)
window.resizable(False, False)

print(n)
window.mainloop()
