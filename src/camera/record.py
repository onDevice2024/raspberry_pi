import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput, PyavOutput

def test_record(picam2:Picamera2, encoder=None, output=None, file_name:str="test_video.h264"):
  if encoder is None:
    encoder = H264Encoder(10000000)
  
  if output is None:
    output = FileOutput(file_name)
    
  picam2.start_recording(encoder, output)
  time.sleep(5)
  picam2.stop_recording()
  
if __name__ == "__main__":
  picam2 = Picamera2()
  test_record(picam2)