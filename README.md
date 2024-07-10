# Saturated-Contrast-Stretching-
Images may appear dull and lifeless, lacking the vibrancy to grab attention. Equally problematic are visuals where key elements blend, creating confusion and hindering the intended message. These limitations can stem from various factors, including a lack of awareness regarding the importance of contrast and saturation, or the technical limitations of image capture and editing tools.
The core problem addressed in this work is the ineffective use of contrast and saturation, resulting in visuals that fail to engage the audience. Washed-out colours and a monotonous tonal range lead to a sense of disinterest, while a lack of clear contrast between elements makes it difficult for viewers to decipher the central message. This can be particularly detrimental in fields like photography, graphic design, user interfaces, and presentations, where visuals play a critical role in communication and persuasion.
The proposed solution lies in a comprehensive understanding and strategic manipulation of contrast and saturation. Contrast refers to the relationship between light and dark areas within an image. By effectively employing contrast techniques, creators can establish a clear hierarchy of elements, guiding the viewer's attention and emphasising the most important aspects of the visual message. Saturation, on the other hand, deals with the intensity of colours. Strategic use of saturation can inject vibrancy and life into an image, making it more visually appealing and memorable.
Technique for improving the contrast of an image by stretching the pixel values to the full range of possible values (0 to 255). The operation works by first finding the minimum and maximum values of the image. The minimum value is used as the lower threshold value and the maximum value is used as the upper threshold value. The pixels that are below the lower threshold value are set to the lower threshold value. The pixels that are above the upper threshold value are set to the upper threshold value. The pixels that are between the lower and upper threshold values are linearly mapped to the range 0 to 255. In this project, the tool that we have used for image processing is OpenCV. It is a open source library which is used to adjust the contrast of the image as well as change the dimensions of the image like stretching it.
Given is the process with which we have implemented OpenCV:

>First of all, it is necessary to import all the libraries as well as the image we will be working on. Using the code
  import cv2
  import numpy as np

> Load the image
  image = cv2.imread('your_image.jpg')

>We will also create a histogram of pixel values in the image, using the code piece 
  plt.hist(img.ravel(), bins=655, range=(1, img.ravel().max()))
