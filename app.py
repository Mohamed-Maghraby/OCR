import pytesseract
from PIL import Image


x = 5
print(x+9)

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

print(pytesseract.image_to_string('image.jpg'))
myImage = Image.open('image.jpg')
myImage.show()  



