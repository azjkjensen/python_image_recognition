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
            #print mean(pixel)
            newP = []
            for p in pixel:
              newP.append(int(p))
            avgNum = mean((newP))
            balanceArray.append(avgNum)
    for n in balanceArray:
        total += n
    balance=total/len(balanceArray)

    #Iterate through each pixel again and reassign new values to either black or white accordingly
    for rows in newArray:
        for pixel in rows:
            if mean(newP) < balance:
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
    matchedArray = []
    loadExamples = open('numArEx.txt', 'r').read() #load all examples from our txt file
    loadExamples = loadExamples.split('\n') #split each file into its own object

    i = Image.open(filePath) #Open the file in question
    iar = np.array(i) #Same as before, create an array of the image
    iarl = iar.tolist() #Create a list from the array so we can change it to a string

    inQuestion = str(iarl) #Change the list to a string for manipulation (split())

    #Iterate through each example to compare it to the image in question
    for example in loadExamples:
        if len(example) > 3: #This if statement just prevents us from trying to use the eof line or any other mistake line
                             #in the txt file
            splitEx = example.split('::') #Split our examples to extract the data for use
            curNum = splitEx[0] #The number of the example
            curArray = splitEx[1] #The data contained in the example

            pixel = curArray.split('],') #Split the array into pixels

            pixelInQuestion = inQuestion.split('],') #split the image in question into pixels

            x = 0
            #iterate through the length of each pixel
            while (x < len(pixel)):
                #if both pixels are dark or light, add a count to the matched array
                if(pixel[x] == pixelInQuestion[x]):
                    matchedArray.append(int(curNum))
                x += 1

    # print matchedArray
    x = Counter(matchedArray)
    print x #For testing. Prints the array to tell us how many of each number were found
    winner = 0

    #iterate through all of the possible numbers 0-9 to determine the most likely winner
    for number in x:
        # print x[number]
        # print winner

        #determine the winner based on the largest count
        if x[number] > x[winner]:
            winner = number
    return winner #return the number with the highest count 
