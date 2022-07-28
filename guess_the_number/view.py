# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

from model import Partida


class JogoGUI:

    def __init__(self, titulo, versao):
        self.jogo = None

        self.root = tk.Tk()
        self.root.title(string=f'{titulo} v{versao}')
        self.root.option_add("*font", "arial 20")

        self.string_palpite = tk.StringVar(self.root)

        self.frm_iniciar = tk.Frame(master=self.root, relief=tk.FLAT, borderwidth=3, padx=5, pady=5)
        self.frm_iniciar.pack(fill=tk.X, side=tk.TOP)
        self.btn_iniciar = tk.Button(master=self.frm_iniciar, text='INICIAR O JOGO', command=self.action_novo_jogo)
        self.btn_iniciar.pack(fill=tk.X)

        self.frm_palpitar = tk.Frame(master=self.root, relief=tk.GROOVE, borderwidth=7, padx=5, pady=5)
        self.frm_palpitar.pack(fill=tk.X)
        self.lbl_palpite = tk.Label(master=self.frm_palpitar, text='INSIRA SEU PALPITE ABAIXO: ', anchor='w')
        self.lbl_palpite.pack(fill=tk.Y, side=tk.TOP)
        self.ent_palpite = tk.Entry(master=self.frm_palpitar, width=20, textvariable=self.string_palpite)
        self.ent_palpite['state'] = 'disabled'
        self.ent_palpite.pack(fill=tk.Y, side=tk.LEFT)
        self.btn_palpitar = tk.Button(master=self.frm_palpitar, text='PALPITAR', command=self.action_palpitar)
        self.btn_palpitar['state'] = 'disabled'
        self.btn_palpitar.pack(fill=tk.Y, side=tk.RIGHT)

        self.frm_ultimas = tk.Frame(master=self.root, relief=tk.GROOVE, borderwidth=5, padx=5, pady=5)
        self.frm_ultimas.pack(side=tk.BOTTOM, fill=tk.X)
        self.lbl_ult_palpite = tk.Label(master=self.frm_ultimas, text='ÚLTIMOS PALPITES: ', anchor='w')
        self.lbl_ult_palpite.pack(fill=tk.X, side=tk.BOTTOM)

    def action_novo_jogo(self):
        self.jogo = Partida(1, 100, 7)
        self.btn_palpitar['state'] = 'normal'
        self.btn_iniciar['state'] = 'disabled'
        self.ent_palpite['state'] = 'normal'
        self.ent_palpite.delete(0, 'end')
        self.ent_palpite.focus()
        messagebox.showinfo(
            title='BOM JOGO!',
            message=f'O SISTEMA ESCOLHEU UM NÚMERO SECRETO ENTRE {self.jogo.n_min} E {self.jogo.n_max}!\nVOCÊ TEM {self.jogo.n_tentativas} TENTAVIAS PARA ACERTÁ-LO.'
        )

    def action_palpitar(self):
        palpite = int(self.string_palpite.get())

        if self.jogo.palpitar(palpite):
            messagebox.showinfo(title='PARABÉNS!', message='VOCÊ ACERTOU O NÚMERO SECRETO!')
        else:
            messagebox.showinfo(title='ERROOOOU!', message=f'{self.jogo.get_dica()}\nRESTAM {self.jogo.n_tentativas} TENTATIVAS.')
            self.lbl_ult_palpite.configure(text=f'ÚLTIMOS PALPITES: {self.jogo.palpites}')
            self.ent_palpite.delete(0, 'end')
            self.ent_palpite.focus()

        if self.jogo.fim_partida:
            messagebox.showinfo(title='FIM DE JOGO!', message=f'NÃO RESTAM MAIS TENTATIVAS!')
            self.jogo = None
            self.ent_palpite.delete(0, 'end')
            self.btn_iniciar['state'] = 'normal'
            self.btn_palpitar['state'] = 'disabled'
            self.ent_palpite['state'] = 'disabled'
            self.ent_palpite.delete(0, 'end')
            self.lbl_ult_palpite.configure(text='ÚLTIMOS PALPITES: ')

    def mainloop(self):
        self.root.mainloop()
