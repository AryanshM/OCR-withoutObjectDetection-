import pytesseract
import cv2
import time


startTime  = time.time()
image = cv2.imread("pan2.jpg")
res = pytesseract.image_to_string(image,lang='hin+eng')
print(res)
endTime = time.time()

print("Total time taken:"+str(endTime - startTime))