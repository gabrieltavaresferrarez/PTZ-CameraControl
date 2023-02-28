import customtkinter as ctk
import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkOptionMenu, CTkEntry, CTkRadioButton, CTkSegmentedButton, CTkSlider, CTkFont, CTkCheckBox, CTkInputDialog


def limits(value, min_value, max_value):
    if value > max_value:
        return max_value
    if value < min_value:
        return  min_value
    return value

class Velocidades(CTkFrame):
    def __init__(self, master, title = 'Velocidade', global_index : int = False):
        super().__init__(master)

        int_padX = 5
        int_padY = 5
        string_stickSlider = 'ns'
        string_stickLabels = 'nswe'
        font_Value = CTkFont(size=8)
        font_Labels = CTkFont(size=10)
        
        self.grid_rowconfigure((0,1,2,3), weight = 1)
        self.grid_columnconfigure((0, 1, 2), weight = 1)

        self.label_Titulo = CTkLabel(self, text=title, font=CTkFont(size=15, weight='bold'))
        self.label_Titulo.grid(row=0, column=0, columnspan=3, padx=int_padX, pady=int_padY)

        vel_max = 10.0
        self.label_VelMax = CTkLabel(self, text='Velocidade\nMax', font= font_Labels)
        self.label_VelMax.grid(row=1, column=0, stick=string_stickLabels, padx=int_padX, pady=int_padY)
        self.slider_VelMax = CTkSlider(self, orientation='vertical', number_of_steps = vel_max-1, from_=1, to=vel_max, command=self.changeVelMax)
        self.slider_VelMax.grid(row=2, column=0, stick=string_stickSlider)
        self.label_VelMaxValue = CTkLabel(self, text=f'{vel_max/2}', font = font_Value)
        self.label_VelMaxValue.grid(row=3, column=0, padx=int_padX, pady=int_padY)
        # self.label_VelGlobal = CTkLabel(self, text='Velocidade\nGlobal', font= font_Labels)
        # self.label_VelGlobal.grid(row=1, column=0, stick=string_stickLabels, padx=int_padX, pady=int_padY)
        # self.slider_VelGlobal = CTkSlider(self, orientation='vertical', command=self.changeVelGlobal)
        # self.slider_VelGlobal.grid(row=2, column=0, stick=string_stickSlider)
        # self.label_VelGlobalValue = CTkLabel(self, text='0.5', font = font_Value)
        # self.label_VelGlobalValue.grid(row=3, column=0, padx=int_padX, pady=int_padY)

        self.label_VelPanTilt = CTkLabel(self, text='Velocidade\nPan/Tilt', font= font_Labels)
        self.label_VelPanTilt.grid(row=1, column=1, stick=string_stickLabels, padx=int_padX, pady=int_padY)
        self.slider_VelPanTilt = CTkSlider(self, orientation='vertical', command=self.changeVelPanTilt)
        self.slider_VelPanTilt.grid(row=2, column=1, stick=string_stickSlider)
        self.label_VelPanTiltValue = CTkLabel(self, text='0.5', font = font_Value)
        self.label_VelPanTiltValue.grid(row=3, column=1, padx=int_padX, pady=int_padY)

        self.label_VelZoom = CTkLabel(self, text='Velocidade\nZoom', font= font_Labels)
        self.label_VelZoom.grid(row=1, column=2, stick=string_stickLabels, padx=int_padX, pady=int_padY)
        self.slider_VelZoom = CTkSlider(self, orientation='vertical', command=self.changeVelZoom)
        self.slider_VelZoom.grid(row=2, column=2, stick=string_stickSlider)
        self.label_VelZoomValue = CTkLabel(self, text='0.5', font = font_Value)
        self.label_VelZoomValue.grid(row=3, column=2, padx=int_padX, pady=int_padY)
        

    def changeVelGlobal(self, valor):
        self.label_VelGlobalValue.configure(text=f'{valor:.2f}')
        self.slider_VelGlobal.set(valor)
        self.changeVelPanTilt(valor)
        self.changeVelZoom(valor)
    def changeVelPanTilt(self, valor):
        self.slider_VelPanTilt.set(valor)
        self.label_VelPanTiltValue.configure(text=f'{valor:.2f}')
    def changeVelZoom(self, valor):
        self.slider_VelZoom.set(valor)
        self.label_VelZoomValue.configure(text=f'{valor:.2f}')
    def changeVelMax(self, valor):
        self.slider_VelMax.set(valor)
        self.label_VelMaxValue.configure(text=f'{valor:.2f}')

    
    @property
    def velGlobal(self):
        return self.slider_VelGlobal.get()
    @velGlobal.setter
    def velGlobal(self, value : float):
        self.changeVelGlobal(limits(value, 0.0, 1.0))
    
    @property
    def velMax(self):
        return self.slider_VelMax.get()
    @velMax.setter
    def velMax(self, value : float):
        self.changeVelMax(limits(value, 1, 24))
    
    @property
    def velPanTilt(self):
        return self.slider_VelPanTilt.get()
    @velPanTilt.setter
    def velPanTilt(self, value : float):
        self.changeVelPanTilt(limits(value, 0.0, 1.0))
    
    @property
    def velZoom(self):
        return self.slider_VelZoom.get()
    @velZoom.setter
    def velZoom(self, value : float):
        self.changeVelZoom(limits(value, 0.0, 1.0))

