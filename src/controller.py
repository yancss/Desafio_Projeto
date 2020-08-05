from flask import Flask, render_template, request, redirect, flash, url_for
from src.dao.dao import ClienteDao
from flask_mysqldb import MySQL
from src.models.models import Cliente

app = Flask(__name__)
app.secret_key = 'yan'

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "123456"
app.config['MYSQL_DB'] = "aplicacao"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
cliente_dao = ClienteDao(db)


@app.route('/')
def index():
    lista = cliente_dao.listar()
    return render_template('lista.html', titulo='Clientes', clientes=lista)


@app.route('/novo_cliente')
def novo_cliente():
    return render_template('novo_cliente.html', titulo='Novo Cliente')


@app.route('/inserir_cliente', methods=['POST',])
def inserir_cliente():
    print('Fui chamado')
    print(f'''Dados: {request.json['nome_cliente']}''')
    nome_cliente = request.json['nome_cliente']
    razao_social = request.json['razao_social']
    cpf_cnpj = request.json['cpf_cnpj']
    insc_estadual = request.json['insc_estadual']
    telefone = request.json['telefone']
    celular = request.json['celular']
    email = request.json['email']
    n_endereco = request.json['n_endereco']
    id_grupo = request.json['id_grupo']
    id_cidade = request.json['id_cidade']
    id_bairro = request.json['id_bairro']
    id_endereco = request.json['id_endereco']
    cliente = Cliente(nome_cliente, razao_social, cpf_cnpj, insc_estadual, telefone, celular, email, n_endereco, id_grupo, id_cidade, id_bairro, id_endereco)
    cliente_dao.salvar(cliente)
    return redirect(url_for('index'))


@app.route('/editor/<int:id_cliente>')
def editor(id_cliente):
    cliente = cliente_dao.busca_por_id(id_cliente)
    return render_template('editor.html', titulo='Editando Cliente', cliente=cliente)


@app.route('/atualizar', methods=['POST',])
def atualizar():
    nome_cliente = request.json['nome_cliente']
    razao_social = request.json['razao_social']
    cpf_cnpj = request.json['cpf_cnpj']
    insc_estadual = request.json['insc_estadual']
    telefone = request.json['telefone']
    celular = request.json['celular']
    email = request.json['email']
    n_endereco = request.json['n_endereco']
    id_grupo = request.json['id_grupo']
    id_cidade = request.json['id_cidade']
    id_bairro = request.json['id_bairro']
    id_endereco = request.json['id_endereco']
    cliente = Cliente(nome_cliente, razao_social, cpf_cnpj, insc_estadual, telefone, celular, email, n_endereco, id_grupo, id_cidade, id_bairro, id_endereco, id_cliente=request.json['id_cliente'])
    cliente_dao.salvar(cliente)
    return redirect(url_for('index'))


@app.route('/deletar/<int:id_cliente>')
def deletar(id_cliente):
    cliente_dao.deletar(id_cliente)
    flash('Cliente Deletado!')
    return redirect(url_for('index'))

app.run(debug=True)
