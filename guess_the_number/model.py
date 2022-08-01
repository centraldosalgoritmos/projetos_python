# -*- coding: utf-8 -*-
"""
@description Number Guessing Game by O Cara dos Algoritmos @ocaradosalgoritmos
@since 2022-07-28
"""
from random import randint


class Partida:

    def __init__(self, n_min: int, n_max: int, n_tentativas: int):
        self.__n_min = n_min
        self.__n_max = n_max
        self.__n_tentativas = n_tentativas
        self.__numero_secreto = randint(n_min, n_max)
        self.__ultimo_palpite = None

    @property
    def n_min(self):
        return self.__n_min

    @property
    def n_max(self):
        return self.__n_max

    @property
    def n_tentativas(self):
        return self.__n_tentativas

    @property
    def fim_partida(self):
        return self.n_tentativas < 1

    def get_dica(self):
        if self.__ultimo_palpite > self.__numero_secreto:
            return f'<{self.__ultimo_palpite}'
        return f'>{self.__ultimo_palpite}'

    def palpitar(self, palpite: int):
        if self.n_tentativas < 1:
            raise Exception(f'JOGO JÁ FINALIZADO!\nNÃO É POSSÍVEL FAZER MAIS PALPITES.')
        if palpite < self.n_min or palpite > self.n_max:
            raise ValueError(f'PALPITE INVÁLIDO! O PALPITE DEVE ESTAR NO INTERVALO {self.n_min}-{self.n_max}.')

        self.__n_tentativas -= 1
        self.__ultimo_palpite = palpite
        if self.__ultimo_palpite == self.__numero_secreto:
            return True
        return False
