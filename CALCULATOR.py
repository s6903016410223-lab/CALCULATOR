import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Calculator")
app.geometry("350x500")
app.resizable(False, False)

expression = ""

display = ctk.CTkEntry(
    app,
    width=320,
    height=60,
    font=("Arial", 28),
    justify="right"
)
display.pack(pady=20)


def click(value):
    global expression
    expression += str(value)
    display.delete(0, "end")
    display.insert("end", expression)


def clear():
    global expression
    expression = ""
    display.delete(0, "end")


def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, "end")
        display.insert("end", result)
        expression = result
    except:
        display.delete(0, "end")
        display.insert("end", "Error")
        expression = ""


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+']
]

frame = ctk.CTkFrame(app)
frame.pack()

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "C":
            cmd = clear
        else:
            cmd = lambda t=text: click(t)

        btn = ctk.CTkButton(
            frame,
            text=text,
            width=70,
            height=60,
            font=("Arial", 22),
            command=cmd
        )
        btn.grid(row=r, column=c, padx=5, pady=5)

equal = ctk.CTkButton(
    app,
    text="=",
    width=300,
    height=60,
    font=("Arial", 26),
    command=calculate
)

equal.pack(pady=15)

app.mainloop()