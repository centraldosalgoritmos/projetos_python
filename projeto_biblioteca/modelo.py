class Estudante:
    def __init__(self, codigo, nome, cpf, sexo, data_nascimento, escolaridade, status):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.escolaridade = escolaridade
        self.status = status


class Autor:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome


class Livro:
    def __init__(self, codigo, isbn, titulo, descricao, pagina, autor):
        self.codigo = codigo
        self.isbn = isbn
        self.titulo = titulo
        self.descricao = descricao
        self.pagina = pagina
        self.autor = autor


class Exemplar:
    def __init__(self, codigo, codigo_livro, ordem, estante, prateleira, disponibilidade):
        self.codigo = codigo
        self.codigo_livro = codigo_livro
        self.ordem = ordem
        self.estnte = estante
        self.prateleira = prateleira
        self.disponibilidade = disponibilidade


class Emprestimo:
    def __init__(self, codigo, codigo_estudante, codigo_exemplar, data_emprestimo, data_prevista_devolucao, estado):
        self.codigo = codigo
        self.codigo_estudante = codigo_estudante
        self.codigo_exemplar = codigo_exemplar
        self.data_emprestimo = data_emprestimo
        self.data_prevista_devolucao = data_prevista_devolucao
        self.estado = estado

