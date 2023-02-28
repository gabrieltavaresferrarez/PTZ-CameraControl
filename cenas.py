import customtkinter as ctk
import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkOptionMenu, CTkEntry, CTkRadioButton, CTkSegmentedButton, CTkSlider, CTkFont, CTkCheckBox, CTkInputDialog
from customtkinter import set_default_color_theme
import codecs

class Cenas(CTkFrame):
    def __init__(self, master, masterFunction_getPosition, masterFunction_loadPosition, num_cenas:int= 8):
        super().__init__(master)
        self.masterFunction_getPosition = masterFunction_getPosition
        self.masterFunction_loadPosition = masterFunction_loadPosition

        self.num_cenas = 16 if num_cenas > 16 else num_cenas #max de 16 cenas
        self.grid_rowconfigure((0,1,2,3), weight = 1)
        self.grid_columnconfigure((0,1), weight = 1)

        self.listDict_cenas = self.load_cenas_from_file()
        self.listFunction_funcoesCenasSelect = [ \
            lambda event : self.select_cena(0), lambda event : self.select_cena(1), lambda event : self.select_cena(2), lambda event : self.select_cena(3), lambda event : self.select_cena(4), \
            lambda event : self.select_cena(5), lambda event : self.select_cena(6), lambda event : self.select_cena(7), lambda event : self.select_cena(8), lambda event : self.select_cena(9), \
            lambda event : self.select_cena(10), lambda event : self.select_cena(11), lambda event : self.select_cena(12), lambda event : self.select_cena(13), lambda event : self.select_cena(14), lambda event : self.select_cena(15)
        ]
        
        # lista de funções que retornam qual cena foi apertada (max -> 16 cenas)
        self.listFunction_funcoesCenasLoad = [ \
            lambda event : self.load_cena(0), lambda event : self.load_cena(1), lambda event : self.load_cena(2), lambda event : self.load_cena(3), lambda event : self.load_cena(4), \
            lambda event : self.load_cena(5), lambda event : self.load_cena(6), lambda event : self.load_cena(7), lambda event : self.load_cena(8), lambda event : self.load_cena(9), \
            lambda event : self.load_cena(10), lambda event : self.load_cena(11), lambda event : self.load_cena(12), lambda event : self.load_cena(13), lambda event : self.load_cena(14), lambda event : self.load_cena(15)
        ]
        self.listButton_Cenas = [None]*self.num_cenas

        self.listDict_cenas = self.load_cenas_from_file()
        self.load_buttons_cenas_from_file()
        self.int_selectedCena = None


        self.button_saveCena = CTkButton(self, text='Save', command=self.save_cena)
        self.button_saveCena.grid(row=self.num_cenas//2+1, column = 0, pady=(10,5))
        self.button_renameCena = CTkButton(self, text='Rename', command=self.rename_cena)
        self.button_renameCena.grid(row=self.num_cenas//2+1, column = 1, pady=(10,5))



    def select_cena(self, int_cena):
        string_defaultBlue = '#3B8ED0'
        string_defaultDarkBlue = '#1F6AA5'
        for i in range(self.num_cenas):
            self.listButton_Cenas[i].configure(fg_color = [string_defaultBlue, string_defaultDarkBlue])

        if self.int_selectedCena != int_cena: # vê se estou selecionando cena
            self.listButton_Cenas[int_cena].configure(fg_color = [string_defaultDarkBlue, string_defaultBlue])
            self.int_selectedCena = int_cena
        else: # está deselecionando a cena
            self.listButton_Cenas[int_cena].configure(fg_color = [string_defaultBlue, string_defaultDarkBlue])
            self.int_selectedCena = None

    def load_cena(self, index):
        int_x = self.listDict_cenas[index]['x']
        int_y = self.listDict_cenas[index]['y']
        float_zoom = self.listDict_cenas[index]['zoom']
        
        self.masterFunction_loadPosition(int_x, int_y, float_zoom)

    def load_cenas_from_file(self, string_fileName = 'cenas.txt'):
        listString_chaves = ['nome', 'x', 'y', 'zoom']
        with codecs.open(string_fileName, "r", encoding='utf-8') as file_cenas:
            listString_cenas = file_cenas.readlines()
            listString_cenas = listString_cenas[1:] # remove primeira linha de descrição do arquivo
            listDict_cenas = []
            for line in listString_cenas:
                listString_parts = line.split(',')
                nome = listString_parts[0].strip()
                x = int(listString_parts[1].strip())
                y = int(listString_parts[2].strip())
                zoom = float(listString_parts[3].strip())
                listDict_cenas.append({'nome':nome, 'x':x, 'y':y, 'zoom':zoom})
        return listDict_cenas

    def load_buttons_cenas_from_file(self):
        stick_buttons = 'nswe' ; width_buttons = 200; height_buttons = 25 ; padx_buttons = 2; pady_buttons = 2
        for i in range(self.num_cenas):
            self.listButton_Cenas[i] = CTkButton(self, text=self.listDict_cenas[i]['nome'], height=height_buttons, width=width_buttons)
            self.listButton_Cenas[i].bind('<Double-Button-1>', self.listFunction_funcoesCenasLoad[i])
            self.listButton_Cenas[i].bind('<Button-1>', self.listFunction_funcoesCenasSelect[i])
            row = i//2
            column=i%2
            self.listButton_Cenas[i].grid(row=row, column=column, padx=padx_buttons, pady=pady_buttons, stick=stick_buttons)



    def save_cena(self):
        if self.int_selectedCena != None:
            listInt_positions = self.masterFunction_getPosition()
            self.listDict_cenas[self.int_selectedCena]['x'] = listInt_positions[0]
            self.listDict_cenas[self.int_selectedCena]['y'] = listInt_positions[1]
            self.listDict_cenas[self.int_selectedCena]['zoom'] = listInt_positions[2]
            print(f'{self.listDict_cenas}')
            self.save_file_cenas()
        pass


    def rename_cena(self):
        if self.int_selectedCena != None:
            dialog = CTkInputDialog()
            string_nomeCena = dialog.get_input()
            self.listButton_Cenas[self.int_selectedCena].configure(text=string_nomeCena)
            self.listDict_cenas[self.int_selectedCena]['nome'] = string_nomeCena
            self.save_file_cenas()



    def save_file_cenas(self, string_fileName = 'cenas.txt'):
        listString_chaves = ['nome', 'x', 'y', 'zoom']
        with codecs.open(string_fileName, "w", encoding='utf-8') as file_cenas:
            file_cenas.write('NOME DA CENA, POSIÇÃO X, POSIÇÃO Y, POSIÇÃO ZOOM\n')
            for i in range(len(self.listDict_cenas)):
                string_nome = self.listDict_cenas[i]['nome']
                string_x = self.listDict_cenas[i]['x']
                string_y = self.listDict_cenas[i]['y']
                string_zoom = self.listDict_cenas[i]['zoom']
                file_cenas.write(f'{string_nome},{string_x},{string_y},{string_zoom}\n')
            self.listDict_cenas