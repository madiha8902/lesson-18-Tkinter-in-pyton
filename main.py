from tkinter import *

window=Tk()
window.title("my tkinter window")
window.geometry("900x900")

greeting=Label(text="Madiha",fg="red",bg="yellow")
greeting.pack()
button=Button(text="click me",fg="yellow",bg="red")
button.pack()
entry=Entry(bg="blue",fg="white",width=70)
entry.pack()

frame=Frame(master=window,relief=RAISED,borderwidth=5)

frame.pack()
label=Label(master=frame,text="my window")
label.pack()
textbox=Text(fg="blue",bg="white")
textbox.pack()
window.mainloop()