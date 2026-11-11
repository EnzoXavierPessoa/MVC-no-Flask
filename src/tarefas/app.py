from flask import Flask, render_template, request
from tarefas import init_db  # Importa a função do arquivo tarefas.py local

app = Flask(__name__)

# Inicializa o banco de dados ao subir a aplicação
with app.app_context():
    init_db('data/tarefas.sql')


@app.route('/test')
def test():
    return 'Servidor online!'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Captura os dados enviados pelo formulário no HTML
        titulo_form = request.form.get('tituloTarefa')
        data_conclusao_form = request.form.get('dataConclusao')

        # Se você tiver a classe Tarefa implementada:
        # Tarefa.criar(titulo=titulo_form, data_conclusao=data_conclusao_form)

    # Exemplo de lista de tarefas fictícia enviada para o template
    tarefas = [
        {
            "id_tarefa": 1,
            "titulo_tarefa": "Exemplo de tarefa 1",
            "data_conclusao": "2026-11-11 00:00:00",
        },
        {
            "id_tarefa": 2,
            "titulo_tarefa": "Exemplo de tarefa 2",
            "data_conclusao": "2026-11-11 00:00:00",
        }
    ]

        

    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        tarefas_da_pagina=tarefas,
    )


if __name__ == '__main__':
    app.run(debug=True)