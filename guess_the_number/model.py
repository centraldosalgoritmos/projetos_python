# -*- coding: utf-8 -*-
from random import randint


class Jogo:

    def __init__(self, n_min: int, n_max: int, n_tentativas: int):
        self.__n_min = n_min
        self.__n_max = n_max
        self.__n_tentativas = n_tentativas
        self.__fim_jogo = False
        self.__ultimo_palpite = None
        self.__numero_secreto = randint(n_min, n_max)
        self.__palpites = []

    def get_n_min(self):
        return self.__n_min

    def get_n_max(self):
        return self.__n_max

    def get_n_tentativas(self):
        return self.__n_tentativas

    def get_palpites(self):
        return ','.join(self.__palpites)

    def get_dica(self):
        if self.__ultimo_palpite > self.__numero_secreto:
            return f'SEU PALPITE {self.__ultimo_palpite} FOI MAIOR QUE O NÚMERO SECRETO!'
        return f'SEU PALPITE {self.__ultimo_palpite} FOI MENOR QUE O NÚMERO SECRETO!'

    def is_fim_jogo(self):
        return self.__fim_jogo

    def palpitar(self, palpite: int):
        if palpite < self.get_n_min() or palpite > self.get_n_max():
            raise ValueError(f'PALPITE INVÁLIDO! O PALPITE DEVE ESTAR NO INTERVALO {self.get_n_min()}-{self.get_n_max()}.')

        if not self.is_fim_jogo():
            self.__ultimo_palpite = palpite
            self.__palpites.append(str(palpite))
            self.__n_tentativas -= 1
            if self.__ultimo_palpite == self.__numero_secreto:
                self.__fim_jogo = True
                return True

            if self.__n_tentativas < 1:
                self.__fim_jogo = True
        else:
            raise SystemError(f'JOGO JÁ FINALIZADO!\nNÃO É POSSÍVEL FAZER MAIS PALPITES.')
        return False
