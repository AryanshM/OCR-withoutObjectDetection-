import easyocr
import time

startTime = time.time()
# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'], gpu=True)  # You can specify multiple languages here
middleTime = time.time()

# Load an image from file
image_path = './pan2.jpg'  # Replace 'example_image.jpg' with the path to your image

# Perform OCR on the image
results = reader.readtext(image_path)

# Print the detected text
for text in results:
    print(text[1])
endTime = time.time()

print("Time taken to load Model: "+str(middleTime - startTime))
print("Total Time taken : "+str(endTime - startTime))