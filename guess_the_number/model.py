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
        self.__fim_partida = False
        self.__numero_secreto = randint(n_min, n_max)
        self.__palpites = []

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
        return self.__fim_partida

    @property
    def palpites(self):
        return ','.join([str(x) for x in self.__palpites])

    def get_dica(self):
        if self.__palpites[-1] > self.__numero_secreto:
            return f'SEU PALPITE {self.__palpites[-1]} FOI MAIOR QUE O NÚMERO SECRETO!'
        return f'SEU PALPITE {self.__palpites[-1]} FOI MENOR QUE O NÚMERO SECRETO!'

    def palpitar(self, palpite: int):
        if palpite < self.n_min or palpite > self.n_max:
            raise ValueError(f'PALPITE INVÁLIDO! O PALPITE DEVE ESTAR NO INTERVALO {self.n_min}-{self.n_max}.')

        if not self.fim_partida:
            self.__palpites.append(palpite)
            self.__n_tentativas -= 1
            if self.__palpites[-1] == self.__numero_secreto:
                self.__fim_partida = True
                return True

            if self.n_tentativas < 1:
                self.__fim_partida = True
        else:
            raise Exception(f'JOGO JÁ FINALIZADO!\nNÃO É POSSÍVEL FAZER MAIS PALPITES.')
        return False
