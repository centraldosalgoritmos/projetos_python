# -*- coding: utf-8 -*-
import tkinter as tk

from random import randint
from tkinter import messagebox


class Jogo:

    __TENTATIVAS_MAX = 5

    def __init__(self, titulo, versao):
        self.titulo = titulo
        self.versao = versao
        self.numero_secreto = None
        self.palpite = None
        self.tentativas = None
        self.ultimos_palpites = []

        self.root = tk.Tk()
        # self.root.option_add('*Dialog.msg.font', 'arial 32')
        self.root.title(string=f'{titulo} v{versao}')
        self.root.option_add("*font", "arial 20")

        self.string_palpite = tk.StringVar(self.root)

        self.frm_iniciar = tk.Frame(master=self.root, relief=tk.FLAT, borderwidth=3, padx=5, pady=5)
        self.frm_iniciar.pack(fill=tk.X, side=tk.TOP)
        self.botao_iniciar = tk.Button(master=self.frm_iniciar, text='INICIAR O JOGO', command=self.novo_jogo)
        self.botao_iniciar.pack(fill=tk.X)

        self.frm_palpite = tk.Frame(master=self.root, relief=tk.GROOVE, borderwidth=7, padx=5, pady=5)
        self.frm_palpite.pack(fill=tk.X)

        self.lbl_palpite = tk.Label(master=self.frm_palpite, text='INSIRA SEU PALPITE ABAIXO: ', anchor='w')
        self.lbl_palpite.pack(fill=tk.Y, side=tk.TOP)

        self.entrada_palpite = tk.Entry(master=self.frm_palpite, width=20, textvariable=self.string_palpite)
        self.entrada_palpite['state'] = 'disabled'
        self.entrada_palpite.pack(fill=tk.Y, side=tk.LEFT)

        self.botao_palpitar = tk.Button(master=self.frm_palpite, text='PALPITAR', command=self.palpitar)
        self.botao_palpitar['state'] = 'disabled'
        self.botao_palpitar.pack(fill=tk.Y, side=tk.RIGHT)

        self.frm_ultimas = tk.Frame(master=self.root, relief=tk.GROOVE, borderwidth=5, padx=5, pady=5)
        self.frm_ultimas.pack(side=tk.BOTTOM, fill=tk.X)

        self.lbl_ult_palpite = tk.Label(master=self.frm_ultimas, text='ÚLTIMOS PALPITES: ', anchor='w')
        self.lbl_ult_palpite.pack(fill=tk.X, side=tk.BOTTOM)

    def iniciar(self):
        self.root.mainloop()

    def novo_jogo(self):
        self.numero_secreto = randint(1, 100)
        self.tentativas = Jogo.__TENTATIVAS_MAX
        self.botao_palpitar['state'] = 'normal'
        self.botao_iniciar['state'] = 'disabled'
        self.entrada_palpite['state'] = 'normal'
        self.entrada_palpite.delete(0, 'end')
        self.lbl_ult_palpite.configure(text='ÚLTIMOS PALPITES: ')
        messagebox.showinfo(title='BOM JOGO!', message=f'O SISTEMA ESCOLHEU UM NÚMERO SECRETO ENTRE 1 E 100!\nVOCÊ TEM {self.tentativas} PARA ACERTÁ-LO.')

    def palpitar(self):
        palpite = int(self.string_palpite.get())
        self.ultimos_palpites.append(str(palpite))
        self.lbl_ult_palpite.configure(text=f"ÚLTIMOS PALPITES {','.join(self.ultimos_palpites)}")
        if palpite == self.numero_secreto:
            self.numero_secreto = None
            self.tentativas = None
            self.palpite = None
            self.botao_palpitar['state'] = 'disabled'
            self.botao_iniciar['state'] = 'normal'
            self.entrada_palpite['state'] = 'disabled'
            messagebox.showinfo(title='PARABÉNS!', message='VOCÊ ACERTOU O NÚMERO SECRETO!')
        else:
            self.tentativas -= 1
            if palpite > self.numero_secreto:
                messagebox.showinfo(title='ERROOOOU!', message=f'SEU PALPITE FOI MAIOR!\nRESTAM {self.tentativas} TENTATIVAS')
            else:
                messagebox.showinfo(title='ERROOOOU!', message=f'SEU PALPITE FOI MENOR!\nRESTAM {self.tentativas} TENTATIVAS')

            if self.tentativas < 1:
                messagebox.showinfo(title='FIM DE JOGO!', message=f'NÃO RESTAM MAIS TENTATIVAS!\nO NÚMERO SECRETO ERA {self.numero_secreto}.')
                self.numero_secreto = None
                self.tentativas = None
                self.palpite = None
                self.ultimos_palpites = []
                self.botao_palpitar['state'] = 'disabled'
                self.botao_iniciar['state'] = 'normal'
                self.entrada_palpite['state'] = 'disabled'
                self.entrada_palpite.delete(0, 'end')
