import tkinter

key = 0

def key_down(e):
    global key
    key = e.keycode
    print("KEY:" + str(key))

def main_proc():
    label["text"] = key
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("リアルタイムキー入力")
root.bind("<KeyPress>", key_down)
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()

main_proc()
root.mainloop()
