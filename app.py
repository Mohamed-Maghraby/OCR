import pytesseract
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
imgPath = 'folded-image.jpg'

img = cv2.imread(imgPath)
img = cv2.resize(img, None, fx=0.5,fy=0.5)
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(grayImage)
print(text)

cv2.imshow('grayImage',grayImage)
cv2.imshow('img',img)
cv2.waitKey(0)

# myImage = Image
# 
# 
# 
#.open(imgPath)
# myImage.show() 




