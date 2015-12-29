import imageRecognition
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('images/numbers/0.1.png') #Get our image

iArray = np.array(i) #Convert image to an array

plt.imshow(iArray)
# plt.show()

imageRecognition.createExamples()
imageRecognition.threshold(iArray)
plt.imshow(iArray)
# plt.show()

imageRecognition.whatNumIsThis('images/test.png')
