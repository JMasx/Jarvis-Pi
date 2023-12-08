# import the opencv module
import os
import socket
import subprocess
import time

import cv2
import numpy

capture = cv2.VideoCapture(0)
cv2.namedWindow = ('HELLO THERE!')
cnt=1
prevPicTime=0
audio = 'C:\\Users\\masca\\Downloads\\Jarvis.mp3'
firstDetection=True


def bluetoothSeek():
    addresses = []
    devices = subprocess.run(['hcitool', 'scan'], Scan=True, Names=True)        #resources using HCITool
    if not devices.returncode:                                                  #IF code does not give error:
        print('Local devices are:\n ')
        for i in devices.stdout.strip().split('\n'):
            addresses.append(i.split([0]))
        
        for i in range(len(addresses)):
            print(f'\t {i+1} {addresses[i]}')

    else:
        print('No devices found.')

def bluetoothConnect(addresses):
    connection = subprocess.run('rfcomm', 'connect', '0', addresses )                        #rfcomm documentation as source for virtual serial port
    if not connection.returncode:
        print('Connected successfully')

def bluetoothDisconnect():
    disconnection=subprocess.run('rfcomm', 'release', '0')
    if not disconnection.returncode:
        print("Disconnected successfully")

def playSound(audioFile):
    try:
        # Use start to open the default media player for the MP3 file (Windows command)
        #os.system("start {}".format(audioFile))
        subprocess.Popen(['start', 'Groove Music.exe', audioFile], shell=True, creationflags=subprocess.DETACHED_PROCESS)
    except Exception as e:
        print('Could not play audio: {%s}' % e)

if bluetoothSeek:
    inputIndex = input("Choose a device # from the list: ")
    bluetoothConnect[bluetoothSeek[inputIndex-1]]
while capture.isOpened():
    # to read frame by frame
    _, currentFrame = capture.read()
    _, nextFrame = capture.read()

    
    motionSens=numpy.sum(cv2.absdiff(currentFrame, nextFrame) > 60)    #checks these many frames per second for difference in image's matrices

    if numpy.all(motionSens > 500):
        picTime=time.time()
        if picTime - prevPicTime > 10:
            if firstDetection:
                playSound(audio)
                firstDetection=False
            img_name = 'Movement was Found{%d}.png' % cnt                       #possible error, replace with 'Movement was Found{}.png'.format(cnt)
            cnt+=1
            prevPicTime = time.time()
            cv2.imwrite(img_name, currentFrame)
            print(img_name + ' was captured')
    nextFrame = currentFrame
            
    cv2.imshow("Hello Sir", currentFrame)
    if cv2.waitKey(1)%256 == 27:                                    #when press Esc key
        capture.release()
        exit()