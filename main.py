from directory import Directory
from window import MainWindow
from errorwindow import errorwindow
import os
from tkinter import messagebox
def getfiletype(name):
    type = ""
    f = False  # эта штука проверяет, была ли точка до текущей j
    for j in i:
        if j == '.':
            f = True
        if f:
            type += j

    return type
ok = False
while not ok: #это блять не работает почему-то
    dir = Directory(MainWindow.Create_inputbox('1', '1', 'Отправить')).getdirectory()
    if os.path.isdir(dir):
        ok = True
    else:
        errorwindow.showerror()
types = []
os.chdir(dir)
for i in os.listdir():
    if getfiletype(i) not in types and getfiletype(i) != "":
        types.append(getfiletype(i))
for i in types:
    os.mkdir(i)

os.chdir(dir)

for i in os.listdir():
    if getfiletype(i) != "" and i not in types:
        os.replace(dir+"\\"+i, dir+"\\"+getfiletype(i)+"\\"+i)