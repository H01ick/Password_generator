from tkinter import *
import config
import random
import clipboard

password_to_clipboard = ""


def appearEntrySymbols() -> None:
    entry_your_symbols.grid_remove()
    entry_your_symbols.grid(row=8, column=0, stick="w", padx=30)


def disappearEntrySymbols() -> None:
    entry_your_symbols.grid(row=8, column=0, stick="w", padx=30)
    entry_your_symbols.grid_remove()


def createPass() -> str:
    all_symbols = ""
    if check_numbers_var.get():
        all_symbols += config.numbers
    if check_lower_letters_var.get():
        all_symbols += config.lower_letters
    if check_higher_letters_var.get():
        all_symbols += config.higher_letters
    if symbols_var.get() == 0:
        all_symbols += config.symbols
    elif symbols_var.get() == 1:
        all_symbols += your_symbols_var.get()
    all_symbols = list(all_symbols)
    random.shuffle(all_symbols)
    try:
        password = "".join([random.choice(all_symbols) for x in range(pass_length_var.get())])
    except IndexError:
        password = "Are you stupid?"
    return password


def clickPasswordGenerateButton() -> None:
    password = StringVar()
    password.set(createPass())
    password_label = Label(root, textvariable=password)
    password_label.grid(row=2, column=1)
    global password_to_clipboard
    password_to_clipboard = password.get()


def copyPassword() -> None:
    clipboard.copy(text=password_to_clipboard)


root = Tk()
root.grid_columnconfigure(0, minsize=220)
pass_length_label = Label(text="pass length")
pass_length_var = IntVar(value=8)
pass_length = Entry(root, textvariable=pass_length_var)
check_numbers_var = BooleanVar(value=True)
check_numbers = Checkbutton(root, text="numbers", variable=check_numbers_var)
check_lower_letters_var = BooleanVar(value=True)
check_lower_letters = Checkbutton(root, text="lower letters", variable=check_lower_letters_var)
check_higher_letters_var = BooleanVar(value=True)
check_higher_letters = Checkbutton(root, text="higher letters", variable=check_higher_letters_var)
symbols_var = IntVar()
symbols = Radiobutton(root, text="symbols: '!@#$%&*?№'", variable=symbols_var, value=0, command=disappearEntrySymbols)
your_symbols = Radiobutton(root, text="your symbols", variable=symbols_var, value=1, command=appearEntrySymbols)
your_symbols_var = StringVar()
entry_your_symbols = Entry(root, textvariable=your_symbols_var)
button_generate_password = Button(root, text="Generate", width=14, height=3, command=clickPasswordGenerateButton)
copy_button = Button(root, text="copy", width=10, height=2, command=copyPassword)
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 150
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 150
root.wm_geometry("+%d+%d" % (x, y))


def main():
    button_generate_password.grid(row=0, column=1, stick="w", pady=30)
    pass_length_label.grid(row=1, column=0, stick="w", padx=30)
    pass_length.grid(row=2, column=0, stick="w", padx=30)
    check_numbers.grid(row=3, column=0, stick="w", padx=30)
    check_lower_letters.grid(row=4, column=0, stick="w", padx=30)
    check_higher_letters.grid(row=5, column=0, stick="w", padx=30)
    symbols.grid(row=6, column=0, stick="w", padx=30)
    your_symbols.grid(row=7, column=0, stick="w", padx=30)
    copy_button.grid(row=3, column=1, stick="w", pady=20, rowspan=3)
    root.title(u"Password generator")
    root.geometry("400x380")
    root.mainloop()


if __name__ == "__main__":
    main()
