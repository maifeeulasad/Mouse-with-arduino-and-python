import serial
import pyautogui

def mapV(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)


ser = serial.Serial('COM3', 9600)
xMax=1366
yMax=768
while True:
    try:
        myData = ser.readline().strip()
        data = myData.decode('utf-8')
        print(data)
        x,y=data.split("   ")
        pyautogui.moveTo(int(mapV(float(x),0,1023,0,xMax)),int(mapV(float(y),0,1023,0,yMax)))
    except:
        print("error")

        
