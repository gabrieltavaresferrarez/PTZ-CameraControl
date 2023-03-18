import sys
import numpy as np
import cv2 as cv
import NDIlib as ndi
import time


class NDICamera():
    def __init__(self):
        if not ndi.initialize():
            return 0
        self.bool_on = False


    def search_sources(self, num_try = 5):
        self.ndi_find = ndi.find_create_v2()

        if self.ndi_find is None:
            return []

        self.sources = []
        trial = 0
        while  len(self.sources) < 2:
            print('Looking for sources ...')
            time.sleep(0.5)
            ndi.find_wait_for_sources(self.ndi_find, 1000)
            self.sources = ndi.find_get_current_sources(self.ndi_find)
            trial += 1
            if trial == num_try :
                break

        sources_names = []
        for source in self.sources:
            sources_names.append(source.ndi_name)
        
        return sources_names



    def connect_sources(self, int_indexSource):
        if self.bool_on:
            return 0
        
        self.bool_on = True
        if self.ndi_find is None:
            return 0

        ndi_recv_create = ndi.RecvCreateV3()
        ndi_recv_create.color_format = ndi.RECV_COLOR_FORMAT_BGRX_BGRA

        self.ndi_recv = ndi.recv_create_v3(ndi_recv_create)

        if self.ndi_recv is None:
            return 0


        ndi.recv_connect(self.ndi_recv, self.sources[int_indexSource])

        ndi.find_destroy(self.ndi_find)

    def read(self):
        t, v, _, _ = ndi.recv_capture_v2(self.ndi_recv, 5000)
        if t == ndi.FRAME_TYPE_VIDEO:
            # print('Video data received (%dx%d).' % (v.xres, v.yres))
            frame = np.copy(v.data)
            ndi.recv_free_video_v2(self.ndi_recv, v)
            return (frame, True)
        else:
            return (None, False)
        
    
    def release(self):
        ndi.recv_destroy(self.ndi_recv)
        ndi.destroy()

if __name__ == '__main__':
    camera = NDICamera()
    # for i in range(5):
    #     cv_image, received = camera.read()
    #     if received:
    #         cv.imshow('bola', cv_image)
    camera.release()
