# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

from model import Jogo


class JogoGUI:

    def __init__(self, titulo, versao):
        self.titulo = titulo
        self.versao = versao
        self.jogo = None

        self.root = tk.Tk()
        # self.root.option_add('*Dialog.msg.font', 'arial 32')
        self.root.title(string=f'{titulo} v{versao}')
        self.root.option_add("*font", "arial 20")

        self.string_palpite = tk.StringVar(self.root)

        self.frm_iniciar = tk.Frame(master=self.root, relief=tk.FLAT, borderwidth=3, padx=5, pady=5)
        self.frm_iniciar.pack(fill=tk.X, side=tk.TOP)
        self.botao_iniciar = tk.Button(master=self.frm_iniciar, text='INICIAR O JOGO', command=self.action_novo_jogo)
        self.botao_iniciar.pack(fill=tk.X)

        self.frm_palpite = tk.Frame(master=self.root, relief=tk.GROOVE, borderwidth=7, padx=5, pady=5)
        self.frm_palpite.pack(fill=tk.X)

        self.lbl_palpite = tk.Label(master=self.frm_palpite, text='INSIRA SEU PALPITE ABAIXO: ', anchor='w')
        self.lbl_palpite.pack(fill=tk.Y, side=tk.TOP)

        self.entrada_palpite = tk.Entry(master=self.frm_palpite, width=20, textvariable=self.string_palpite)
        self.entrada_palpite['state'] = 'disabled'
        self.entrada_palpite.pack(fill=tk.Y, side=tk.LEFT)

        self.botao_palpitar = tk.Button(master=self.frm_palpite, text='PALPITAR', command=self.action_palpitar)
        self.botao_palpitar['state'] = 'disabled'
        self.botao_palpitar.pack(fill=tk.Y, side=tk.RIGHT)

        self.frm_ultimas = tk.Frame(master=self.root, relief=tk.GROOVE, borderwidth=5, padx=5, pady=5)
        self.frm_ultimas.pack(side=tk.BOTTOM, fill=tk.X)

        self.lbl_ult_palpite = tk.Label(master=self.frm_ultimas, text='ÚLTIMOS PALPITES: ', anchor='w')
        self.lbl_ult_palpite.pack(fill=tk.X, side=tk.BOTTOM)

    def mainloop(self):
        self.root.mainloop()

    def action_novo_jogo(self):
        self.jogo = Jogo(1, 100, 7)
        self.botao_palpitar['state'] = 'normal'
        self.botao_iniciar['state'] = 'disabled'
        self.entrada_palpite['state'] = 'normal'
        self.entrada_palpite.delete(0, 'end')
        self.entrada_palpite.focus()
        messagebox.showinfo(
            title='BOM JOGO!',
            message=f'O SISTEMA ESCOLHEU UM NÚMERO SECRETO ENTRE {self.jogo.get_n_min()} E {self.jogo.get_n_max()}!\nVOCÊ TEM {self.jogo.get_n_tentativas()} TENTAVIAS PARA ACERTÁ-LO.'
        )

    def action_palpitar(self):
        palpite = int(self.string_palpite.get())

        if self.jogo.palpitar(palpite):
            messagebox.showinfo(title='PARABÉNS!', message='VOCÊ ACERTOU O NÚMERO SECRETO!')
        else:
            messagebox.showinfo(title='ERROOOOU!', message=f'{self.jogo.get_dica()}\nRESTAM {self.jogo.get_n_tentativas()} TENTATIVAS.')
            self.lbl_ult_palpite.configure(text=f'ÚLTIMOS PALPITES: {self.jogo.get_palpites()}')
            self.entrada_palpite.delete(0, 'end')
            self.entrada_palpite.focus()

        if self.jogo.is_fim_jogo():
            self.action_fim_jogo()

    def action_fim_jogo(self):
        messagebox.showinfo(title='FIM DE JOGO!', message=f'NÃO RESTAM MAIS TENTATIVAS!')
        self.jogo = None
        self.entrada_palpite.delete(0, 'end')
        self.botao_iniciar['state'] = 'normal'
        self.botao_palpitar['state'] = 'disabled'
        self.entrada_palpite['state'] = 'disabled'
        self.entrada_palpite.delete(0, 'end')
        self.lbl_ult_palpite.configure(text='ÚLTIMOS PALPITES: ')
