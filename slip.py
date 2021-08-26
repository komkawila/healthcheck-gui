from tkinter import *

root = Tk()

bg = PhotoImage(file = r"assets/images/bg/bg.png") 

my_canvas = Canvas(root,width=750,height=450)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg,anchor="nw")
my_canvas.create_text(400,85,text="กรุณาถอดบัตรประชาชน และรับใบสลิป",font=("Helvetica",35),fill="brown")



img = PhotoImage(file="0000.png")
my_canvas.create_image(230,150, anchor=NW, image=img)

root.mainloop()