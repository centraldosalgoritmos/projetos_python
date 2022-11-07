from db import DatabaseManager
from datetime import datetime, timedelta

#tela inicial
def menu_inicial():
    while True:
        print('olá, bem vindo. Digite a opção desejada:')
        print('1 - Cadastros')
        print('2 - Empréstimos e Devoluções')
        print('3 - Consultas')
        print('4 - Relatórios')
        print('0 - Sair')
        entrada = int(input())
        if entrada == 1:
            menu_cadastro()
        elif entrada == 2:
            menu_emprestimo()
        elif entrada == 3:
            menu_consulta()
        elif entrada == 4:
            menu_relatorio()
        elif entrada == 0:    
            break


#cadastro de estudante
def cadastro_estudante():
    nome = input("Digite o nome do estudante:").upper()
    cpf = input("Digite o cpf do estudante (somente números):")
    sexo = input("Digite o sexo do estudante (M/F):").upper()
    data_nascimento = input("Digite a data de nascimento do estudante (DD/MM/AAAA):")
    escolaridade = input("Digite a escolaridade do estudante:").upper()
    status = True
    sql = 'INSERT INTO public.estudante(nome, cpf, sexo, data_nascimento, escolaridade, status)	VALUES (%s, %s, %s, %s, %s, %s);'
    parametros = (nome, cpf, sexo, data_nascimento, escolaridade, status)
    conexao = DatabaseManager.get_connection()
    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    DatabaseManager.close_connection()


#cadastro de livros
def cadastro_livro():
    isbn = input("Digite o ISBN do livro:").upper()
    titulo = input("Digite o título do livro:").upper()
    descricao = input("Digite a descrição do livro:").upper()
    pagina = input("Digite a quantidade de páginas do livro:")
    autor = input("Digite o nome do autor do livro:")
    sql = 'INSERT INTO public.livro(isbn, titulo, descricao, pagina, autor) VALUES (%s, %s, %s, %s, %s);'
    parametros = (isbn, titulo, descricao, pagina, autor)
    conexao = DatabaseManager.get_connection()
    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    DatabaseManager.close_connection()


#cadastro de exemplares
def cadastro_exemplar():
    codigo_livro = input("Digite o codigo do livro:")
    ordem = input("Digite a ordem do exemplar:")
    estante = input("Digite a localização (estante) do exemplar:").upper()
    prateleira = input("Digite qual prateleira o exemplar se encontra:").upper()
    disponibilidade = True
    sql = 'INSERT INTO public.exemplar(codigo_livro, ordem, estante, prateleira, disponibilidade) VALUES (%s, %s, %s, %s, %s);'
    parametros = (codigo_livro, ordem, estante, prateleira, disponibilidade)
    conexao = DatabaseManager.get_connection()
    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    DatabaseManager.close_connection()



#cadastro de autores
def cadastro_autor():
    nome = input("Digite o nome do autor:").upper()
    sql = 'INSERT INTO public.autor(nome) VALUES (%s);'
    parametros = (nome,)
    conexao = DatabaseManager.get_connection()
    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    DatabaseManager.close_connection()


def menu_cadastro():
    while True:
        print('Área de cadastros, digite a opção desejada:')
        print('1 - Cadastro de estudantes')
        print('2 - Cadastro de livros')
        print('3 - Cadastro de exemplares')
        print('4 - Cadastro de autores')
        print('0 - Retornar a tela inicial')
        entrada = int(input())
        if entrada == 1:
            cadastro_estudante()
        elif entrada == 2:
            cadastro_livro()
        elif entrada == 3:
            cadastro_exemplar()
        elif entrada == 4:
            cadastro_autor()
        elif entrada == 0:    
            break

#emprestimos e devoluções
#menu emprestimo
def realizar_emprestimo():
    codigo_estudante = input("Digite o codigo do estudante:")
    codigo_exemplar = input("Digite o codigo do exemplar:")
    data_emprestimo = str(datetime.now()).split(' ')[0]
    data_devolucao = datetime.now() + timedelta(days = 5)
    data_prevista_devolucao = str(data_devolucao).split(' ')[0]
    estado = 'EM ABERTO'
    sql = 'INSERT INTO public.emprestimo(codigo_estudante, codigo_exemplar, data_emprestimo, data_prevista_devolucao, estado) VALUES (%s, %s, %s, %s, %s);'
    parametros = (codigo_estudante, codigo_exemplar, data_emprestimo, data_prevista_devolucao, estado)
    conexao = DatabaseManager.get_connection()
    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    DatabaseManager.close_connection()


