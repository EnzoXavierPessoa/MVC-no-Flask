from flask import Flask, render_template, request, redirect, url_for
from tarefas import init_db
from tarefas.models.tarefa import Tarefa  # Importa o seu Model Tarefa

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

        # Salva a nova tarefa no banco de dados usando o Model
        nova_tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_conclusao_form)
        nova_tarefa.salvarTarefa()
        
        return redirect(url_for('home'))

    # Busca as tarefas reais do banco de dados
    tarefas = Tarefa.listarTarefas()

    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        tarefas_da_pagina=tarefas,
    )


@app.route('/apagar/<int:id_tarefa>')
def apagar(id_tarefa):
    Tarefa.apagarTarefa(id_tarefa)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)