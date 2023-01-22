import cv2
from pyzbar.pyzbar import decode
import webbrowser
from urllib.parse import urlparse

capture = cv2.VideoCapture(0) 
received_data = None

def is_valid_url(data):
    try:
        result = urlparse(data)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

while True:
    _, frame = capture.read() 
    decoded_data = decode(frame)
    try:
        data = decoded_data[0][0] 
        if data != received_data: 
            if is_valid_url(data):
                data_URL = webbrowser.open(data)
                print (data_URL) 
                received_data = data
            else: 
                print (data) 
                received_data = data
    except:
        pass
    cv2.imshow('QR code scanner', frame) 
    key = cv2.waitKey(1) 
    if key == ord('q'):
        break