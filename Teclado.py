import customtkinter as ctk
import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkOptionMenu, CTkEntry, CTkRadioButton, CTkSegmentedButton, CTkSlider, CTkFont, CTkCheckBox


class Teclado(CTkFrame):
    def __init__(self, master, func_master_direcional_press, func_master_direcional_release, func_master_zoom_press, func_master_zoom_release, func_master_focus_press, func_master_focus_release ):
        super().__init__(master)

        #função da função pai que será chamada sempre que apertar um botão
        #essa função será chamada com func_master('00')
        self.func_master_direcional_press = func_master_direcional_press 
        self.func_master_direcional_release = func_master_direcional_release 
        self.func_master_zoom_press = func_master_zoom_press 
        self.func_master_zoom_release = func_master_zoom_release 
        self.func_master_focus_press = func_master_focus_press 
        self.func_master_focus_release = func_master_focus_release 

        stick_buttons = 'nswe' ; width_buttons = 60; height_buttons = 40 ; padx_buttons = 2; pady_buttons = 2
        self.grid_rowconfigure((0,1,2), weight = 1)
        self.grid_columnconfigure((0,1,2), weight = 1)
        # self.frame_Teclado.grid(row=2, column=0, pady=pady_ManualControl, padx=padx_ManualControl, stick='nsew')
        self.button_Tec00 = CTkButton(self, text= '↖', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        self.button_Tec00.bind('<ButtonPress-1>',self.func_botao_press_00)
        self.button_Tec00.bind('<ButtonRelease-1>',self.func_botao_release_00)
        self.button_Tec00.grid(row=0, column=0, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)

        self.button_Tec01 = CTkButton(self, text= '↑', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        self.button_Tec01.bind('<ButtonPress-1>',self.func_botao_press_01)
        self.button_Tec01.bind('<ButtonRelease-1>',self.func_botao_release_01)
        self.button_Tec01.grid(row=0, column=1, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)

        self.button_Tec02 = CTkButton(self, text= '↗', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        self.button_Tec02.bind('<ButtonPress-1>',self.func_botao_press_02)
        self.button_Tec02.bind('<ButtonRelease-1>',self.func_botao_release_02)
        self.button_Tec02.grid(row=0, column=2, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)

        self.button_Tec10 = CTkButton(self, text= '←', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        self.button_Tec10.bind('<ButtonPress-1>',self.func_botao_press_10)
        self.button_Tec10.bind('<ButtonRelease-1>',self.func_botao_release_10)
        self.button_Tec10.grid(row=1, column=0, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)
        
        self.button_Tec11 = CTkButton(self, text= 'O', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        self.button_Tec11.bind('<ButtonPress-1>',self.func_botao_press_11)
        self.button_Tec11.bind('<ButtonRelease-1>',self.func_botao_release_11)
        self.button_Tec11.grid(row=1, column=1, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)


        self.button_Tec12 = CTkButton(self, text= '→', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        self.button_Tec12.bind('<ButtonPress-1>',self.func_botao_press_12)
        self.button_Tec12.bind('<ButtonRelease-1>',self.func_botao_release_12)
        self.button_Tec12.grid(row=1, column=2, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)

        self.button_Tec20 = CTkButton(self, text= '↙', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        self.button_Tec20.bind('<ButtonPress-1>',self.func_botao_press_20)
        self.button_Tec20.bind('<ButtonRelease-1>',self.func_botao_release_20)
        self.button_Tec20.grid(row=2, column=0, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)

        self.button_Tec21 = CTkButton(self, text= '↓', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        self.button_Tec21.bind('<ButtonPress-1>',self.func_botao_press_21)
        self.button_Tec21.bind('<ButtonRelease-1>',self.func_botao_release_21)
        self.button_Tec21.grid(row=2, column=1, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)

        self.button_Tec22 = CTkButton(self, text= '↘', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        self.button_Tec22.bind('<ButtonPress-1>',self.func_botao_press_22)
        self.button_Tec22.bind('<ButtonRelease-1>',self.func_botao_release_22)
        self.button_Tec22.grid(row=2, column=2, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)

        self.button_zoomOut = CTkButton(self, text = '-', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        self.button_zoomOut.bind('<ButtonPress-1>',self.func_botao_press_zoomOut)
        self.button_zoomOut.bind('<ButtonRelease-1>',self.func_botao_release_zoomOut)
        self.button_zoomOut.grid(row=3, column=0, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)

        self.button_focusTap = CTkButton(self, text = 'Focus', font=ctk.CTkFont(weight='bold', size=15), width=width_buttons, height=height_buttons)
        self.button_focusTap.grid(row=3, column=1, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)

        self.button_zoomIn = CTkButton(self, text = '+', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        self.button_zoomIn.bind('<ButtonPress-1>',self.func_botao_press_zoomIn)
        self.button_zoomIn.bind('<ButtonRelease-1>',self.func_botao_release_zoomIn)
        self.button_zoomIn.grid(row=3, column=2, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)

#    - 
# -     +
#    +
    def func_botao_press_00(self, event):
        self.func_master_direcional_press([-1,-1])
    def func_botao_release_00(self, event):
        self.func_master_direcional_release([-1,-1])

    def func_botao_press_01(self, event):
        self.func_master_direcional_press([0,-1])
    def func_botao_release_01(self, event):
        self.func_master_direcional_release([0,-1])

    def func_botao_press_02(self, event):
        self.func_master_direcional_press([1,-1])
    def func_botao_release_02(self, event):
        self.func_master_direcional_release([1,-1])

    def func_botao_press_10(self, event):
        self.func_master_direcional_press([-1,0])
    def func_botao_release_10(self, event):
        self.func_master_direcional_release([-1,0])

    def func_botao_press_11(self, event):
        self.func_master_direcional_press([0,0])
    def func_botao_release_11(self, event):
        self.func_master_direcional_release([0,0])
                                 
    def func_botao_press_12(self, event):
        self.func_master_direcional_press([1,0])
    def func_botao_release_12(self, event):
        self.func_master_direcional_release([1,0])

    def func_botao_press_20(self, event):
        self.func_master_direcional_press([-1,1])
    def func_botao_release_20(self, event):
        self.func_master_direcional_release([-1,1])

    def func_botao_press_21(self, event):
        self.func_master_direcional_press([0,1])
    def func_botao_release_21(self, event):
        self.func_master_direcional_release([0,1])
        
    def func_botao_press_22(self, event):
        self.func_master_direcional_press([1,1])
    def func_botao_release_22(self, event):
        self.func_master_direcional_release([1,1])



    def func_botao_press_zoomIn(self, event):
        self.func_master_zoom_press(1)
    def func_botao_release_zoomIn(self, event):
        self.func_master_zoom_release()
    def func_botao_press_zoomOut(self, event):
        self.func_master_zoom_press(-1)
    def func_botao_release_zoomOut(self, event):
        self.func_master_zoom_release()
        


# OLD FUNCTION 
        # stick_buttons = 'nswe' ; width_buttons = 60; height_buttons = 40 ; padx_buttons = 2; pady_buttons = 2
        # self.frame_Teclado = CTkFrame(self.frame_ManualControl)
        # self.frame_Teclado.grid_rowconfigure((0,1,2), weight = 1)
        # self.frame_Teclado.grid_columnconfigure((0,1,2), weight = 1)
        # self.frame_Teclado.grid(row=2, column=0, pady=pady_ManualControl, padx=padx_ManualControl, stick='nsew')
        # self.button_Tec00 = CTkButton(self.frame_Teclado, text= '↖', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        # self.button_Tec00.grid(row=0, column=0, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)
        # self.button_Tec01 = CTkButton(self.frame_Teclado, text= '↑', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        # self.button_Tec01.grid(row=0, column=1, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)
        # self.button_Tec02 = CTkButton(self.frame_Teclado, text= '↗', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        # self.button_Tec02.grid(row=0, column=2, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)
        # self.button_Tec10 = CTkButton(self.frame_Teclado, text= '←', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        # self.button_Tec10.grid(row=1, column=0, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)
        # self.button_Tec12 = CTkButton(self.frame_Teclado, text= '→', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        # self.button_Tec12.grid(row=1, column=2, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)
        # self.button_Tec20 = CTkButton(self.frame_Teclado, text= '↙', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        # self.button_Tec20.grid(row=2, column=0, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)
        # self.button_Tec21 = CTkButton(self.frame_Teclado, text= '↓', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        # self.button_Tec21.grid(row=2, column=1, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)
        # self.button_Tec22 = CTkButton(self.frame_Teclado, text= '↘', font=ctk.CTkFont(weight='bold', size=30), width=width_buttons, height=height_buttons)
        # self.button_Tec22.grid(row=2, column=2, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)