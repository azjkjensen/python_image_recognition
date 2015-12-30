import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from statistics import mean
from collections import Counter
import time
import uuid

# Creates a text file with a list of our example files to compare the image in question with. Each line will contain
# one image file
def createExamples():
    numberArrayExamples = open('numArEx.txt','a')#Open the file to enter a list from our data
    numbersWeHave = range(0,10) #Set up to recognize numbers 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9
    versionsWeHave = range(1,10)#This is for the given data, we have 10 examples of each number
    #iterate through all versions of each number
    for number in numbersWeHave:
        for version in versionsWeHave:
            # print str(number) + '.' + str(version) #for testing - prints each version being checked
            imgFilePath = 'images/numbers/' + str(number) + '.' + str(version) + '.png' #filepath for each image to compare
            ei = Image.open(imgFilePath) #open the given image
            eiArray = np.array(ei) #array of each image
            eiArray1 = str(eiArray.tolist()) #String version of each image, for string manipulation (split())

            lineToWrite = str(number) + '::' + eiArray1 + '\n' #Creates the line to write to our txt file
            numberArrayExamples.write(lineToWrite) #Write the line to the txt file

#Thresholds the image in question by altering all colors to be either black or white
def threshold(imageArray):
    balanceArray = [] #Array containing all averages
    newArray = imageArray #New image because our image array cannot be altered
    total = 0 #total number of pixels, so the average value can be computed correctly

    #iterate through all pixels in the image and compute the average value
    for rows in imageArray:
        for pixel in rows:
            avgNum = mean(pixel)
            balanceArray.append(avgNum)
    for n in balanceArray:
        total += n
    balance=total/len(balanceArray)

    #Iterate through each pixel again and reassign new values to either black or white accordingly
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

#The real workhorse, determines what number the image contains based on the similarities
#to our dataset.
def whatNumIsThis(filePath):
    matchedArray = []#
    loadExamples = open('numArEx.txt', 'r').read()
    loadExamples = loadExamples.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for example in loadExamples:
        if len(example) > 3:
            splitEx = example.split('::')
            curNum = splitEx[0]
            curArray = splitEx[1]

            pixel = curArray.split('],')

            pixelInQuestion = inQuestion.split('],')

            x = 0
            while (x < len(pixel)):
                if(pixel[x] == pixelInQuestion[x]):
                    matchedArray.append(int(curNum))
                x += 1

    # print matchedArray
    x = Counter(matchedArray)
    print x
    winner = 0
    for number in x:
        # print x[number]
        # print winner
        if x[number] > x[winner]:
            winner = number
    isCorrectAnswer = raw_input('is ' + str(winner) + ' the number you drew? ')
    if(isCorrectAnswer == 'yes' or isCorrectAnswer == 'Yes'):
        print 'Hoorah! I\'m learning.'
        i.save('images/learned/'  + str(correctAnswer) + str(uuid.uuid4()), 'png')
    elif (isCorrectAnswer == 'no') or (isCorrectAnswer == 'No'):
        correctAnswer = input('What number did you draw? ')
        i.save('images/learned/' + str(correctAnswer) + str(uuid.uuid4()), 'png')
