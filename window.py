from tkinter import *
class MainWindow:
    def __init__(self):
        None
    def __del__(self):
        None

    def Create_inputbox(title, message, button_text):
        root = Tk()
        root.title("dirCleaner")
        root.resizable(False, False)

        label = Label(text="Введите директорию, в которой нужно прибраться")
        label.pack()

        text = ''
        def on_return(e=None):
            nonlocal text
            text = textbox.get()
            root.destroy()

        textbox = Entry(width=40)
        textbox.bind('<Return>', on_return)
        textbox.pack()
        textbox.focus_set()

        button = Button(text=button_text, command=on_return)
        button.pack()

        root.mainloop()

        return text