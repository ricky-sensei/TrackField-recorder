import tkinter as tk


root = tk.Tk()

root.geometry("400x400")

button_setResults = tk.Button(root, text="リザルトファイルを追加", width= 200)
button_setEntries = tk.Button(root, text="入力用ファイルを追加")
button_execute = tk.Button(root, text="入力用ファイルんい書き込む")

button_setResults.pack(anchor="center", expand=True)
button_setEntries.pack(anchor="center", expand=True)
button_execute.pack(anchor="center", expand=True)

root.mainloop()



