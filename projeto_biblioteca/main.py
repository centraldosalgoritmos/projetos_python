import interface
import db
from datetime import datetime


def atualiza_emprestimos():
    sql = 'SELECT codigo, data_prevista_devolucao, estado FROM emprestimo;'
    conexao = db.DatabaseManager.get_connection()
    cursor = conexao.cursor()
    cursor.execute(sql)
    registros = cursor.fetchall()
    for registro in registros:
        if registro[2] != "FINALIZADO":
            data_devolucao = registro[1]
            data_hoje = datetime.now().date()
            if data_devolucao < data_hoje:
                sql = 'UPDATE public.emprestimo SET estado = %s WHERE codigo = %s;'
                parametros = ('EM ATRASO', registro[0])
                cursor.execute(sql, parametros)


atualiza_emprestimos()

janela = interface.JanelaPrincipal()
janela.mainloop()

# interface.menu_inicial()
db.DatabaseManager.close_connection()
