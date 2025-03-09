print("\t======================={ QR Code Generator }=======================\n")

import qrcode
import cv2

# Function to create QR Code
def generate_qr_code(data, filename='qrcode.png'):
    try:
        img = qrcode.make(data)
        img.save(filename)
        print(f"QR Code saved as '{filename}'")
    except Exception as e:
        print(f"Error generating QR Code: {e}")

# Function to decode QR Code
def decode_qr_code(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Image '{image_path}' not found!")
            return
        
        qr_detector = cv2.QRCodeDetector()
        decoded_text, points, _ = qr_detector.detectAndDecode(image)

        if decoded_text:
            print(f"Decoded QR Code Data: {decoded_text}")
        else:
            print("No QR Code detected in the image.")
    except Exception as e:
        print(f"Error decoding QR Code: {e}")

# Generate QR Code
generate_qr_code('https://www.google.com')

# Decode QR Code
decode_qr_code('qrcode.png')
