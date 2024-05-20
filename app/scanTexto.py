import pytesseract as tess
import cv2
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# my_image = Image.open('D:\\PROGRAMMING\\3-Python\\My_Virtual_Envs\\ocr_youtube\\routing.PNG')
my_image = cv2.imread('D:\\python_ScanTexto\\data\\routing.PNG')
txt = tess.image_to_string(my_image)
print(txt)

# Display original image
cv2.imshow('Image', my_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

my_file = open('file1.txt', 'w')
my_file.write(txt + '\n')
my_file.close()

output = tess.image_path('text_result.txt')