#realizar devolução
def realizar_devolucao():
    codigo_emprestimo = input("Digite o codigo do empréstimo:")
    sql = 'SELECT data_prevista_devolucao, estado FROM emprestimo WHERE codigo = %s;'
    parametros = (codigo_emprestimo,)
    conexao = DatabaseManager.get_connection()
    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    registro = cursor.fetchone()
    data_devolucao, estado = registro
    if estado == "EM ATRASO":
        data_hoje = datetime.now().date()
        diferenca_entre_datas = data_hoje - data_devolucao
        dias_em_atraso = diferenca_entre_datas.days
        multa = dias_em_atraso * 1.5
        print("Devolução em atraso. Multa de R$", round(multa, 2))
    sql = 'UPDATE public.emprestimo SET estado = %s WHERE codigo = %s;'
    parametros = ('FINALIZADO', codigo_emprestimo)
    cursor.execute(sql, parametros)
    DatabaseManager.close_connection()


def menu_emprestimo():
    while True:
        print('Área de empréstimos, digite a opção desejada:')
        print('1 - Realizar um empréstimo')
        print('2 - Realizar uma devolução')
        print('0 - Retornar a tela inicial')
        entrada = int(input())
        if entrada == 1:
            realizar_emprestimo()
        elif entrada == 2:
            realizar_devolucao()
        elif entrada == 0:    
            break

#cadastro de consultas
def consulta_disponibilidade():
    entrada = input("Digite o ISBN do livro:")
    sql = 'SELECT livro.titulo, exemplar.ordem, exemplar.disponibilidade FROM livro JOIN exemplar ON livro.codigo = exemplar.codigo_livro WHERE livro.isbn = %s;'
    parametros = (entrada,)
    conexao = DatabaseManager.get_connection()
    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    registros = cursor.fetchall()
    DatabaseManager.close_connection()
    for registro in registros:
        print(registro)


#Consulta autores e livros
def consulta_autores():
    entrada = input("Digite o nome do autor:").upper()
    sql = 'SELECT autor.codigo, livro.titulo, livro.descricao, livro.pagina FROM livro JOIN autor ON livro.autor = autor.codigo WHERE autor.nome LIKE %s;'
    parametros = ('%' + entrada + '%',)
    conexao = DatabaseManager.get_connection()
    cursor = conexao.cursor()
    cursor.execute(sql, parametros)
    registros = cursor.fetchall()
    DatabaseManager.close_connection()
    print(f'TÍTULO\t\tDESCRIÇÃO\t\tPAGINAS')
    for registro in registros:
        codigo, titulo, descricao, pagina = registro
        print(f'{titulo}\t\t{descricao}\t\t{pagina}')


def menu_consulta():
    while True:
        print('Área de consultas, digite a opção desejada:')
        print('1 - Consultar disponibilidade de exemplares do livro')
        print('2 - Consultar autores e respectivos livros')
        print('3 - Consultar empréstimos de livros em atraso')
        print('4 - Consultar estudantes com empréstimos em atraso')
        print('0 - Retornar a tela inicial')
        entrada = int(input())
        if entrada == 1:
            consulta_disponibilidade()
        elif entrada == 2:
            consulta_autores()
        elif entrada == 3:
            pass
        elif entrada == 4:
            pass
        elif entrada == 0:    
            break

#cadastro de relatorios
def menu_relatorio():
    while True:
        print('Área de relatórios, digite a opção desejada:')
        print('1 - Relatórios de livros mais emprestados. Top 10')
        print('2 - Relatórios de estudantes com empréstimos em atraso')
        print('3 - Relatórios de multas por estudante (com o total)')
        print('0 - Retornar a tela inicial')
        entrada = int(input())
        if entrada == 1:
            pass
        elif entrada == 2:
            pass
        elif entrada == 3:
            pass
        elif entrada == 0:    
            break