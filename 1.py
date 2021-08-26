#!/usr/bin/env python
#!/usr/bin/python3
import binascii
import io
import os
import sys
from PIL import Image
from smartcard.System import readers
from smartcard.util import HexListToBinString, toHexString, toBytes
import numpy as np

import _thread
import time

from tkinter import *


status_waiting_card = False
status_read_card = False

def thai2unicode(data):
	result = ''
	result = bytes(data).decode('tis-620')
	return result.strip();

def getData(cmd, req = [0x00, 0xc0, 0x00, 0x00]):
	data, sw1, sw2 = connection.transmit(cmd)
	data, sw1, sw2 = connection.transmit(req + [cmd[-1]])
	return [data, sw1, sw2];
    
def print_time( threadName, delay):
    global status_waiting_card
    global status_read_card
    # Check card
    SELECT = [0x00, 0xA4, 0x04, 0x00, 0x08]
    THAI_CARD = [0xA0, 0x00, 0x00, 0x00, 0x54, 0x48, 0x00, 0x01]

    # CID
    CMD_CID = [0x80, 0xb0, 0x00, 0x04, 0x02, 0x00, 0x0d]

    # TH Fullname
    CMD_THFULLNAME = [0x80, 0xb0, 0x00, 0x11, 0x02, 0x00, 0x64]

    # EN Fullname
    CMD_ENFULLNAME = [0x80, 0xb0, 0x00, 0x75, 0x02, 0x00, 0x64]

    # Date of birth
    CMD_BIRTH = [0x80, 0xb0, 0x00, 0xD9, 0x02, 0x00, 0x08]

    # Gender
    CMD_GENDER = [0x80, 0xb0, 0x00, 0xE1, 0x02, 0x00, 0x01]

    # Card Issuer
    CMD_ISSUER = [0x80, 0xb0, 0x00, 0xF6, 0x02, 0x00, 0x64]

    # Issue Date
    CMD_ISSUE = [0x80, 0xb0, 0x01, 0x67, 0x02, 0x00, 0x08]

    # Expire Date
    CMD_EXPIRE = [0x80, 0xb0, 0x01, 0x6F, 0x02, 0x00, 0x08]

    # Address
    CMD_ADDRESS = [0x80, 0xb0, 0x15, 0x79, 0x02, 0x00, 0x64]
    while True:
        while status_waiting_card:
            try:
                print("SELECT = ")
                print(SELECT)
                print("THAI_CARD = ")
                print(THAI_CARD)
                readerList = readers()
                reader = readerList[0]
                connection = reader.createConnection()
                connection.connect()
                atr = connection.getATR()
                print ("ATR: " + toHexString(atr))
                if (atr[0] == 0x3B & atr[1] == 0x67):
                    req = [0x00, 0xc0, 0x00, 0x01]
                else :
                    req = [0x00, 0xc0, 0x00, 0x00]
                print(atr)
                
                # Check card
                data, sw1, sw2 = connection.transmit(SELECT + THAI_CARD)
                print ("Select Applet: %02X %02X" % (sw1, sw2))
                print(data)
                '''
                # CID
                data = getData(CMD_CID, req)
                cid = thai2unicode(data[0])
                print ("CID: " + cid)'''


                show_frame(frame_check_th)
                #status_read_card = True
                status_waiting_card = False
                print(" !!!!!!!!!!!!!1 break")
                break
            except:
                print("Not Card")

                
def show_frame(frame):
    frame.tkraise()
    
def insertcard():
    show_frame(frame_insertcard_th)
    global status_waiting_card
    status_waiting_card = True
    print("status_waiting_card = ")
    print(status_waiting_card)
    if status_waiting_card == True:
        print("Condition")
    
window = Tk()

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame_home = Frame(window)
frame_insertcard_th = Frame(window)
frame_insertcard_en = Frame(window)
frame_check_th = Frame(window)
for frame in (frame_home, frame_insertcard_th, frame_insertcard_en, frame_check_th):
    frame.grid(row=0,column=0,sticky='nsew')
    
    
#==================Frame 1 code
bg = PhotoImage(file = r"assets/images/bg/bg.png") 

my_canvas = Canvas(frame_home,width=750,height=450)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg,anchor="nw")
my_canvas.create_text(370,90,text="กรุณาเลือกภาษา",font=("Helvetica",35),fill="brown")
my_canvas.create_text(370,135,text="Choose your language",font=("Helvetica",35),fill="brown")
photo_Eng = PhotoImage(file = r"assets/images/Eng.png")
photoimage_ENG = photo_Eng.subsample(3, 3)
btEN = Button(frame_home, image = photoimage_ENG,borderwidth=1 ,command=lambda:show_frame(frame_insertcard_en))
photo_TH = PhotoImage(file = r"assets/images/thai.png")
photoimage_TH = photo_TH.subsample(3, 3)
btTH = Button(frame_home, image = photoimage_TH,borderwidth=1 ,command=insertcard)

my_canvas.create_window(200,300,window=btEN)
my_canvas.create_window(600,300,window=btTH)



#================== frame_insertcard_th code
my_canvas = Canvas(frame_insertcard_th,width=750,height=450)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg,anchor="nw")
my_canvas.create_text(400,85,text="กรุณาสอดบัตรประชาชน",font=("Helvetica",35),fill="brown")

img_insert_th = PhotoImage(file="assets/images/insert_card/pic1.png")
my_canvas.create_image(200,150, anchor=NW, image=img_insert_th)

#================== frame_insertcard_en code
my_canvas = Canvas(frame_insertcard_en,width=750,height=450)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg,anchor="nw")
my_canvas.create_text(400,85,text="Please insert your ID card.",font=("Helvetica",35),fill="brown")

img_insert_en = PhotoImage(file="assets/images/insert_card/pic1.png")
my_canvas.create_image(200,150, anchor=NW, image=img_insert_en)

#================== frame_check_th code
my_canvas = Canvas(frame_check_th,width=750,height=450)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg,anchor="nw")
my_canvas.create_text(400,150,text="ตรวจสอบข้อมูล และ กดยืนยัน",font=("Helvetica",35),fill="brown")

photo_Eng = PhotoImage(file = r"assets/images/start/ยืนยัน.png")
photoimage_ENG2 = photo_Eng.subsample(3, 3)
btEN_check = Button(frame_check_th, image = photoimage_ENG2,borderwidth=1 )
photo_TH = PhotoImage(file = r"assets/images/start/ยกเลิก.png")
photoimage_TH2 = photo_TH.subsample(3, 3)
btTH_check = Button(frame_check_th, image = photoimage_TH2,borderwidth=1 )

my_canvas.create_window(200,350,window=btEN_check)
my_canvas.create_window(600,350,window=btTH_check)
















show_frame(frame_home)

_thread.start_new_thread( print_time, ("Thread-1", 0.1, ) )

window.mainloop()
    #pass


