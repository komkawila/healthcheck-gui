#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=1)
    ser.flush()
    ser.write(b'')
    time.sleep(2)
    ser.readline().decode('utf-8').rstrip()
    print('start')
    try:
        while True:
            data = input()
            #print(data + '\r\n')
            data1 = data + "\r\n"
            ser.write(data1.encode())
            ser.flush()
            while True:
                if(data != '0'):
                    print("!4")
                    line = ser.readline().decode('utf-8').rstrip()
                    if bool(line) == True:
                        print("DATA : " + line.split(" ")[3])
                        break
                '''elif data == '4':
                    line = ser.readline().decode('utf-8').rstrip()
                    print(line)'''
    except:
        print("ERROR !!!!!!!!!!!!!!!")
