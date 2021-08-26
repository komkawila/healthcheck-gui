from tkinter import *

root = Tk()
# root.geometry("750x450")

bg = PhotoImage(file = r"../assets/images/bg/bg.png") 

my_canvas = Canvas(root,width=750,height=450)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg,anchor="nw")
my_canvas.create_text(400,85,text="Please insert your ID card.",font=("Helvetica",35),fill="brown")



img = PhotoImage(file="../assets/images/insert_card/pic1.png")
my_canvas.create_image(200,150, anchor=NW, image=img)
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.mainloop()