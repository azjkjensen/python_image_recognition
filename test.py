import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from statistics import mean
import time

i = Image.open('images/numbers/0.1.png') #Get our image

iArray = np.array(i) #Convert image to an array

plt.imshow(iArray)
# plt.show()

def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(0,10)
    versionsWeHave = range(1,10)
    for number in numbersWeHave:
        for version in versionsWeHave:
            print str(number) + '.' + str(version)
            imgFilePath = 'images/numbers/' + str(number) + '.' + str(version) + '.png'
            ei = Image.open(imgFilePath)
            eiArray = np.array(ei)
            eiArray1 = str(eiArray.tolist())

            lineToWrite = str(number) + '::' + eiArray1 + '\n'
            numberArrayExamples.write(lineToWrite)

def threshold(imageArray):
    balanceArray = []
    newArray = imageArray
    total = 0

    for rows in imageArray:
        for pixel in rows:
            avgNum = mean(pixel)
            balanceArray.append(avgNum)
    for n in balanceArray:
        total += n
    balance=total/len(balanceArray)

    for rows in newArray:
        for pixel in rows:
            if mean(pixel) < balance:
                pixel[0] = 255
                pixel[1] = 255
                pixel[2] = 255
                pixel[3] = 255
            else:
                pixel[0] = 0
                pixel[1] = 0
                pixel[2] = 0
                pixel[3] = 255
    return newArray

def whatNumIsThis(filePath):
    matchedArray = []
    

createExamples()
threshold(iArray)
plt.imshow(iArray)
plt.show()
