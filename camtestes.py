import time
from visca_over_ip import Camera
# from camera import Camera
import time
import math


if __name__ == '__main__':
    cam = Camera('192.168.15.180')



    # time.sleep(3)

    cam.pantilt(5, 5, pan_position=1000, tilt_position=-1000)
    cam.zoom_to(0)
    time.sleep(2)
    cam.pantilt(0, 0)
    time.sleep(1)
    print(cam.get_pantilt_position())

