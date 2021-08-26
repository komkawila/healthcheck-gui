from tkinter import *

root = Tk()
# root.geometry("750x450")

bg = PhotoImage(file = r"assets/images/bg/bg.png") 

my_canvas = Canvas(root,width=750,height=450)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg,anchor="nw")
my_canvas.create_text(370,90,text="กรุณาเลือกภาษา",font=("Helvetica",35),fill="brown")
my_canvas.create_text(370,135,text="Choose your language",font=("Helvetica",35),fill="brown")
photo_Eng = PhotoImage(file = r"assets/images/Eng.png")
photoimage_ENG = photo_Eng.subsample(3, 3)
btEN = Button(root, image = photoimage_ENG,borderwidth=1 )
photo_TH = PhotoImage(file = r"assets/images/thai.png")
photoimage_TH = photo_TH.subsample(3, 3)
btTH = Button(root, image = photoimage_TH,borderwidth=1 )

my_canvas.create_window(200,300,window=btEN)
my_canvas.create_window(600,300,window=btTH)

#img = PhotoImage(file="assets\images\Eng.png")
#my_canvas.create_image(0,0, anchor=NW, image=img)
#  root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.mainloop()
