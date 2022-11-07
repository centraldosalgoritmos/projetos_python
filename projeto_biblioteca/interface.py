import calendar
from select import select
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# pip install tkcalendar
import tkcalendar
from controler import EstudanteControler, UsuarioControler
from controler import AutorControler
from controler import LivroControler
from tkinter import messagebox
from modelo import Estudante
from modelo import Autor
from modelo import Livro


class JanelaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Sistema de gerenciamento de biblioteca V1')
        self.configure(background=TemaPadrao.COR_FUNDO_JANELAS)
        # objeto de estilização da interface
        self.estilo = ttk.Style(self)
        self.attributes('-fullscreen', True)

        #full screen
        #screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        #self.geometry(f"{screen_width}x{screen_height}")

        # width x height (comprimento x altura)
        #self.window_width = screen_width
        #self.window_height = screen_height
        # self.resizable(False, False)
        self.barra_status = tk.Label(self, text='Sistema de gerenciamento de biblioteca V1 [Usuário não autenticado]', relief=tk.SUNKEN, font=('Arial', 16))
        self.barra_status.pack(side=tk.BOTTOM, fill=tk.X)

        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        self.menu_principal = tk.Menu(self.menubar)
        self.menu_principal.add_command(label='Logout', command=self.menu_logout_click)
        self.menu_principal.add_command(label='Sair', command=self.menu_sair_click)

        self.menu_cadastro = tk.Menu(self.menubar)
        self.menu_cadastro.add_command(label = 'Cadastro de estudante', command=self.menu_estudanteclick)
        self.menu_cadastro.add_command(label = 'Cadastro de autor', command=self.menu_autorclick)
        self.menu_cadastro.add_command(label = 'Cadastro de livro', command=self.menu_livroclick)

        self.menubar.add_cascade(label='Principal', menu=self.menu_principal)
        self.menubar.add_cascade(label = 'Cadastro', menu=self.menu_cadastro)

        self.login = JanelaLogin(self)
        # TODO manter janela login acima da janela principal até login completo
        self.login.grab_set()
    
    def menu_estudanteclick(self):
        janela = JanelaEstudante(self)
    
    def menu_autorclick(self):
        janela = JanelaAutor(self)

    def menu_livroclick(self):
        janela = JanelaLivro(self)

    def menu_logout_click(self):
        pass

    def menu_sair_click(self):
        self.destroy()

    def efetuar_login(self, usuario):
        self.usuario = usuario
        self.barra_status['text'] = f'Sistema de gerenciamento de biblioteca V1 [{self.usuario}]'


class JanelaLogin(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master = master)
        self.title('Login')
        self.window_width = 300
        self.window_height = 135
        self.geometry(f'{self.window_width}x{self.window_height}')
        self.resizable(False, False)

        self.label_usuario = ttk.Label(self, text='Login: ')
        self.label_usuario.place(x=15, y=15)
        self.label_password = ttk.Label(self, text='Senha: ')
        self.label_password.place(x=15, y=55)

        self.svar_usuario = tk.StringVar()
        self.entry_usuario = ttk.Entry(self, textvariable=self.svar_usuario)
        self.entry_usuario.place(x=100, y=15)
        self.svar_password = tk.StringVar()
        self.entry_password = ttk.Entry(self, textvariable=self.svar_password, show='*')
        self.entry_password.place(x=100, y=55)

        self.button_ok = ttk.Button(self, text='OK', command=self.evento_ok_click)
        self.button_ok.place(x=55, y=90)
        self.button_cancel = ttk.Button(self, text='CANCELAR', command=self.evento_cancel_click)
        self.button_cancel.place(x=175, y=90)

        self.protocol("WM_DELETE_WINDOW", self.evento_cancel_click)

    def evento_ok_click(self):
        nome = self.svar_usuario.get()
        senha = self.svar_password.get()

        if UsuarioControler.validar_login(nome, senha):
            messagebox.showinfo('SUCESSO', 'Login e senha informados estão corretos!')
            self.master.efetuar_login(nome)
            self.destroy()
        else:
            messagebox.showwarning('DADOS INVÁLIDOS', 'Login e senha informados estão incorretos!')

    def evento_cancel_click(self):
        self.destroy()
        self.master.destroy()


