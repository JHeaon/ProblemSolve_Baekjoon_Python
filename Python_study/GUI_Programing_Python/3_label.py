from tkinter import *

root = Tk()
root.title("Nado GUI") # 창 이름설정

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="image.png")
photo2 = PhotoImage(file="image2.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    label2.config(image=photo2)
    

btn = Button(root, text="클릭", command=change)
btn.pack()


root.mainloop()