# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from PIL import ImageTk

from model import Partida


class JogoDefinicoesEstilo:

    # theme colors
    BACKGROUND_COLOR = '#009f92'
    FRAME_COLOR = '#005366'
    TEXT_COLOR = '#f7e7b3' #silver


class JogoGUI(tk.Tk):

    def __init__(self, title: str, version: str, width: int, height: int):
        super().__init__()
        self.title(string=f'{title} v{version}')
        self.width = width
        self.height = height
        self.resizable(False, False)
        self.geometry(f'{width}x{height}')
        self.configure(bg=JogoDefinicoesEstilo.BACKGROUND_COLOR)

        # style
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('ngg.frame.top.TFrame', background=JogoDefinicoesEstilo.FRAME_COLOR)
        self.style.configure('ngg.frame.bottom.TFrame', background=JogoDefinicoesEstilo.FRAME_COLOR)
        self.style.configure('ngg.frame.bottom.TLabel', background=JogoDefinicoesEstilo.FRAME_COLOR)
        self.style.configure('ngg.heart.TLabel', background=JogoDefinicoesEstilo.FRAME_COLOR)
        self.style.configure('ngg.kicks.TLabel', foreground=JogoDefinicoesEstilo.TEXT_COLOR, background=JogoDefinicoesEstilo.BACKGROUND_COLOR)

        self.string_palpite = tk.StringVar(self)
        self.game = None

        self.frm_top = ttk.Frame(master=self, width=width, height=self.height * 0.1, style='ngg.frame.top.TFrame', relief=tk.FLAT)
        self.frm_top.place(x=0, y=0)
        self.frm_bottom = ttk.Frame(master=self, width=width, height=self.height * 0.2, style='ngg.frame.bottom.TFrame', relief=tk.FLAT)
        self.frm_bottom.place(x=0, y=self.height * 0.8)

        self.image_heart_filled = ImageTk.PhotoImage(file='resources/heart-filled.png')

        self.label_heart1 = ttk.Label(self.frm_top, style='ngg.heart.TLabel', image=self.image_heart_filled)
        self.label_heart2 = ttk.Label(self.frm_top, style='ngg.heart.TLabel', image=self.image_heart_filled)
        self.label_heart3 = ttk.Label(self.frm_top, style='ngg.heart.TLabel', image=self.image_heart_filled)
        self.label_heart4 = ttk.Label(self.frm_top, style='ngg.heart.TLabel', image=self.image_heart_filled)
        self.label_heart5 = ttk.Label(self.frm_top, style='ngg.heart.TLabel', image=self.image_heart_filled)
        self.label_heart6 = ttk.Label(self.frm_top, style='ngg.heart.TLabel', image=self.image_heart_filled)
        self.label_heart7 = ttk.Label(self.frm_top, style='ngg.heart.TLabel', image=self.image_heart_filled)

        self.lifes = []

        self.image_start = ImageTk.PhotoImage(file='resources/start-button.png')
        self.image_stop = ImageTk.PhotoImage(file='resources/stop-button.png')
        self.label_start = ttk.Label(self.frm_bottom, style='ngg.frame.bottom.TLabel', image=self.image_start)
        self.label_start.place(x=(self.width // 2), y=self.height * .1, anchor=tk.CENTER)
        self.label_start.bind("<Button-1>", self.button_action)
        self.label_start.update()

        self.label_kicks = ttk.Label(self, style='ngg.kicks.TLabel', text='', font=('Showcard Gothic', 24))
        self.label_kicks.place(x=45, y=self.height * .1, anchor='n')

        self.ent_palpite = tk.Entry(master=self, width=10, textvariable=self.string_palpite, font=('Helvetica', 32))
        self.ent_palpite['state'] = 'disabled'
        self.ent_palpite.place(x=(self.width // 2), y=self.height * .45, anchor=tk.CENTER)
        self.ent_palpite.bind("<KeyPress>", self.guess_action)

    def initial_state(self):
        self.game = None
        self.label_kicks['text'] = ''
        self.ent_palpite.delete(0, 'end')
        self.ent_palpite['state'] = 'disabled'
        self.label_start['image'] = self.image_start
        self.label_start.focus()
        for life in self.lifes:
            life.place_forget()
        self.lifes = []

    def guess_action(self, e):
        if e.keycode == 13:
            if self.lifes:
                palpite = int(self.string_palpite.get())
                if self.game.palpitar(palpite):
                    messagebox.showinfo(title='PARABÉNS!', message='VOCÊ ACERTOU O NÚMERO SECRETO!')
                    self.initial_state()
                else:
                    life = self.lifes.pop()
                    life.place_forget()
                    self.label_kicks['text'] += f"{self.game.get_dica()}\n"
                    self.ent_palpite.delete(0, 'end')
                    self.ent_palpite.focus()
            else:
                messagebox.showinfo(title='FIM DE JOGO!', message=f'NÃO RESTAM MAIS TENTATIVAS!')
                self.initial_state()

    def button_action(self, e):
        if self.game:
            option = tk.messagebox.askquestion('FINALIZAR PARTIDA', 'VOCÊ REALMENTE DESEJA FINALIZAR ESSA PARTIDA?', icon='question')
            if option == 'yes':
                self.initial_state()
        else:
            self.game = Partida(1, 100, 7)
            self.label_kicks['text'] = ''
            self.ent_palpite['state'] = 'normal'
            self.ent_palpite.focus()
            self.label_start['image'] = self.image_stop

            self.label_heart1.place(x=self.width * 0.95, y=30, anchor=tk.CENTER)
            self.label_heart2.place(x=self.width * .85, y=30, anchor=tk.CENTER)
            self.label_heart3.place(x=self.width * 0.75, y=30, anchor=tk.CENTER)
            self.label_heart4.place(x=self.width * 0.65, y=30, anchor=tk.CENTER)
            self.label_heart5.place(x=self.width * 0.55, y=30, anchor=tk.CENTER)
            self.label_heart6.place(x=self.width * 0.45, y=30, anchor=tk.CENTER)
            self.label_heart7.place(x=self.width * 0.35, y=30, anchor=tk.CENTER)

            self.lifes = [
                self.label_heart1,
                self.label_heart2,
                self.label_heart3,
                self.label_heart4,
                self.label_heart5,
                self.label_heart6,
                self.label_heart7
            ]

            messagebox.showinfo(
                title='BOM JOGO!',
                message=f'O SISTEMA ESCOLHEU UM NÚMERO SECRETO ENTRE {self.game.n_min} E {self.game.n_max}!\nVOCÊ TEM {self.game.n_tentativas} TENTAVIAS PARA ACERTÁ-LO.'
            )