class JanelaEstudante(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master = master)
        self.title('Janela Cadastro - Estudante')
        self.configure(background=TemaPadrao.COR_FUNDO_JANELAS)
        self.novo_cadastro = False
        # objeto de estilização da interface
        self.estilo = ttk.Style(self)
        self.estilo.configure(
            'biblioteca.TLabel',
            background=TemaPadrao.COR_FUNDO_JANELAS,
            foreground=TemaPadrao.COR_TEXTO_LABELS
        )

        # full screen
        # screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        # self.geometry(f"{screen_width}x{screen_height}")

        # width x height (comprimento x altura)
        self.window_width = 1050
        self.window_height = 700
        self.geometry(f'{self.window_width}x{self.window_height}')
        self.resizable(False, False)

        self.label_matricula = ttk.Label(self, text='MATRICULA:', style='biblioteca.TLabel')
        self.label_matricula.place(x=25, y=35)
        self.svar_matricula = tk.StringVar()
        self.entry_matricula = ttk.Entry(self, textvariable=self.svar_matricula)
        self.entry_matricula.place(x=135, y=32)

        self.label_nome = ttk.Label(self, text='NOME:', style='biblioteca.TLabel')
        self.label_nome.place(x=62, y=75)
        self.svar_nome = tk.StringVar()
        self.entry_nome = ttk.Entry(self, width=100, textvariable=self.svar_nome)
        self.entry_nome.place(x=135, y=72)

        self.label_cpf = ttk.Label(self, text='CPF:', style='biblioteca.TLabel')
        self.label_cpf.place(x=335, y=35)
        self.svar_cpf = tk.StringVar()
        self.entry_cpf = ttk.Entry(self, width=15, textvariable=self.svar_cpf)
        self.entry_cpf.place(x=395, y=32)

        self.label_sexo  = ttk.Label(self, text='SEXO:', style='biblioteca.TLabel')
        self.label_sexo.place(x=65, y=115)
        self.svar_masculino = tk.StringVar()
        self.check_masculino = tk.Checkbutton(self, text='Masculino', onvalue='M', variable=self.svar_masculino, offvalue=None, state='disabled', command=self.alternar_checkbox_m) 
        self.check_masculino.select()
        self.check_masculino.place(x=132, y=113)
        self.svar_feminino = tk.StringVar()
        self.check_feminino = tk.Checkbutton(self, text='Feminino', onvalue='F', variable=self.svar_feminino, offvalue=None, state='disabled', command=self.alternar_checkbox_f)
        self.check_feminino.deselect()
        self.check_feminino.place(x=132, y=153)
        self.label_dnascimento = ttk.Label(self, text='DATA NASCIMENTO:', style='biblioteca.TLabel')
        self.label_dnascimento.place(x=250, y=115)
        self.dnascimento = tkcalendar.DateEntry(self, selectmode='day', state='disabled')
        self.dnascimento.place(x=410, y=113)

        self.label_escolaridade = ttk.Label(self, text='ESCOLARIDADE:', style='biblioteca.TLabel')
        self.label_escolaridade.place(x=560, y=115)
        self.svar_escolaridade = tk.StringVar()
        self.menu_escolaridade = ttk.Combobox(self, state='disabled', textvariable=self.svar_escolaridade)
        self.menu_escolaridade['values'] = ['Ensino Fundamental', 'Ensino Médio', 'Graduação', 'Mestrado', 'Doutorado']
        self.menu_escolaridade.place(x=680, y=113)

        self.button_novo = ttk.Button(self, text='NOVO', command=self.evento_novo_click)
        self.button_novo.place(x=133, y=215)
        self.button_editar = ttk.Button(self, text='EDITAR', state='disabled', command=self.evento_editar_click)
        self.button_editar.place(x=233, y=215)
        self.button_salvar = ttk.Button(self, text='SALVAR', state='disabled', command=self.evento_salvar_click)
        self.button_salvar.place(x=333, y=215)
        self.button_pesquisar = ttk.Button(self, text='PESQUISAR', command=self.evento_pesquisar_click)
        self.button_pesquisar.place(x=433, y=215)
        self.button_cancelar = ttk.Button(self, text='CANCELAR', state='disabled', command=self.evento_cancelar_click)
        self.button_cancelar.place(x=533, y=215)

    def evento_novo_click(self):
        self.check_masculino['state'] = 'active'
        self.check_feminino['state'] = 'active'
        self.dnascimento['state'] = 'enabled'
        self.menu_escolaridade['state'] = 'enabled'
        self.button_novo['state'] = 'disabled'
        self.button_editar['state'] = 'disabled'
        self.button_salvar['state'] = 'enabled'
        self.button_pesquisar['state'] = 'disabled'
        self.button_cancelar['state'] = 'enabled'
        self.novo_cadastro = True

    def evento_cancelar_click(self):
        self.entry_matricula['state'] = 'enabled'
        self.check_masculino['state'] = 'disabled'
        self.check_feminino['state'] = 'disabled'
        self.dnascimento['state'] = 'disabled'
        self.menu_escolaridade['state'] = 'disabled'
        self.button_novo['state'] = 'enabled'
        self.button_editar['state'] = 'disabled'
        self.button_salvar['state'] = 'disabled'
        self.button_pesquisar['state'] = 'enabled'
        self.button_cancelar['state'] = 'disabled'
        self.svar_matricula.set('')
        self.svar_nome.set('')
        self.svar_cpf.set('')
        self.dnascimento.set_date(None)
        self.check_masculino.deselect()
        self.check_feminino.deselect()
        self.svar_escolaridade.set('')
        self.novo_cadastro = False

    def evento_editar_click(self):
        self.entry_cpf['state'] = 'enabled'
        self.entry_nome['state'] = 'enabled'
        self.check_masculino['state'] = 'active'
        self.check_feminino['state'] = 'active'
        self.dnascimento['state'] = 'enabled'
        self.menu_escolaridade['state'] = 'enabled'
        self.button_novo['state'] = 'disabled'
        self.button_salvar['state'] = 'enabled'
        self.button_pesquisar['state'] = 'disabled'
        self.button_cancelar['state'] = 'enabled'

    def evento_salvar_click(self):
        matricula = self.svar_matricula.get()
        nome = self.svar_nome.get()
        cpf = self.svar_cpf.get()
        sexo = self.svar_masculino.get() or self.svar_feminino.get()
        escolaridade = self.svar_escolaridade.get()
        data_nascimento = self.dnascimento.get_date().strftime('%d/%m/%Y')
        novo_estudante = Estudante(matricula, nome.upper(), cpf, sexo, data_nascimento, escolaridade.upper(), status = True)

        try:
            if self.novo_cadastro:
                EstudanteControler.inserir(novo_estudante)
                messagebox.showinfo('Sucesso', 'Estudante cadastrado com sucesso' )
            else:
                EstudanteControler.atualizar(novo_estudante)
                messagebox.showinfo('Sucesso', 'Registro atualizado com sucesso' )
        except AttributeError as erro:
            messagebox.showerror('Erro no cadastro', str(erro))
        self.evento_cancelar_click()

    def alternar_checkbox_m(self):
        if self.svar_masculino.get() and self.svar_feminino.get():
            self.check_feminino.toggle()

    def alternar_checkbox_f(self):
        if self.svar_feminino.get() and self.svar_masculino.get():
            self.check_masculino.toggle()

    def evento_pesquisar_click(self):
        matricula = self.svar_matricula.get()
        nome = self.svar_nome.get()
        cpf = self.svar_cpf.get()
        
        criterios = dict()
        if len(matricula.strip()) > 0:
            criterios['codigo'] = (matricula,'=')
        if len(nome.strip()) > 0:
            criterios['nome'] = ('%'+nome.upper()+'%','LIKE')
        if len(cpf.strip()) > 0:
            criterios['cpf'] = (cpf,'=')

        estudante = EstudanteControler.pesquisar(criterios)
        if estudante:
            self.entry_matricula['state'] = 'disabled'
            self.entry_cpf['state'] = 'disabled'
            self.entry_nome['state'] = 'disabled'
            self.button_novo['state'] = 'disabled'
            self.button_editar['state'] = 'enabled'
            self.button_salvar['state'] = 'disabled'
            self.button_pesquisar['state'] = 'disabled'
            self.button_cancelar['state'] = 'enabled'
            self.svar_matricula.set(estudante[0])
            self.svar_nome.set(estudante[1])
            self.svar_cpf.set(estudante[2])
            if estudante[3] == 'M':
                self.check_masculino.select()
                self.check_feminino.deselect()
            else:
                self.check_masculino.deselect()
                self.check_feminino.select()
            self.dnascimento.set_date(estudante[4])
            self.svar_escolaridade.set(estudante[5])
        else:
            messagebox.showwarning('Nenhum registro encontrado', 'Não foi encontrado o registro solicitado')
        
            
