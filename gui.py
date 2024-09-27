import tkinter as tk
import subprocess
import os
from main import main

school_list = [
    "大更小学校",
    "平舘小学校",
    "田頭小学校",
    "柏台小学校",
    "松野小学校",
    "寄木小学校",
    "平笠小学校",
    "安代小学校",
    "寺田小学校",
    "田山小学校",
]



root = tk.Tk()
root.geometry("400x400")


variable = tk.StringVar(root)
variable.set(school_list[0])
selected_school = ""

def open_record_folder():
    path = os.path.abspath("./data/record")
    checkFolder(path)

def open_input_folder():
    path = os.path.abspath("./data/input")
    checkFolder(path)

def checkFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    subprocess.Popen(['explorer', path], shell=True)

def execute():
    print(selected_school)
    if selected_school in school_list:
        print("a")
        main(selected_school[:-3])

def callback(*args):
    global selected_school
    selected_school = variable.get()
    print(selected_school)

button_setRecords = tk.Button(root, text="リザルトファイルを追加",command=open_record_folder)
button_setInputs = tk.Button(root, text="入力用ファイルを追加",command=open_input_folder)
button_execute = tk.Button(root, text="入力用ファイルに書き込む", command=execute)
opt = tk.OptionMenu(root, variable, *school_list)
opt.config(width=90)




button_setRecords.pack(anchor="center", expand=True)
button_setInputs.pack(anchor="center", expand=True)
button_execute.pack(anchor="center", expand=True)
opt.pack(anchor="center", expand=True)
variable.trace("w", callback)

root.mainloop()



