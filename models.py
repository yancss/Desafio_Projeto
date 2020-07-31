class Cliente:
    def __init__(self, nome_cliente, razao_social, cpf_cnpj, insc_estadual, telefone, celular, email, n_endereco, id_grupo, id_cidade, id_bairro, id_endereco, id_cliente=None):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.razao_social = razao_social
        self.cpf_cnpj = cpf_cnpj
        self.insc_estadual = insc_estadual
        self.telefone = telefone
        self.celular = celular
        self.email = email
        self.n_endereco = n_endereco
        self.id_grupo = id_grupo
        self.id_cidade = id_cidade
        self.id_bairro = id_bairro
        self.id_endereco = id_endereco

class Grupo_Cliente:
    def __init__(self, nome_grupo, id_grupo=None):
        self.id_grupo = id_grupo
        self.nome_grupo = nome_grupo