class TemaPadrao:

    COR_FUNDO_JANELAS = '#1d3344'
    COR_TEXTO_LABELS = '#FFFFFF'


class JanelaAutor(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master = master)
        self.title('Janela Cadastro - Autor')
        self.configure(background=TemaPadrao.COR_FUNDO_JANELAS)
        self.novo_registro = False
        
        # objeto de estilização da interface
        self.estilo = ttk.Style(self)
        self.estilo.configure(
            'biblioteca.TLabel',
            background=TemaPadrao.COR_FUNDO_JANELAS,
            foreground=TemaPadrao.COR_TEXTO_LABELS
        )

        # full screen
        # screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        # self.geometry(f"{screen_width}x{screen_height}")

        # width x height (comprimento x altura)
        self.window_width = 1050
        self.window_height = 700
        self.geometry(f'{self.window_width}x{self.window_height}')
        self.resizable(False, False)

        self.label_matricula = ttk.Label(self, text='MATRICULA:', style='biblioteca.TLabel')
        self.label_matricula.place(x=25, y=35)
        self.svar_matricula = tk.StringVar()
        self.entry_matricula = ttk.Entry(self, textvariable=self.svar_matricula)
        self.entry_matricula.place(x=135, y=32)
        self.entry_matricula['state'] = 'enabled'

        self.label_nome = ttk.Label(self, text='NOME:', style='biblioteca.TLabel')
        self.label_nome.place(x=62, y=75)
        self.svar_nome = tk.StringVar()
        self.entry_nome = ttk.Entry(self, width=100, textvariable=self.svar_nome)
        self.entry_nome.place(x=135, y=72)
        self.entry_nome['state'] = 'enabled'
        
        self.button_novo = ttk.Button(self, text='NOVO', command=self.evento_novo_click)
        self.button_novo.place(x=133, y=215)
        self.button_editar = ttk.Button(self, text='EDITAR', state='disabled',command=self.evento_editar_click)
        self.button_editar.place(x=233, y=215)
        self.button_salvar = ttk.Button(self, text='SALVAR', state='disabled', command=self.evento_salvar_click)
        self.button_salvar.place(x=333, y=215)
        self.button_pesquisar = ttk.Button(self, text='PESQUISAR', command=self.evento_pesquisar_click)
        self.button_pesquisar.place(x=433, y=215)
        self.button_cancelar = ttk.Button(self, text='CANCELAR', state='disabled', command=self.evento_cancelar_click)
        self.button_cancelar.place(x=533, y=215)

    def evento_novo_click(self):
        self.button_novo['state'] = 'disabled'
        self.button_editar['state'] = 'disabled'
        self.button_salvar['state'] = 'enabled'
        self.button_pesquisar['state'] = 'disabled'
        self.button_cancelar['state'] = 'enabled'
        self.entry_nome['state'] = 'enabled'
        self.novo_registro = True

    def evento_cancelar_click(self):
        self.button_novo['state'] = 'enabled'
        self.button_editar['state'] = 'disabled'
        self.button_salvar['state'] = 'disabled'
        self.button_pesquisar['state'] = 'enabled'
        self.button_cancelar['state'] = 'disabled'
        self.svar_matricula.set('')
        self.svar_nome.set('')
        self.entry_nome['state'] = 'enabled'
        self.entry_matricula['state'] = 'enabled'        
        self.novo_registro = False

    def evento_salvar_click(self):
        matricula = self.svar_matricula.get()
        nome = self.svar_nome.get()
        novo_autor = Autor(matricula, nome.upper())
        self.entry_nome['state'] = 'disabled'   
        try:
            if self.novo_registro:
                AutorControler.inserir(novo_autor)
                messagebox.showinfo('Sucesso', 'Autor cadastrado com sucesso' )
            else:
                AutorControler.atualizar(novo_autor)
                messagebox.showinfo('Sucesso', 'Autor atualizado com sucesso')
            self.evento_cancelar_click()
        except AttributeError as erro:
            messagebox.showerror('Erro no cadastro', str(erro))

    def evento_editar_click(self):
        self.entry_nome['state'] = 'enabled'
        self.entry_matricula['state'] = 'enabled'
        self.button_novo['state'] = 'disabled'
        self.button_salvar['state'] = 'enabled'
        self.button_pesquisar['state'] = 'disabled'
        self.button_cancelar['state'] = 'enabled'
        

    def evento_pesquisar_click(self):
        matricula = self.svar_matricula.get()
        nome = self.svar_nome.get()
        
        criterios = dict()
        if len(matricula.strip()) > 0:
            criterios['codigo'] = (matricula,'=')
        if len(nome.strip()) > 0:
            criterios['nome'] = ('%'+nome.upper()+'%','LIKE')

        autor = AutorControler.pesquisar(criterios)
        if autor:
            self.entry_matricula['state'] = 'disabled'
            self.entry_nome['state'] = 'disabled'
            self.button_novo['state'] = 'disabled'
            self.button_editar['state'] = 'enabled'
            self.button_salvar['state'] = 'disabled'
            self.button_pesquisar['state'] = 'disabled'
            self.button_cancelar['state'] = 'enabled'
            self.svar_matricula.set(autor[0])
            self.svar_nome.set(autor[1])
        else:
            messagebox.showwarning('Nenhum registro encontrado', 'Não foi encontrado o registro solicitado')
    

