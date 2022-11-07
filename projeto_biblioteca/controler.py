from db import DatabaseManager
from modelo import Estudante
from modelo import Autor
from modelo import Livro


class UsuarioControler:

    @staticmethod
    def validar_login(nome, senha):
        sql = 'SELECT codigo FROM public.usuario WHERE login=%s AND senha=%s;'
        parametros = (nome, senha)
        conexao = DatabaseManager.get_connection()
        cursor = conexao.cursor()
        cursor.execute(sql, parametros)
        return cursor.fetchone()


class EstudanteControler:
    
    @staticmethod
    def inserir(estudante:Estudante):
        sql = 'INSERT INTO public.estudante(nome, cpf, sexo, data_nascimento, escolaridade, status)	VALUES (%s, %s, %s, %s, %s, %s);'
        parametros = (estudante.nome, estudante.cpf, estudante.sexo, estudante.data_nascimento, estudante.escolaridade, estudante.status)
        conexao = DatabaseManager.get_connection()
        cursor = conexao.cursor()
        cursor.execute(sql, parametros)
        return True
        # DatabaseManager.close_connection()

    @staticmethod
    def pesquisar(criterios):
        sql = 'SELECT * FROM estudante WHERE '
        lista = [f'{x} {y[1]} %s' for x,y in criterios.items()]
        sql += ' AND '.join(lista)
        params = [x[0] for x in criterios.values()]
        conexao = DatabaseManager.get_connection()
        cursor = conexao.cursor()
        cursor.execute(sql, params)
        return cursor.fetchone()
    
    @staticmethod
    def atualizar(estudante:Estudante):
        sql = 'UPDATE public.estudante SET nome = %s, cpf = %s, sexo = %s, data_nascimento = %s, escolaridade = %s WHERE codigo = %s;'
        params = (estudante.nome, estudante.cpf, estudante.sexo, estudante.data_nascimento, estudante.escolaridade, estudante.codigo)
        conexao = DatabaseManager.get_connection()
        cursor = conexao.cursor()
        cursor.execute(sql, params)
        return True

class AutorControler:
    
    @staticmethod
    def inserir(autor:Autor):
        sql = 'INSERT INTO public.autor(nome)	VALUES (%s);'
        parametros = (autor.nome,)
        conexao = DatabaseManager.get_connection()
        cursor = conexao.cursor()
        cursor.execute(sql, parametros)
        return True
        # DatabaseManager.close_connection()

    @staticmethod
    def pesquisar(criterios):
        sql = 'SELECT * FROM autor WHERE '
        lista = [f'{x} {y[1]} %s' for x,y in criterios.items()]
        sql += ' AND '.join(lista)
        params = [x[0] for x in criterios.values()]
        conexao = DatabaseManager.get_connection()
        cursor = conexao.cursor()
        cursor.execute(sql, params)
        return cursor.fetchone()
    
    @staticmethod
    def atualizar(autor:Autor):
        sql = 'UPDATE public.autor SET nome = %s WHERE codigo = %s;'
        params = (autor.nome, autor.codigo)
        conexao = DatabaseManager.get_connection()
        cursor = conexao.cursor()
        cursor.execute(sql, params)
        return True


class LivroControler:
    
    @staticmethod
    def inserir(livro:Livro):
        sql = 'INSERT INTO public.livro(isbn, titulo, descricao, pagina, autor)	VALUES (%s, %s, %s, %s, %s);'
        parametros = (livro.isbn, livro.titulo, livro.descricao, livro.pagina, livro.autor)
        conexao = DatabaseManager.get_connection()
        cursor = conexao.cursor()
        cursor.execute(sql, parametros)
        return True
        # DatabaseManager.close_connection()

    @staticmethod
    def pesquisar(criterios):
        sql = 'SELECT * FROM livro WHERE '
        lista = [f'{x} {y[1]} %s' for x,y in criterios.items()]
        sql += ' AND '.join(lista)
        params = [x[0] for x in criterios.values()]
        conexao = DatabaseManager.get_connection()
        cursor = conexao.cursor()
        cursor.execute(sql, params)
        return cursor.fetchone()
    
    @staticmethod
    def atualizar(livro:Livro):
        sql = 'UPDATE public.livro SET isbn = %s, titulo = %s, descricao = %s, pagina = %s, autor = %s WHERE codigo = %s;'
        params = (livro.isbn, livro.titulo, livro.descricao, livro.pagina, livro.autor, livro.codigo)
        conexao = DatabaseManager.get_connection()
        cursor = conexao.cursor()
        cursor.execute(sql, params)
        return True
