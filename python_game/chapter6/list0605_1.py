import tkinter

root = tkinter.Tk()
root.title("おみくじソフト")
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="python_game\\chapter6\\miko.png")
canvas.create_image(400, 300, image=gazou)

root.mainloop()