class JanelaLivro(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master = master)
        self.title('Janela Cadastro - Livro')
        self.configure(background=TemaPadrao.COR_FUNDO_JANELAS)
        self.novo_registro = False

        # objeto de estilização da interface
        self.estilo = ttk.Style(self)
        self.estilo.configure(
            'biblioteca.TLabel',
            background=TemaPadrao.COR_FUNDO_JANELAS,
            foreground=TemaPadrao.COR_TEXTO_LABELS
        )

        # full screen
        # screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        # self.geometry(f"{screen_width}x{screen_height}")

        # width x height (comprimento x altura)
        self.window_width = 1050
        self.window_height = 700
        self.geometry(f'{self.window_width}x{self.window_height}')
        self.resizable(False, False)

        self.label_matricula = ttk.Label(self, text='MATRICULA:', style='biblioteca.TLabel')
        self.label_matricula.place(x=25, y=35)
        self.svar_matricula = tk.StringVar()
        self.entry_matricula = ttk.Entry(self, textvariable=self.svar_matricula)
        self.entry_matricula.place(x=135, y=32)

        self.label_isbn = ttk.Label(self, text='ISBN:', style='biblioteca.TLabel')
        self.label_isbn.place(x=62, y=75)
        self.svar_isbn = tk.StringVar()
        self.entry_isbn = ttk.Entry(self, width=20, textvariable=self.svar_isbn)
        self.entry_isbn.place(x=135, y=72)

        self.label_titulo = ttk.Label(self, text='TÍTULO:', style='biblioteca.TLabel')
        self.label_titulo.place(x=62, y=112)
        self.svar_titulo = tk.StringVar()
        self.entry_titulo = ttk.Entry(self, width=100, textvariable=self.svar_titulo)
        self.entry_titulo.place(x=135, y=112)

        self.label_descricao = ttk.Label(self, text='DESCRIÇÃO:', style='biblioteca.TLabel')
        self.label_descricao.place(x=62, y=152)
        self.svar_descricao = tk.StringVar()
        self.entry_descricao = ttk.Entry(self, width=100, textvariable=self.svar_descricao)
        self.entry_descricao.place(x=135, y=152)

        self.label_pagina = ttk.Label(self, text='PÁGINA:', style='biblioteca.TLabel')
        self.label_pagina.place(x=335, y=75)
        self.svar_pagina = tk.StringVar()
        self.entry_pagina = ttk.Entry(self, width=15, textvariable=self.svar_pagina)
        self.entry_pagina.place(x=395, y=72)

        self.label_autor = ttk.Label(self, text='AUTOR:', style='biblioteca.TLabel')
        self.label_autor.place(x=335, y=35)
        self.svar_autor = tk.StringVar()
        self.entry_autor = ttk.Entry(self, width=15, textvariable=self.svar_autor)
        self.entry_autor.place(x=395, y=32)

        self.button_novo = ttk.Button(self, text='NOVO', command=self.evento_novo_click)
        self.button_novo.place(x=133, y=215)
        self.button_editar = ttk.Button(self, text='EDITAR', state='disabled', command=self.evento_editar_click)
        self.button_editar.place(x=233, y=215)
        self.button_salvar = ttk.Button(self, text='SALVAR', state='disabled', command=self.evento_salvar_click)
        self.button_salvar.place(x=333, y=215)
        self.button_pesquisar = ttk.Button(self, text='PESQUISAR', command=self.evento_pesquisar_click)
        self.button_pesquisar.place(x=433, y=215)
        self.button_cancelar = ttk.Button(self, text='CANCELAR', state='disabled', command=self.evento_cancelar_click)
        self.button_cancelar.place(x=533, y=215)

    def evento_novo_click(self):
        self.button_novo['state'] = 'disabled'
        self.button_editar['state'] = 'disabled'
        self.button_salvar['state'] = 'enabled'
        self.button_pesquisar['state'] = 'disabled'
        self.button_cancelar['state'] = 'enabled'
        self.novo_registro = True

    def evento_cancelar_click(self):
        self.button_novo['state'] = 'enabled'
        self.button_editar['state'] = 'disabled'
        self.button_salvar['state'] = 'disabled'
        self.button_pesquisar['state'] = 'enabled'
        self.button_cancelar['state'] = 'disabled'
        self.svar_isbn.set('')
        self.svar_titulo.set('')
        self.svar_descricao.set('')
        self.svar_pagina.set('')
        self.svar_autor.set('')
        self.svar_matricula.set('')
        self.novo_registro = False

    def evento_editar_click(self):
        self.entry_isbn['state'] = 'enabled'
        self.entry_titulo['state'] = 'enabled'
        self.entry_descricao['state'] = 'enabled'
        self.entry_pagina['state'] = 'enabled'
        self.entry_autor['state'] = 'enabled'
        self.button_novo['state'] = 'disabled'
        self.button_salvar['state'] = 'enabled'
        self.button_pesquisar['state'] = 'disabled'
        self.button_cancelar['state'] = 'enabled'
        self.button_editar['state'] = 'disabled'

    def evento_salvar_click(self):
        matricula = self.svar_matricula.get()
        isbn = self.svar_isbn.get()
        titulo = self.svar_titulo.get()
        descricao = self.svar_descricao.get()
        pagina = self.svar_pagina.get()
        autor = self.svar_autor.get()
        novo_livro = Livro(matricula, isbn, titulo.upper(), descricao.upper(), pagina, autor)

        try:
            if self.novo_registro:
                LivroControler.inserir(novo_livro)
                messagebox.showinfo('Sucesso', 'Livro cadastrado com sucesso' )
            else:
                LivroControler.atualizar(novo_livro)
                messagebox.showinfo('Sucesso', 'Registro atualizado com sucesso' )
            self.evento_cancelar_click()
        except AttributeError as erro:
            messagebox.showerror('Erro no cadastro', str(erro))
    
    def evento_pesquisar_click(self):
        matricula = self.svar_matricula.get()
        isbn = self.svar_isbn.get()
        titulo = self.svar_titulo.get()
        descricao = self.svar_descricao.get()
        pagina = self.svar_pagina.get()
        autor = self.svar_autor.get()

        criterios = dict()
        if len(matricula.strip()) > 0:
            criterios['codigo'] = (matricula,'=')
        if len(isbn.strip()) > 0:
            criterios['isbn'] = (isbn,'=')
        if len(titulo.strip()) > 0:
            criterios['titulo'] = ('%'+titulo.upper()+'%','LIKE')
        
        livro = LivroControler.pesquisar(criterios)
        if livro:
            self.entry_isbn['state'] = 'disabled'
            self.entry_titulo['state'] = 'disabled'
            self.entry_descricao['state'] = 'disabled'
            self.entry_pagina['state'] = 'disabled'
            self.entry_autor['state'] = 'disabled'
            self.button_novo['state'] = 'disabled'
            self.button_editar['state'] = 'enabled'
            self.button_salvar['state'] = 'disabled'
            self.button_pesquisar['state'] = 'disabled'
            self.button_cancelar['state'] = 'enabled'
            self.svar_matricula.set(livro[0])
            self.svar_isbn.set(livro[1])
            self.svar_titulo.set(livro[2])
            self.svar_descricao.set(livro[3])
            self.svar_pagina.set(livro[4])
            self.svar_autor.set(livro[5])
        else:
            messagebox.showwarning('Nenhum registro encontrado', 'Não foi encontrado o registro solicitado')