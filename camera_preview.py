import customtkinter as ctk
import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkFont, CTkImage, CTkOptionMenu
import cv2 as cv
from PIL import Image
import numpy as np
from customtkinter import CTkFont

from ndicamera import NDICamera

class CameraPreview(CTkFrame):
    def __init__(self, master, size = (426, 240)):
        super().__init__(master)


        self.grid_rowconfigure((0,1,2), weight = 1)
        self.grid_columnconfigure((0,1,2,3), weight = 1)

        self.tupleInt_imageSize = size

        self.camera = None   
        cv_image = cv.imread('camera_preview.png');
        cvImage_gray = cv.cvtColor(cv_image, cv.COLOR_BGR2GRAY)
        image_imagem = Image.fromarray(cvImage_gray)
        self.ctkImage_imagem = CTkImage(image_imagem, size = self.tupleInt_imageSize)

        self.label_title = CTkLabel(self, text='Camera Preview', font=ctk.CTkFont(size=15, weight='bold'))
        self.label_title.grid(row = 0, column= 0, columnspan = 4, padx = 5, pady= 5)

        self.label_imagem = CTkLabel(self, text = '', image=self.ctkImage_imagem, width = self.tupleInt_imageSize[0], height=self.tupleInt_imageSize[1])
        self.label_imagem.grid(row = 1, column= 0, columnspan = 4, padx = 5, pady= 5)

        self.button_searchCamera = CTkButton(self, text='Search', command=self.search_sources)
        self.button_searchCamera.grid(row = 2, column= 0, padx = 5, pady= 5)
        
        self.list_sources = []
        self.optionMenu_sources = CTkOptionMenu(self, dynamic_resizing=False,  values=self.list_sources)
        self.optionMenu_sources.grid(row = 2, column= 1, padx = 5, pady= 5)

        self.button_connectCamera = CTkButton(self, text='Connect', command=self.connect_camera)
        self.button_connectCamera.grid(row = 2, column= 2, padx = 5, pady= 5)
        
        self.button_disconnectCamera = CTkButton(self, text='Disconnect', command=self.disconnect_camera)
        self.button_disconnectCamera.grid(row = 2, column= 3, padx = 5, pady= 5)


        self.init_camera()


    def init_camera(self):
        if not(self.camera):
            self.camera = NDICamera()


    def update_image(self):
        if self.camera.bool_on:
            cvImage, received = self.camera.read()
            if received:
                cvImage_gray = cv.cvtColor(cvImage, cv.COLOR_BGR2GRAY)
                self.show_image(cvImage_gray)
                self.update()
                pass

    def close(self):
        if self.camera.bool_on:
            self.camera.bool_on = False
            self.camera.release()
        
    def show_image(self, cv_image): #recebe uma imagem no formato open cv
        image_imagem = Image.fromarray(cv_image)
        self.ctkImage_imagem = CTkImage(image_imagem, size = self.tupleInt_imageSize)
        self.label_imagem.configure(image=self.ctkImage_imagem)

    def search_sources(self):
        self.list_sources =  self.camera.search_sources()
        print(self.list_sources)
        self.optionMenu_sources.configure(values = self.list_sources)

    def connect_camera(self):
        print(f'Connecting to {self.optionMenu_sources.get()}')
        index_source = self.list_sources.index(self.optionMenu_sources.get())
        try:
            self.camera.connect_sources(index_source)
        except:
            print('ERRO Não encontrou NDI Source')

    def disconnect_camera(self):
        print(f'Disconnecting to {self.optionMenu_sources.get()}')
        if self.camera.bool_on:
            self.camera.bool_on = False
            self.camera.release()
            cv_image = cv.imread('camera_preview.png');
            self.show_image(cv_image)




if __name__ == '__main__':
    app = ctk.CTk()
    frame_cameraPreview = CameraPreview(app)
    frame_cameraPreview.pack()
    while True:
        frame_cameraPreview.update_image()
        app.update()
        