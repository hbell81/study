import tkinter

root = tkinter.Tk()
root.title("おみくじソフト")
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="python_game\\chapter6\\miko.png")
canvas.create_image(400, 300, image=gazou)

label = tkinter.Label(root, text="？？", font=("Times New Roman", 120), bg="white")
label.place(x=380, y=60)
button = tkinter.Button(root, text="おみくじを引く", font=("Times New Roman", 36), fg="skyblue")
button.place(x=360, y=400)

root.mainloop()
