from directory import Directory
from window import MainWindow
import os
dir = Directory(MainWindow.Create_inputbox('1', '1', 'Отправить')).getdirectory()
types = []
os.chdir(dir)
for i in os.listdir():
    type = ""
    f = False #эта штука проверяет, была ли точка до текущей j
    for j in i:
        if j == '.':
            f = True
        if f:
            type+=j
    if type not in types and type != "":
        types.append(type)
for i in types:
    os.mkdir(i)
print(os.listdir())
#for i in os.listdir():
 #   os.replace(dir+"\\"+i, )