print("\t======================={ QR Code Generator }=======================\n")

# making qrcode
import qrcode
from flask import Flask

img = qrcode.make('https://www.google.com')
img.save('qrcode.png')



# making docode of qrcode
import cv2

# Ensure the image path is correct
image_path = 'qrcode.png'

# Read the image
image = cv2.imread(image_path)
if image is None:
    print(f"Error: Image '{image_path}' not found!")
else:
    # Create QRCodeDetector
    qr_detector = cv2.QRCodeDetector()
    
    # Detect and decode QR code
    decoded_text, points, _ = qr_detector.detectAndDecode(image)
    
    if decoded_text:
        print(f"Decoded QR Code Data: {decoded_text}")
    else:
        print("No QR Code detected in the image.")
