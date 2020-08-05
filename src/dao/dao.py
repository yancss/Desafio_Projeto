from src.models.models import Cliente

SQL_DELETA_CLIENTE = 'DELETE FROM aplicacao.cliente where id_cliente = %s'
SQL_CLIENTE_POR_ID = 'SELECT id_cliente, nome_cliente, razao_social, cpf_cnpj, insc_estadual, celular, telefone, email, n_endereco, id_grupo, id_cidade, id_bairro, id_endereco from aplicacao.cliente where id_cliente = %s'
SQL_BUSCA_CLIENTE = 'SELECT id_cliente, nome_cliente, razao_social, cpf_cnpj, insc_estadual, celular, telefone, email, n_endereco, id_grupo, id_cidade, id_bairro, id_endereco from aplicacao.cliente'

class ClienteDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, cliente):
        cursor = self.__db.connection.cursor()

        if (cliente.id_cliente):
            cursor.execute("UPDATE aplicacao.cliente SET nome_cliente='{0}', razao_social='{1}', cpf_cnpj='{2}', insc_estadual='{3}', celular='{4}', telefone='{5}', email='{6}',  n_endereco='{7}', "
                           "id_grupo='{8}', id_cidade='{9}', id_bairro='{10}', id_endereco='{11}' where id_cliente = '{12}'".format
                           (cliente.nome_cliente, cliente.razao_social, cliente.cpf_cnpj, cliente.insc_estadual, cliente.celular, cliente.telefone, cliente.email, cliente.n_endereco,
                            cliente.id_grupo, cliente.id_cidade, cliente.id_bairro, cliente.id_endereco, cliente.id_cliente))

        else:
            cursor.execute("INSERT into aplicacao.cliente (nome_cliente, razao_social, cpf_cnpj, insc_estadual, celular, telefone, email, n_endereco, id_grupo, id_cidade, id_bairro, id_endereco) "
                           "values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format
                           (cliente.nome_cliente, cliente.razao_social, cliente.cpf_cnpj, cliente.insc_estadual, cliente.celular, cliente.telefone, cliente.email, cliente.n_endereco,
                            cliente.id_grupo, cliente.id_cidade, cliente.id_bairro, cliente.id_endereco))
            cliente.id_cliente = cursor.lastrowid
        self.__db.connection.commit()
        return cliente

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CLIENTE)
        clientes = traduz_cliente(cursor.fetchall())
        return clientes

    def busca_por_id(self, id_cliente):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CLIENTE_POR_ID, (id_cliente,))
        tupla = cursor.fetchone()
        return Cliente(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], tupla[10], tupla[11], tupla[12], id_cliente=tupla[0])

    def deletar(self, id_cliente):
        self.__db.connection.cursor().execute(SQL_DELETA_CLIENTE, (id_cliente, ))
        self.__db.connection.commit()

def traduz_cliente(clientes):
    def cria_cliente_com_tupla(tupla):
        return Cliente(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], tupla[10], tupla[11], tupla[12], id_cliente=tupla[0])
    return list(map(cria_cliente_com_tupla, clientes))
