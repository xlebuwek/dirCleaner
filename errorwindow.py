from tkinter import *
class errorwindow:
    def __init__(self):
        None
    def __del__(self):
        None
    def showerror():
        root = Tk()
        root.title("Ошибка")
        root.resizable(False, False)

        label = Label(text="Вы ввели неверную директорию")
        label.pack()

        def on_return(e=None):
            root.destroy()

        root.bind('<Return>', on_return)

        button = Button(text="Ок", command=on_return)
        button.pack()

        root.mainloop()

        return None