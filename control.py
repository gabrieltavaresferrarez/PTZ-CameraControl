import time

import customtkinter as ctk
import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkOptionMenu, CTkEntry, CTkRadioButton, CTkSegmentedButton, CTkSlider, CTkFont, CTkCheckBox, CTkInputDialog

from Teclado import Teclado
from cenas import Cenas
from camera import Camera
from velocidades import Velocidades


class Control(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.cam = None

        self.title("PTZ Camera Control")
        self.geometry(f"{600}x{700}")
        self.minsize(600, 700)
        self.maxsize(800, 800)
        
        self.grid_columnconfigure(0, minsize = 300)
        self.grid_columnconfigure((0, 1), weight = 50)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 10)
        self.grid_rowconfigure((0,1), minsize = 50)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bool_open = True


        # Frame de busca de câmera --------------------------------------------------------------
        self.frame_SearchCamera = CTkFrame(self, corner_radius=0, height=50, width = 900)
        self.frame_SearchCamera.grid_rowconfigure(0, weight = 1)
        self.frame_SearchCamera.grid_columnconfigure((0,1,2,3), weight = 1)
        self.frame_SearchCamera.grid(row = 0, column=0, columnspan=3, stick='nswe')
        self.label_IpCamera = CTkLabel(self.frame_SearchCamera, text='IP Câmera:', anchor='e')
        self.label_IpCamera.grid(row=0, column = 0, padx = (20,5), pady= 10, stick='we')
        self.entry_IpCamera = CTkEntry(self.frame_SearchCamera, width = 150, placeholder_text = '111.111.111.111')
        self.entry_IpCamera.insert(0, '192.168.15.180') # default IP
        self.entry_IpCamera.grid(row = 0, column = 1, padx = (5,20), pady= 10, stick='we')
        self.button_SearchCamera = CTkButton(self.frame_SearchCamera, text='Search Cam', command=self.search_cam)
        self.button_SearchCamera.grid(row = 0, column = 2, padx = 20, pady= 10, stick='we')


        # Frame de controle manual --------------------------------------------------------------
        self.frame_ManualControl = CTkFrame(self)
        self.frame_ManualControl.grid(row = 1, column = 0, stick='nswe', padx=5, pady = 5)
        self.frame_ManualControl.grid_rowconfigure((0,1,2,3,4), weight = 1)
        self.frame_ManualControl.grid_columnconfigure(0, weight = 1)
        padx_ManualControl = 20
        pady_ManualControl = 5

        # Título
        self.label_ModoManual = CTkLabel(self.frame_ManualControl, text='Modo Manual', font=ctk.CTkFont(size=20, weight='bold'))
        self.label_ModoManual.grid(row=0, column=0, pady=pady_ManualControl, padx=padx_ManualControl, stick='nsew')

        # modo Duro vs Natural
        self.segmentedButton_DuroNatural = CTkSegmentedButton(master=self.frame_ManualControl, command=self.teste_func_1)
        self.segmentedButton_DuroNatural.grid(row=1, column=0, padx=padx_ManualControl, pady=pady_ManualControl, stick='nswe')
        self.segmentedButton_DuroNatural.configure(values=["Duro", "Natural"])
        self.segmentedButton_DuroNatural.set("Duro")

        # Teclado
        self.frame_Teclado = Teclado(self.frame_ManualControl, self.func_teclado_dir_press, self.func_teclado_dir_release, self.teclado_zoom_press, self.teclado_zoom_release, self.teclado_focus_press, self.teclado_focus_release)
        self.frame_Teclado.grid(row=2, column=0, pady=pady_ManualControl, padx=padx_ManualControl, stick='nsew')


        self.frame_velocidades = Velocidades(self.frame_ManualControl, title='Velocidade Manual') 
        self.frame_velocidades.grid(row=3, column = 0, stick='nsew', padx=padx_ManualControl, pady=pady_ManualControl)

        # Simulação de mão
        self.checkbox_ModoMao = CTkCheckBox(self.frame_ManualControl, text='Simulação de Mão', command=self.get_size)
        self.checkbox_ModoMao.grid(row=4, column = 0, stick='nswe', padx=padx_ManualControl, pady=pady_ManualControl)

        # Frame de controle automático --------------------------------------------------------------
        self.frame_AutomaticControl = CTkFrame(self)
        self.frame_AutomaticControl.grid(row = 1, column = 1, stick='nswe', padx=5, pady = 5)
        self.frame_AutomaticControl.grid_rowconfigure((0,1,2), weight = 1)
        self.frame_AutomaticControl.grid_columnconfigure(0, weight = 1)
        padx_AutomaticControl = 20
        pady_AutomaticControl = 5

        self.label_ModoAuto =  CTkLabel(self.frame_AutomaticControl, text='Modo Automático', font=CTkFont(weight='bold', size=20))
        self.label_ModoAuto.grid(row=0, column=0, padx=padx_AutomaticControl, pady=pady_AutomaticControl, stick='nsew')

        self.frame_Cenas = Cenas(self.frame_AutomaticControl, self.get_cam_position, self.set_cam_position, num_cenas=6)
        self.frame_Cenas.grid(row=1, column=0, padx=padx_AutomaticControl, pady=pady_AutomaticControl, stick='nsew')

        # Velocidades
        self.frame_VelocidadesCenas = Velocidades(self.frame_AutomaticControl, title='Velocidade Cenas')
        self.frame_VelocidadesCenas.grid(row=2, column=0, padx=padx_AutomaticControl, pady=pady_AutomaticControl)


    def func_teclado_dir_press(self, botao):
        if self.cam:
            if botao == [0,0]:
                self.cam.stop()
            if self.segmentedButton_DuroNatural.get() == 'Duro':
                self.cam.vel_x = botao[0] * self.frame_velocidades.velPanTilt*24
                self.cam.vel_y = botao[1] * self.frame_velocidades.velPanTilt*24
                self.cam.acceleration_x = 0
                self.cam.acceleration_y = 0
                self.cam.vel_max = self.frame_velocidades.velMax
            if self.segmentedButton_DuroNatural.get() == 'Natural':
                self.cam.breaking = 0.0
                self.cam.vel_x = botao[0] # força o movimento a começar
                self.cam.vel_y = botao[1] # força o movimento a começar
                
                self.cam.acceleration_x = botao[0] * self.frame_velocidades.velPanTilt
                self.cam.acceleration_y = botao[1] * self.frame_velocidades.velPanTilt
                self.cam.vel_max = self.frame_velocidades.velMax
        else:
            print('Não há câmera configurada')

    def func_teclado_dir_release(self, botao):
        if self.cam:
            if self.segmentedButton_DuroNatural.get() == 'Duro':
                self.cam.vel_x = 0.0
                self.cam.vel_y = 0.0
            if self.segmentedButton_DuroNatural.get() == 'Natural':
                self.cam.acceleration_x = 0.0
                self.cam.acceleration_y = 0.0
                if self.cam.breaking == 0 :
                    self.cam.breaking = self.frame_velocidades.velPanTilt
        else:
            print('Não há câmera configurada')

    def teclado_zoom_press(self, valor):
        if self.cam:
            if self.segmentedButton_DuroNatural.get() == 'Duro':
                self.cam.vel_zoom = valor*self.frame_velocidades.velZoom
            if self.segmentedButton_DuroNatural.get() == 'Natural':
                self.cam.vel_zoom = valor*0.15 # força o movimento a começar
                self.cam.acceleration_zoom = valor*self.frame_velocidades.velZoom

    def teclado_zoom_release(self):
        if self.cam:
            if self.segmentedButton_DuroNatural.get() == 'Duro':
                self.cam.vel_zoom = 0
            if self.segmentedButton_DuroNatural.get() == 'Natural':
                self.cam.acceleration_zoom = 0.0
                self.cam.breaking_zoom = self.frame_velocidades.velZoom


    def teclado_focus_press(self):
        self.cam.cam.set_focus_mode('one push trigger')
    def teclado_focus_release(self):
        pass

    def get_cam_position(self):
        if self.cam:
            return self.cam.pos
    
    def set_cam_position(self, x, y, zoom):
        if self.cam:
            self.cam.stop()
            self.cam.load_position(x, y, zoom, self.frame_VelocidadesCenas.velPanTilt, self.frame_VelocidadesCenas.velPanTilt, self.frame_VelocidadesCenas.velMax)


    def search_cam(self)->bool:
        string_ip = self.entry_IpCamera.get()
        
        # verification of IP ------
        if len(string_ip) == 0:
            CTkInputDialog(text='[IP Vazio]')
            return False
        
        listString_ipParts = string_ip.split('.')
        if len(listString_ipParts) != 4:
            CTkInputDialog(text='[IP Inválido]')
            return False
        for string_part in listString_ipParts:
            if not(string_part.isnumeric()) or len(string_part) > 3:
                CTkInputDialog(text='[IP Inválido]')
                return False
            if int(string_part) > 255 or int(string_part) < 0:
                CTkInputDialog(text='[IP Inválido]')
                return False
        
        # Connecting to camera
        if self.cam:
            print('Closing Connection with cam')
            self.cam.cam.close_connection()
        print('Starting Connection to cam')
        self.cam = Camera(string_ip)
        try: 
            self.cam.cam.get_pantilt_position()
            print(f'Conectado com {string_ip} com sucesso')
            self.entry_IpCamera.delete(0, tk.END)
        except:
            CTkInputDialog(text='[Conexão Falhou]')
            # self.cam = None
            return False
            


    def teste_func_1(self, valor):
        print(f'test func: {valor}')

    def get_size(self, *args):
        print(f'largura : {self._current_width}')
        print(f'altura : {self._current_height}')
        self.slider_VelGlobal.set(0.5)

    def on_closing(self):
        if self.cam:
            self.cam.stop()
        self.bool_open = False

    def mainloop(self):
        while control.bool_open:
            if control.cam:
                control.cam.update()
            control.update()


if __name__ == '__main__':
    control = Control()
    
    control.mainloop()
    # print(control.frame_Cenas.listFunction_funcoesCenas[0](0))
    # print(control.frame_Cenas.listFunction_funcoesCenas[0](1))
    # print(control.frame_Cenas.listFunction_funcoesCenas[0](2))
    exit(0)
    
        
    