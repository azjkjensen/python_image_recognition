import imageRecognition
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('images/numbers/0.1.png') #Get our image

iArray = np.array(i) #Convert image to an array

# plt.imshow(iArray) #For plotting to make sure that we know which image is in question
# plt.show()

imageRecognition.createExamples() #Arrange examples for use
iArray = imageRecognition.threshold(iArray) #Run the image in question through our threshold

# plt.imshow(iArray) #For plotting to make sure that we know which image is in question
# plt.show()

winner = imageRecognition.whatNumIsThis('images/test.png') #Determine which number was drawn

#This wordplay is for determining whether we picked the right number, and
#add the image to the dataset to learn to recognize the numbers better.
isCorrectAnswer = raw_input('is ' + str(winner) + ' the number you drew? ')
if(isCorrectAnswer == 'yes' or isCorrectAnswer == 'Yes'):
    print 'Hoorah! I\'m learning.'
    #Add the image to the dataset with the number drawn represented by the first digit
    #followed by a unique ID.
    i.save('images/learned/'  + str(correctAnswer) + str(uuid.uuid4()), 'png')
elif (isCorrectAnswer == 'no') or (isCorrectAnswer == 'No'):
    correctAnswer = input('What number did you draw? ')
    #Add the image to the dataset with the number drawn represented by the first digit
    #followed by a unique ID.
    i.save('images/learned/' + str(correctAnswer) + str(uuid.uuid4()), 'png')
