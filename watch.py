import subprocess
import os
import time
from datetime import datetime
from PIL import Image

threshold = 10
sensitivity = 60000
evenCapture = False

pixels1 = None
pixels2 = None

def getFrame():
    command = "sudo fswebcam -q output.png"
    subprocess.check_output(command, shell=True)

while (True):
    getFrame()

    if (evenCapture is False):
        im1 = Image.open("output.png")
        pixels1 = list(im1.getdata())
    elif (evenCapture is True):
        im2 = Image.open("output.png")
        pixels2 = list(im2.getdata())
    
    changedPixels= 0
    if (pixels1 is not None and pixels2 is not None): 
        for i in range(len(pixels1)):
            if (abs(sum(pixels1[i]) - sum(pixels2[i])) > 8):
                changedPixels = changedPixels + 1

    	if (changedPixels > sensitivity):
	    print("farting...")
            subprocess.call(["aplay", "fart-1.wav"])    

    time.sleep(.5)
    evenCapture = not evenCapture
