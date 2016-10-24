import StringIO
import subprocess
import os
import time
from playsound import playsound
from datetime import datetime
from PIL import Image

sensitivity = 60000
evenCapture = False

pixels1 = None
pixels2 = None

def getFrame():
    command = "sudo fswebcam output.png"
    imageData = StringIO.StringIO()
    imageData.write(subprocess.check_output(command, shell=True))

while (True):
    getFrame()

    if (evenCapture is False):
        im1 = Image.open("output.png")
        pixels1 = list(im1.getdata())
    elif (evenCapture is True):
        im2 = Image.open("output.png")
        pixels2 = list(im2.getdata())

    # Count changed pixels
    changedPixels = 0
    print(len(pixels1))
    if (pixels1 is not None and pixels2 is not None): 
        for i in range(len(pixels1)):
            if (abs(sum(pixels1[i]) - sum(pixels2[i])) > 8):
                changedPixels = changedPixels + 1

    	if (changedPixels > sensitivity):
            subprocess.call(["aplay", "sound.wav"])    

    time.sleep(.5)
    evenCapture =  not evenCapture
