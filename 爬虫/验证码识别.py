import image
import pytesseract


vcode=pytesseract.image_to_string(image)    
print(vcode)