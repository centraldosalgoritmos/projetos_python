import tkinter as tk
import urllib.request
import io

from tkinter import Tk, messagebox
from tkinter import ttk

from PIL import Image, ImageTk

from apiclient import PokeAPIClient
from model import PokemonParser


class PokedexUI(Tk):

    _POKEMON_ID = 1

    def __init__(self, title, width, height):
        super().__init__()
        self.title(title)
        self.frame_width = width
        self.frame_height = height
        self.geometry(f'{width}x{height}')
        self.configure(bg=PokedexDefaultStyle.BACKGROUND_COLOR)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.wm_attributes('-transparentcolor', 'grey')

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('pokemon.frame.TFrame', background=PokedexDefaultStyle.TYPE_GRASS_COLOR)
        self.style.configure('pokemon.image.TLabel', background=PokedexDefaultStyle.TYPE_GRASS_COLOR)
        self.style.configure('pokemon.entry.TEntry', foreground=PokedexDefaultStyle.HEADER_COLOR, fieldbackground=PokedexDefaultStyle.TYPE_GRASS_COLOR, borderwidth=1, relief='flat', width=200, height=10, justify='center', font=('Verdana', 40))
        self.style.configure('pokemon.nav.TButton', foreground=PokedexDefaultStyle.HEADER_COLOR, background=PokedexDefaultStyle.TYPE_GRASS_COLOR, activebackgroun=PokedexDefaultStyle.TYPE_GRASS_COLOR, font=('Showcard Gothic', 18), width=3, height=5)
        self.style.configure('pokemon.name.TLabel', foreground=PokedexDefaultStyle.HEADER_COLOR, background=PokedexDefaultStyle.BACKGROUND_COLOR, font=('Showcard Gothic', 28))
        self.style.configure('pokemon.id.TLabel', foreground=PokedexDefaultStyle.HEADER_COLOR, background=PokedexDefaultStyle.TYPE_GRASS_COLOR, font=('Showcard Gothic', 20))
        self.style.configure('pokemon.type1.TLabel', foreground=PokedexDefaultStyle.HEADER_COLOR, background=PokedexDefaultStyle.BACKGROUND_COLOR, font=('Showcard Gothic', 18))
        self.style.configure('pokemon.type2.TLabel', foreground=PokedexDefaultStyle.HEADER_COLOR, background=PokedexDefaultStyle.BACKGROUND_COLOR, font=('Showcard Gothic', 18))
        self.style.configure('pokemon.measures.TLabel', foreground=PokedexDefaultStyle.HEADER_COLOR, background=PokedexDefaultStyle.BACKGROUND_COLOR, font=('Verdana', 16))
        self.style.configure('pokemon.status.TLabel', foreground=PokedexDefaultStyle.TEXT_COLOR, background=PokedexDefaultStyle.BACKGROUND_COLOR, font=('Verdana', 12))
        self.style.configure('hp.Horizontal.TProgressbar', foreground=PokedexDefaultStyle.BAR_HP_COLOR, background=PokedexDefaultStyle.BAR_HP_COLOR)
        self.style.configure('atk.Horizontal.TProgressbar', foreground=PokedexDefaultStyle.BAR_ATK_COLOR, background=PokedexDefaultStyle.BAR_ATK_COLOR)
        self.style.configure('def.Horizontal.TProgressbar', foreground=PokedexDefaultStyle.BAR_DEF_COLOR, background=PokedexDefaultStyle.BAR_DEF_COLOR)
        self.style.configure('spd.Horizontal.TProgressbar', foreground=PokedexDefaultStyle.BAR_SPD_COLOR, background=PokedexDefaultStyle.BAR_SPD_COLOR)

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=0, columnspan=1, ipadx=width//2)

        # poke image
        self.frame_poke_image = ttk.Frame(self, width=width, height=height * 0.40, relief=tk.FLAT, style='pokemon.frame.TFrame')
        self.frame_poke_image.grid(row=1, columns=1)
        self.frame_poke_image.update()

        with urllib.request.urlopen(r'https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png') as u:
            raw_data = u.read()
        self.image_raw = Image.open(io.BytesIO(raw_data))
        self.image_raw = self.image_raw.resize((220, 220))
        self.image = ImageTk.PhotoImage(self.image_raw)
        self.label_image = ttk.Label(self.frame_poke_image, style='pokemon.image.TLabel', image=self.image)
        self.label_image.place(x=width//2, y=180, anchor=tk.CENTER)
        self.label_image.update()
        self.frame_poke_image.update()

        frame_height = self.frame_poke_image.winfo_height()

        # poke id
        self.poke_id = ttk.Label(self, text='[#000]', style='pokemon.id.TLabel', relief=tk.FLAT)
        self.poke_id.place(x=width-15, y=frame_height-45, anchor='ne')

        # poke name
        self.poke_name = ttk.Label(self, text='[Name]', style='pokemon.name.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        self.poke_name.place(x=width//2, y=frame_height+30, anchor=tk.CENTER)

        # poke type
        self.poke_type1 = ttk.Label(self, text='[Type1]', style='pokemon.type1.TLabel', relief=tk.FLAT, anchor=tk.CENTER, padding=(15, 5, 15, 5))
        self.poke_type1.place(x=(width//2)-100, y=frame_height+90, anchor=tk.CENTER)

        self.poke_type2 = ttk.Label(self, text='[Type2]', style='pokemon.type2.TLabel', relief=tk.FLAT, anchor=tk.CENTER, padding=(15, 5, 15, 5))
        self.poke_type2.place(x=(width//2)+100, y=frame_height + 90, anchor=tk.CENTER)

        # poke weight
        label_weight = ttk.Label(self, text='PESO', style='pokemon.status.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        label_weight.place(x=(width//2) - 75, y=frame_height + 175, anchor=tk.CENTER)
        self.poke_weight = ttk.Label(self, text='[- KG]', style='pokemon.measures.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        self.poke_weight.place(x=(width//2) - 80, y=frame_height + 145, anchor=tk.CENTER)

        # poke height
        label_height = ttk.Label(self, text='ALGURA', style='pokemon.status.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        label_height.place(x=(width // 2) + 80, y=frame_height + 175, anchor=tk.CENTER)
        self.poke_height = ttk.Label(self, text='[- M]', style='pokemon.measures.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        self.poke_height.place(x=(width // 2) + 80, y=frame_height + 145, anchor=tk.CENTER)

        # base stats
        label_bstats = ttk.Label(self, text='STATUS BASE', style='pokemon.measures.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        label_bstats.place(x=(width // 2), y=frame_height + 225, anchor=tk.CENTER)

        # poke hp
        poke_base_hp = ttk.Label(self, text='HP:', style='pokemon.status.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        poke_base_hp.place(x=53, y=frame_height + 260)
        self.poke_base_hp_pb = ttk.Progressbar(self, style='hp.Horizontal.TProgressbar', orient=tk.HORIZONTAL, length=width*0.7, mode='determinate', maximum=260, value=0)
        self.poke_base_hp_pb.place(x=90, y=frame_height + 260)

        # poke atk
        poke_base_atk = ttk.Label(self, text='ATK:', style='pokemon.status.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        poke_base_atk.place(x=43, y=frame_height + 290)
        self.poke_base_atk_pb = ttk.Progressbar(self, style='atk.Horizontal.TProgressbar', orient=tk.HORIZONTAL, length=width * 0.7, mode='determinate', maximum=190, value=0)
        self.poke_base_atk_pb.place(x=90, y=frame_height + 290)

        # poke s atk
        poke_base_satk = ttk.Label(self, text='SATK:', style='pokemon.status.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        poke_base_satk.place(x=33, y=frame_height + 320)
        self.poke_base_satk_pb = ttk.Progressbar(self, style='atk.Horizontal.TProgressbar', orient=tk.HORIZONTAL, length=width * 0.7, mode='determinate', maximum=190, value=0)
        self.poke_base_satk_pb.place(x=90, y=frame_height + 320)

        # poke def
        poke_base_def = ttk.Label(self, text='DEF:', style='pokemon.status.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        poke_base_def.place(x=44, y=frame_height + 350)
        self.poke_base_def_pb = ttk.Progressbar(self, style='def.Horizontal.TProgressbar', orient=tk.HORIZONTAL, length=width * 0.7, mode='determinate', maximum=250, value=0)
        self.poke_base_def_pb.place(x=90, y=frame_height + 350)

        # poke sdef
        poke_base_sdef = ttk.Label(self, text='SDEF:', style='pokemon.status.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        poke_base_sdef.place(x=34, y=frame_height + 380)
        self.poke_base_sdef_pb = ttk.Progressbar(self, style='def.Horizontal.TProgressbar', orient=tk.HORIZONTAL, length=width * 0.7, mode='determinate', maximum=250, value=0)
        self.poke_base_sdef_pb.place(x=90, y=frame_height + 380)

        # poke spd
        poke_base_spd = ttk.Label(self, text='SPD:', style='pokemon.status.TLabel', relief=tk.FLAT, anchor=tk.CENTER)
        poke_base_spd.place(x=43, y=frame_height + 410)
        self.poke_base_sdp_pb = ttk.Progressbar(self, style='spd.Horizontal.TProgressbar', orient=tk.HORIZONTAL, length=width * 0.7, mode='determinate', maximum=210, value=0)
        self.poke_base_sdp_pb.place(x=90, y=frame_height + 410)

        self.search_string = tk.StringVar()
        poke_search = ttk.Entry(self, style='pokemon.entry.TEntry', textvariable=self.search_string, justify=tk.CENTER, font=('Verdana', 20))
        poke_search.place(x=width//2, y=30, anchor='c')
        poke_search.update()

        self.bind('<KeyPress>', self.key_press)
        self.change_pokemon('1')

    def change_pokemon(self, pokemon_id):
        poke_data = PokeAPIClient.get_pokemon_data(pokemon_id)
        pokemon = PokemonParser.parse_pokemon(poke_data)
        self.poke_id['text'] = f'#{pokemon.poke_id:03d}'
        self.poke_name['text'] = pokemon.nome
        self.poke_type1['text'] = pokemon.tipos[0].upper()
        type1_color = PokedexDefaultStyle.get_pokemon_tipo_cor(pokemon.tipos[0].upper())
        self.poke_type1['background'] = type1_color
        self.poke_id['background'] = type1_color
        self.style.configure('pokemon.frame.TFrame', background=type1_color)
        self.style.configure('pokemon.image.TLabel', background=type1_color)
        self.style.configure('pokemon.entry.TEntry', fieldbackground=type1_color)
        if len(pokemon.tipos) > 1:
            self.poke_type2['text'] = pokemon.tipos[1].upper()
            self.poke_type2['background'] = PokedexDefaultStyle.get_pokemon_tipo_cor(pokemon.tipos[1].upper())
        else:
            self.poke_type2['text'] = ''
            self.poke_type2['background'] = PokedexDefaultStyle.BACKGROUND_COLOR
        self.poke_weight['text'] = f'{pokemon.weight} KG'
        self.poke_height['text'] = f'{pokemon.height} CM'
        self.poke_base_hp_pb['value'] = pokemon.base_hp
        self.poke_base_atk_pb['value'] = pokemon.base_atk
        self.poke_base_satk_pb['value'] = pokemon.base_satk
        self.poke_base_def_pb['value'] = pokemon.base_def
        self.poke_base_sdef_pb['value'] = pokemon.base_sdef
        self.poke_base_sdp_pb['value'] = pokemon.base_spd
        self.update_pokemon_image(pokemon.poke_id)
        self._POKEMON_ID = pokemon.poke_id
        self.update_idletasks()

    def update_pokemon_image(self, pokemon_id):
        with urllib.request.urlopen(fr'https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon_id:03d}.png') as u:
            raw_data = u.read()
        self.image_raw.close()
        self.image_raw = Image.open(io.BytesIO(raw_data))
        self.image_raw = self.image_raw.resize((220, 220))
        self.image = ImageTk.PhotoImage(self.image_raw)
        self.label_image['image'] = self.image
        self.label_image.place(x=self.frame_width // 2, y=180, anchor=tk.CENTER)
        self.label_image.update()

    def on_closing(self):
        # if messagebox.askokcancel("SAIR", "Deseja realmente finalizar a aplicação?"):
        self.image_raw.close()
        self.destroy()

    def key_press(self, e):
        if e.keycode == 39:
            self._POKEMON_ID += 1
            if self._POKEMON_ID > 898:
                self._POKEMON_ID = 1
            self.change_pokemon(self._POKEMON_ID)

        if e.keycode == 37:
            self._POKEMON_ID -= 1
            if self._POKEMON_ID < 1:
                self._POKEMON_ID = 898
            self.change_pokemon(self._POKEMON_ID)

        if e.keycode == 13:
            try:
                self.change_pokemon(self.search_string.get().lower())
            except Exception as err:
                messagebox.showinfo('POKEMON NÃO ENCONTRADO', 'NÃO FOI POSSÍVEL ENCONTRAR O POKEMON DESEJADO!\nPOR FAVOR TENTE NOVAMENTE.')


class PokedexDefaultStyle:

    # theme colors
    BACKGROUND_COLOR = '#303132' #dark grey
    TEXT_COLOR = '#dcdfe0' #silver
    HEADER_COLOR = '#ffffff' #white
    BAR_HP_COLOR = '#cd3d48' #red
    BAR_ATK_COLOR = '#ed9a5c' #orange
    BAR_DEF_COLOR = '#057fc8' #blue
    BAR_SPD_COLOR = '#668da0' #grey

    # BRANDS: https://pokemon.gameinfo.io/images/icons-sprite.webp
    TYPE_BUG_COLOR = '#a8b820'  # bug
    TYPE_DARK_COLOR = '#705848'  # dark
    TYPE_DRAGON_COLOR = '#7038f8'  # dragon
    TYPE_ELETRIC_COLOR = '#f8d030'  # eletric
    TYPE_FAIRY_COLOR = '#ee99ac'  # fairy
    TYPE_FIGHTING_COLOR = '#c02038'  # fighting
    TYPE_FIRE_COLOR = '#f08030'  # fire
    TYPE_FLYING_COLOR = '#a890f0'  # flying
    TYPE_GRASS_COLOR = '#78c850' # grass
    TYPE_GHOST_COLOR = '#705898'  # ghost
    TYPE_GROUND_COLOR = '#e0c068'  # ground
    TYPE_ICE_COLOR = '#98d8d8'  # ice
    TYPE_NORMAL_COLOR = '#a8a878'  # normal
    TYPE_POISON_COLOR = '#a040a0'  # poison
    TYPE_PSYCHIC_COLOR = '#f85888'  # psychic
    TYPE_ROCK_COLOR = '#b8a038'  # rock
    TYPE_STEEL_COLOR = '#b8b8d0'  # steel
    TYPE_WATER_COLOR = '#6890f0'  # water

    _POKEMON_TYPE_COLOR_MAP = {
        'BUG': TYPE_BUG_COLOR,
        'DARK': TYPE_DARK_COLOR,
        'DRAGON': TYPE_DRAGON_COLOR,
        'ELECTRIC': TYPE_ELETRIC_COLOR,
        'FAIRY': TYPE_FAIRY_COLOR,
        'FIGHTING': TYPE_FIGHTING_COLOR,
        'FIRE': TYPE_FIRE_COLOR,
        'FLYING': TYPE_FLYING_COLOR,
        'GRASS': TYPE_GRASS_COLOR,
        'GHOST': TYPE_GHOST_COLOR,
        'GROUND': TYPE_GROUND_COLOR,
        'ICE': TYPE_ICE_COLOR,
        'NORMAL': TYPE_NORMAL_COLOR,
        'POISON': TYPE_POISON_COLOR,
        'PSYCHIC': TYPE_PSYCHIC_COLOR,
        'ROCK': TYPE_ROCK_COLOR,
        'STEEL': TYPE_STEEL_COLOR,
        'WATER': TYPE_WATER_COLOR
    }

    @staticmethod
    def get_pokemon_tipo_cor(poke_tipo: str):
        return PokedexDefaultStyle._POKEMON_TYPE_COLOR_MAP.get(poke_tipo)
