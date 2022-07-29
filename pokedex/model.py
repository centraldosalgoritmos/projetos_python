# -*- coding: utf-8 -*-

class Pokemon:

    def __init__(self, poke_id, nome, tipos, base_hp, base_atk, base_satk, base_def, base_sdef, base_spd, height, weight):
        self._poke_id = poke_id
        self._nome = nome
        self._tipos = tipos
        self._base_hp = base_hp
        self._base_atk = base_atk
        self._base_satk = base_satk
        self._base_def = base_def
        self._base_sdef = base_sdef
        self._base_spd = base_spd
        self._height = height
        self._weight = weight

    @property
    def poke_id(self):
        return self._poke_id

    @poke_id.setter
    def poke_id(self, value):
        self._poke_id = int(value)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def tipos(self):
        return self._tipos

    @tipos.setter
    def tipos(self, value):
        self._tipos = value

    @property
    def base_hp(self):
        return self._base_hp

    @base_hp.setter
    def base_hp(self, value):
        self._base_hp = value

    @property
    def base_atk(self):
        return self._base_atk

    @base_atk.setter
    def base_atk(self, value):
        self._base_atk = value

    @property
    def base_satk(self):
        return self._base_satk

    @base_satk.setter
    def base_satk(self, value):
        self._base_satk = value

    @property
    def base_def(self):
        return self._base_def

    @base_def.setter
    def base_def(self, value):
        self._base_def = value

    @property
    def base_sdef(self):
        return self._base_sdef

    @base_sdef.setter
    def base_sdef(self, value):
        self._base_sdef = value

    @property
    def base_spd(self):
        return self._base_spd

    @base_spd.setter
    def base_spd(self, value):
        self._base_spd = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


class PokemonParser:

    @staticmethod
    def parse_pokemon(pokemon_data):
        base_stats = {x['stat']['name']: x['base_stat'] for x in pokemon_data['stats']}
        height = round(pokemon_data['height'] * 10, 1)
        weight = round(pokemon_data['weight'] * 0.1, 1)
        return Pokemon(
            pokemon_data['id'],
            pokemon_data['name'],
            [t['type']['name'] for t in pokemon_data['types']],
            base_stats['hp'],
            base_stats['attack'],
            base_stats['special-attack'],
            base_stats['defense'],
            base_stats['special-defense'],
            base_stats['speed'],
            height,
           weight
        )
