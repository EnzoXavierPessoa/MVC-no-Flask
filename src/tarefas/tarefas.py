from datetime import datetime
from database import Database


class Tarefa:
    """Provê métodos para armazenar, recuperar e processar os dados das tarefas
    criadas a partir do formulário principal.
    """

    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvarTarefa(self):
        """Salva a tarefa no banco de dados."""
        sql = 'INSERT INTO tarefa(titulo_tarefa, data_conclusao) VALUES (%s, %s);'
        params = (self.titulo, self.data_conclusao)  # protege contra SQL Injection

        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def listarTarefas() -> list:
        """Retorna uma lista com todas as tarefas cadastradas."""
        sql = '''SELECT id_tarefa, titulo_tarefa, data_conclusao
        FROM tarefa LIMIT 100;'''

        with Database() as db:
            tarefas_banco = db.executar(sql)

        return tarefas_banco if tarefas_banco else []

    @staticmethod
    def apagarTarefa(id_tarefa: int):
        """Apaga uma tarefa do banco de dados pelo seu ID."""
        sql = 'DELETE FROM tarefa WHERE id_tarefa = %s;'
        params = (id_tarefa,)  # A vírgula no final é obrigatória para criar uma tupla em Python

        with Database() as db:
            db.executar(sql, params)