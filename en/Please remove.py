
from tkinter import *

root = Tk()
# root.geometry("750x450")

bg = PhotoImage(file = r"../assets/images/bg/bg.png") 

my_canvas = Canvas(root,width=750,height=450)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg,anchor="nw")
my_canvas.create_text(390,150,text="remove your ID card and slip.",font=("Helvetica",35),fill="brown")
photo_Eng = PhotoImage(file = r"../assets/images/start/confirm.png")
photoimage_ENG = photo_Eng.subsample(3, 3)
photoimage_ENG = photo_Eng.subsample(3, 3)
btEN = Button(root, image = photoimage_ENG,borderwidth=1 )


my_canvas.create_window(375,350,window=btEN)
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.mainloop()