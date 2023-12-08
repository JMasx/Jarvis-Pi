#in-system
import os
#import subprocess
import time

#external library
import cv2
import numpy

#unchanging variables
firstDetection=True                                                                                 #boolean flag for first detection of face
cnt=1                                                                                               #initialization for photo count
prevPicTime=0                                                                                       #initialization for time register
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')         #uses pre-saved directory 'data.haarcascades' and a pre-trained model 'haarcascades...xml' to comprehend a typical face structure


#changeable variables
camera = cv2.VideoCapture(0)                                                                        #initialize camera capture to first USB slot
cv2.namedWindow = ('HELLO THERE!')                                                                  #Arbitrary name for camera's window
audio = 'Jarvis.mp3'                                                                                #audio file within local directory, can use full directory path if needed
speakerAddress = "08:EB:ED:DA:7E:5C"                                                                #BlueTooth device address found from other code
photoInterval = 10                                                                                  #changeable interval to take next photo
windowTitle = 'Hello sir!'                                                                          #changeable name for the window that shows camera video feed
#windowsSoundApp = 'Music.UI.exe'
piSoundApp = 'lxmusic'


def playSound(audioFile):                                                                           #function that plays audio files
    try:
        os.system('xdg-open {}'.format(audioFile))                                                   #Raspbian/Linux using default app for sound
        #subprocess.run([piSoundApp, audio])                                                        #Alternative: Specific app for Raspbian/Linux using terminal

        #os.system("start {}".format(audioFile))                                                    #Windows variant for playing audio file using default app
        #subprocess.run(['start', windowsSoundApp, audioFile])                                      #Alternative: Specific app using terminal command

    except Exception as e:                                                                          #necessary for a central system command to run external file
        print('Incorrect formatting for audioFile: {%s}' % e)







while camera.isOpened():
    _, currentFrame = camera.read()                                                                 #initialize the current frame through the camera's read() function
    _, nextFrame = camera.read()                                                                    #initialize the next frame through the camera's read() function
    motionSens=numpy.sum(cv2.absdiff(currentFrame, nextFrame) > 60)                                 #checks these many frames per second for difference in image's matrices


    if numpy.all(motionSens > 500):                                                                 #IF more than 500 pixels in the matric of the image change
        picTime=time.time()                                                                         #Find current time
        faceDetect = face.detectMultiScale(currentFrame)                                            #Attempt to detect a face in this frame
        if len(faceDetect) != 0:                                                                    #IF there was a face detected
            if firstDetection:                                                                      #IF the firstDetection flag is true
                    playSound(audio)                                                                #plays audio using written method
                    firstDetection=False                                                            #turn off first detection flag so audio does not play again
            if picTime - prevPicTime > photoInterval:                                               #IF the last photo was taken more than the assigned interval ago (10 sec in this case)
                frame = 'Face Found{%d}.png'%cnt                                                    #saving the same string as a filename for saving image
                print('Face Found{%d}.png was captured' % cnt)                                      #possible error, replace with 'Movement was Found{}.png'.format(cnt)
                cnt+=1                                                                              #increment everytime this loops (each photo taken)
                prevPicTime = time.time()                                                           #Save time of photograph taken
                cv2.imwrite(frame, currentFrame)                                                    #physically create the .jpg of the file with the same name and save to current directory
    nextFrame = currentFrame                                                                        #typical video structure of changing frames per second, assigning next image frame to current constantly
    cv2.imshow(windowTitle, currentFrame)                                                           #display the frames in a window with the given title
    
    
    
    #Closing the active code.
    if cv2.waitKey(1)%256 == 27:                                                                    #when press Esc key
        camera.release()                                                                            #release access to the USB camera
        os.system('taskkill /f /im {}'.format('Music.UI.exe'))                                      #closes music app default for windows
        os.system('pkill{}'.format('lxmusic'))
        exit()                                                                                      #end the execution of code