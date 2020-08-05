import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='123456', host='127.0.0.1', port=3306)

conn.cursor().execute("DROP DATABASE `aplicacao`;")
conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `aplicacao`;
    USE `aplicacao`;
    CREATE TABLE `grupo_cliente` (
      `id_grupo` int(12) NOT NULL AUTO_INCREMENT,
      `nome_grupo` varchar(100) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id_grupo`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin; 
    CREATE TABLE `pais` (
      `id_pais` int(12) NOT NULL AUTO_INCREMENT,
      `nome_pais` varchar(100) COLLATE utf8_bin NOT NULL,
      `sigla_pais` varchar(3) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id_pais`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `cidade` (
      `id_cidade` int(12) NOT NULL AUTO_INCREMENT,
      `nome_cidade` varchar(100) COLLATE utf8_bin NOT NULL,
      `cod_mun_fiscal` int(12) COLLATE utf8_bin,
      `id_uf` int(12) COLLATE utf8_bin DEFAULT NULL,
      PRIMARY KEY (`id_cidade`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `uf` (
      `id_uf` int(12) NOT NULL AUTO_INCREMENT,
      `nome_uf` varchar(100) COLLATE utf8_bin NOT NULL,
      `sigla_uf` varchar(2) COLLATE utf8_bin NOT NULL,
      `id_pais` int(12) COLLATE utf8_bin DEFAULT NULL,
      PRIMARY KEY (`id_uf`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `bairro` (
      `id_bairro` int(12) NOT NULL AUTO_INCREMENT,
      `nome_bairro` varchar(100) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id_bairro`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `endereco` (
     `id_endereco` int(12) NOT NULL AUTO_INCREMENT,
     `nome_endereco` varchar(200) COLLATE utf8_bin NOT NULL,
     `logradouro` varchar(10) COLLATE utf8_bin NOT NULL,
     PRIMARY KEY (`id_endereco`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `cliente` (
      `id_cliente` int(12) NOT NULL AUTO_INCREMENT,
      `nome_cliente` varchar(150) COLLATE utf8_bin NOT NULL,
      `razao_social` varchar(150) COLLATE utf8_bin,
      `cpf_cnpj` varchar(14) COLLATE utf8_bin,
      `telefone` varchar(12) COLLATE utf8_bin,
      `insc_estadual` varchar(20) COLLATE utf8_bin,
      `celular` varchar(12) COLLATE utf8_bin,
      `email` varchar(40) COLLATE utf8_bin,
      `n_endereco` int(12) COLLATE utf8_bin DEFAULT 0,
      `id_grupo` int(12) COLLATE utf8_bin DEFAULT 1,
      `id_cidade` int(12) COLLATE utf8_bin DEFAULT 1,
      `id_bairro` int(12) COLLATE utf8_bin DEFAULT 1,
      `id_endereco` int(12) COLLATE utf8_bin DEFAULT 1,
      PRIMARY KEY (`id_cliente`) 
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
'''

conn.cursor().execute(criar_tabelas)
cursor = conn.cursor()



##########################          Adicionando as chaves estrangeiras nas tabelas          #########################################
fk_cliente = '''
    ALTER TABLE `cliente` ADD CONSTRAINT `fk_grupo_cliente` FOREIGN KEY (`id_grupo`) REFERENCES `grupo_cliente` (`id_grupo`);
    ALTER TABLE `cliente` ADD CONSTRAINT `fk_cidade_cliente` FOREIGN KEY (`id_cidade`) REFERENCES `cidade` (`id_cidade`);
    ALTER TABLE `cliente` ADD CONSTRAINT `fk_bairro_cliente` FOREIGN KEY (`id_bairro`) REFERENCES `bairro` (`id_bairro`);
    ALTER TABLE `cliente` ADD CONSTRAINT `fk_endereco_cliente` FOREIGN KEY (`id_endereco`) REFERENCES `endereco` (`id_endereco`);
    ALTER TABLE `cidade` ADD CONSTRAINT `fk_cidade_uf` FOREIGN KEY (`id_uf`) REFERENCES `uf` (`id_uf`);
    ALTER TABLE `uf` ADD CONSTRAINT `fk_uf_pais` FOREIGN KEY (`id_pais`) REFERENCES `pais` (`id_pais`);    
'''
conn.cursor().execute(fk_cliente)
cursor = conn.cursor()


##########################           Populando a tabela de  Grupo de Clientes          #########################################
cursor.executemany(
      'INSERT INTO aplicacao.grupo_cliente (id_grupo, nome_grupo) VALUES (%s, %s)',
      [
            (1, 'Varejo'),
            (2, 'Atacarejo'),
            (3, 'Produtor Rural'),
            (4, 'Atacado')
      ])

#########           Exibindo as chaves dos registros na tabela de Grupo de Cliente       #########
cursor.execute('select * from aplicacao.grupo_cliente')
print(' ---  Grupo de Clientes: ')
for grupo in cursor.fetchall():
    print(grupo[1])
conn.commit()




##########################           Populando a tabela de Países          #########################################
cursor.executemany(
      'INSERT INTO aplicacao.pais (id_pais, nome_pais, sigla_pais) '
      'VALUES (%s, %s, %s)',
      [
            (1, 'Brasil', 'BRA'),
            (2, 'Canada', 'CAN'),
            (3, 'Argentina', 'ARG'),
            (4, 'Equador', 'EQU'),
            (5, 'Holanda', 'HOL')
      ])

#########           Exibindo as chaves dos registros na tabela de País     #########
cursor.execute('select * from aplicacao.pais')
print(' ---  Países cadastrados: ')
for pais in cursor.fetchall():
    print(pais[1])
conn.commit()





##########################           Populando a tabela de UFs          #########################################
cursor.executemany(
      'INSERT INTO aplicacao.uf (id_uf, nome_uf, sigla_uf, id_pais) '
      'VALUES (%s, %s, %s, %s)',
      [
            (1, 'Rondonia', 'RO', 1),
            (2, 'Acre', 'AC', 1),
            (3, 'Amazonas', 'AM', 1),
            (4, 'Roraima', 'RR', 1),
            (5, 'Para', 'PA', 1),
            (6, 'Amapa', 'AP', 1),
            (7, 'Tocantins', 'TO', 1),
            (8, 'Maranhao', 'MA', 1),
            (9, 'Piaui', 'PI', 1),
            (10, 'Ceara', 'CE', 1),
            (11, 'Minas Gerais', 'MG', 1),
            (12, 'Sao Paulo', 'SP', 1),
            (13, 'Rio de Janeiro', 'RJ', 1),
            (14, 'Espirito Santo', 'ES', 1),
            (15, 'Bahia', 'BA', 1),
            (16, 'Goias', 'GO', 1),
            (17, 'Sergipe', 'SE', 1)
      ])

#########          Exibindo as chaves dos registros na tabela de UFs          #########
cursor.execute('select * from aplicacao.uf')
print(' ---  UFs cadastrados: ')
for uf in cursor.fetchall():
    print(uf[1])
conn.commit()





##########################           Populando a tabela de Bairro          #########################################
cursor.executemany(
      'INSERT INTO aplicacao.bairro (id_bairro, nome_bairro) '
      'VALUES (%s, %s)',
      [
            (1, 'Martins'),
            (2, 'Lagoinha'),
            (3, 'Tabajaras'),
            (4, 'Centro'),
            (5, 'Planalto')
      ])

#########           Exibindo as chaves dos registros na tabela de Bairro     #########
cursor.execute('select * from aplicacao.bairro')
print(' ---  Bairros cadastrados: ')
for bairro in cursor.fetchall():
    print(bairro[1])
conn.commit()





##########################           Populando a tabela de Cidade          #########################################
cursor.executemany(
      'INSERT INTO aplicacao.cidade (id_cidade, nome_cidade, cod_mun_fiscal, id_uf) '
      'VALUES (%s, %s, %s, %s)',
      [
            (1, 'Uberlandia', 0, 11),
            (2, 'Belo Horizonte', 0, 11),
            (3, 'Sao Paulo', 0, 12),
            (4, 'Goiania', 0, 16),
            (5, 'Ribeirao Preto', 0, 12)
      ])
#########         Exibindo as chaves dos registros na tabela de Cidade       #########
cursor.execute('select * from aplicacao.cidade')
print(' ---  Cidades cadastrados: ')
for cidade in cursor.fetchall():
    print(cidade[1])
conn.commit()




##########################           Populando a tabela de Endereço          #########################################
cursor.executemany(
      'INSERT INTO aplicacao.endereco (id_endereco, nome_endereco, logradouro) '
      'VALUES (%s, %s, %s)',
      [
            (1, 'Princesa Isabel', 'Rua'),
            (2, 'Getulio Vargas', 'Avenida'),
            (3, 'Rondon Pacheco', 'Avenida'),
            (4, 'Sergio Pacheco', 'Praca'),
            (5, 'Afonso Pena', 'Rua')
      ])

#########           Exibindo as chaves dos registros na tabela de Endereço     #########
cursor.execute('select * from aplicacao.endereco')
print(' ---  Endereços cadastrados: ')
for endereco in cursor.fetchall():
    print(endereco[1])
conn.commit()




##########################           Populando a tabela de Cliente          #########################################

cursor.executemany(
      'INSERT INTO aplicacao.cliente (id_cliente, nome_cliente, razao_social, cpf_cnpj, telefone, celular, email) '
      'VALUES (%s, %s, %s, %s, %s, %s, %s)',
      [
            (1, 'Jose Fernando', 'Jose Fernando', '04498745621', 3432323232, 34992121478, 'jose@gmail.com'),
            (2, 'Joana Fernandes', 'Joana Fernandes', '04421232621', 3432323238, 31998785474, 'joana@gmail.com'),
            (3, 'Jorge Faria', 'Jorge Faria', '14231745621', 3432323232, 48996365232, 'jorge@gmail.com')
      ])

#########        Exibindo as chaves dos registros na tabela de Cliente      #########
cursor.execute('select * from aplicacao.cliente')
print(' ---  Clientes cadastrados: ')
for cliente in cursor.fetchall():
    print(cliente[1])
conn.commit()



cursor.close()