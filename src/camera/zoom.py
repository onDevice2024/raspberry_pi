from picamera2 import Picamera2

def set_zoom(picam2:Picamera2, zoom_factor:float):
  if zoom_factor < 1.0:
    raise ValueError("Zoom factor must be >= 1.0")
  full_res = picam2.camera_properties['PixelArraySize']
  size = [int(d / zoom_factor) for d in full_res]
  offset = [(r - s) // 2 for r, s in zip(full_res, size)]
  picam2.set_controls({"ScalerCrop": offset + size})
  
if __name__ == "__main__":
  from capture import test_capture
  picam2 = Picamera2()
  set_zoom(picam2, 2.0)
  test_capture(picam2)