from picamera2 import Picamera2
import time
import cv2
import numpy as np

def test_capture(picam2:Picamera2, file_name:str="test_image.jpg"):
  picam2.start()
  picam2.capture_file(file_name)
  picam2.stop()
  
def capture_with_timestamp(picam2:Picamera2, file_name="test_image.jpg"):
  image = picam2.capture_array()
  timestamp = time.strftime("%Y-%m-%d %X")
  
  origin = (10, 30)               # Position of the text (x, y)
  font = cv2.FONT_HERSHEY_SIMPLEX # OpenCV font
  scale = 1                       # Font scale
  colour = (255, 255, 255)        # Text color (white in BGR)
  thickness = 2                   # Text thickness
  
  cv2.putText(image, timestamp, origin, font, scale, colour, thickness)
  cv2.imwrite(file_name, image)

if __name__ == "__main__":
  picam2 = Picamera2()
  test_capture(picam2)