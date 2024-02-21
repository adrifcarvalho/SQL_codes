import sqlite3

conexao = sqlite3.connect('bancoSem05')

cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto)
cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(200));')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "ALBERT EINSTEIN", 76, "FISICA");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "SIGMUND FREUD", 83, "PSICANALISE");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "MARIE CURIE", 67, "QUIMICA");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "JEAN-PAUL SARTRE", 75, "FILOSOFIA");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "SIMONE DE BEAUVOIR", 78, "FILOSOFIA");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (6, "CARL GUSTAV JUNG", 86, "PSIQUIATRIA");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (7, "KARL MARX", 65, "ECONOMIA");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (8, "NOAM CHOMSKY", 95, "SOCIOLOGIA");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (9, "BERTRAND RUSSEL", 98, "MATEMATICA");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (10, "FRANS KAFKA", 41, "LITERATURA");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (11, "WALTER BENJAMIN", 48, "SOCIOLOGIA");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (12, "ALBERT CAMUS", 47, "JORNALISMO");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (13, "GEORGE ORWELL", 47, "JORNALISMO");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (14, "PRESTES MAIS" 69, "ENGENHARIA");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (15, "VOLDEMORT", 60, "BRUXARIA");')

#3. Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
cursor.execute('SELECT * FROM alunos;')

#Exibir a lista de alunos
print('Todos os registros da tabela de alunos')
for row in cursor.fetchall():
    print('Id: ', row[0], ' Nome: ', row[1], ' idade: ', row[2], ' curso: ', row[3])

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20;')

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
cursor.execute('SELECT * FROM alunos WHERE curso = "ENGENHARIA" ORDER BY nome;') 

#d) Contar o número total de alunos na tabela
cursor.execute('SELECT COUNT(id) as QTD_ALUNOS FROM alunos;')

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade = 35 WHERE nome = "ALBERT CAMUS";')

#b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id = 15;')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 
# Insira alguns registros de clientes na tabela.

#criação da tabela
cursor.execute('CREATE TABLE clientes (id INT NOT NULL PRIMARY KEY, nome VARCHAR(100), idade INT, saldo REAL);')

#inserção de registros
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "JULIANA CASTRO", 36, 1234.56);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "CARLOS HENRIQUE GOMES", 33, 2145.87);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "ANA CLARA CARVALHO", 27, 956.88);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "MARIA CECILIA SOUZA", 25, 3045.28);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "CLAUDIO SOARES", 28, 1230.90);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (6, "GUSTAVO FIRMINO", 36, 876.20);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (7, "EMERSON DA SILVA FERREIRA", 65, 4990.66);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (8, "RAQUEL AGOSTINHO", 39, 9500.23);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (9, "JULIO BERNARDO SILVEIRA", 29, 7567.20);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (10, "MARIANA GODOI", 41, 4890.11);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (11, "SERGIO SIQUEIRA", 24, 7009.22);')

#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30;')

print('Clientes com idade superior a 30 anos')
for row in cursor.fetchall():
    print('Nome: ', row[0], ' idade: ', row[1])
    
#b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT AVG(saldo) FROM clientes;')
for row in cursor.fetchall():
    print('O saldo médio dos clientes é: ',round(row[0],2))

#c) Encontre o cliente com o saldo máximo.
cursor.execute('SELECT nome, MAX(saldo) FROM clientes;')
for row in cursor.fetchall():
    print('O cliente com maior saldo é: ', row[0], ' com o saldo no valor de ', round(row[1],2))

#d) Conte quantos clientes têm saldo acima de 1000.
cursor.execute('SELECT COUNT(id) FROM clientes  WHERE saldo > 1000;')
for row in cursor.fetchall():
    print('A quantidade de clientes com saldo maior que 1000 é: ', row[0])

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo = 7350.78 WHERE id = 8')

#b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id = 11;')

#8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), 
# cliente_id (chave estrangeira referenciando o id da tabela "clientes"), 
# produto (texto) e valor (real). 
# Insira algumas compras associadas a clientes existentes na tabela "clientes".
# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

#criação da tabela
sql = 'CREATE TABLE compras (id INT NOT NULL, cliente_id INT NOT NULL, produto VARCHAR(100), valor REAL, '
sql += 'PRIMARY KEY (id), '
sql += 'FOREIGN KEY (cliente_id) REFERENCES Clientes(id));'
#cursor.execute(sql)

#inserção de registros
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 1, "ARROZ INTEGRAL", 6.56);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 3, "ARROZ INTEGRAL", 6.56);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 4, "ARROZ INTEGRAL", 6.56);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (4, 7, "ARROZ INTEGRAL", 6.56);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (5, 8, "ARROZ INTEGRAL", 6.56);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (6, 10, "ARROZ INTEGRAL", 6.56);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (7, 2, "FEIJÃO CARIOCA", 4.89);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (8, 3, "FEIJÃO CARIOCA", 4.89);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (9, 5, "FEIJÃO CARIOCA", 4.89);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (10, 6, "FEIJÃO CARIOCA", 4.89);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (11, 2, "ESPAGUETE GRANO DURO", 9.75);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (12, 3, "ESPAGUETE GRANO DURO", 9.75);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (13, 8, "ESPAGUETE GRANO DURO", 9.75);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (14, 9, "ESPAGUETE GRANO DURO", 9.75);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (15, 10, "ESPAGUETE GRANO DURO", 9.75);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (16, 1, "GRÃO DE BICO", 10.99);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (17, 4, "GRÃO DE BICO", 10.99);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (18, 5, "GRÃO DE BICO", 10.99);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (19, 6, "GRÃO DE BICO", 10.99);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (20, 2, "MOLHO DE TOMATE", 7.6);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (21, 8, "MOLHO DE TOMATE", 7.6);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (22, 9, "MOLHO DE TOMATE", 7.6);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (23, 3, "AÇÚCAR MASCAVO", 9.56);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (24, 5, "AÇÚCAR MASCAVO", 9.56);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (25, 6, "AÇÚCAR MASCAVO", 9.56);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (26, 7, "AÇÚCAR MASCAVO", 9.56);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (27, 2, "LENTILHA", 10.9);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (28, 8, "LENTILHA", 10.9);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (29, 9, "LENTILHA", 10.9);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (30, 10, "LENTILHA", 10.9);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (31, 1, "AZEITE DE OLIVA", 29.8);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (32, 2, "AZEITE DE OLIVA", 29.8);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (33, 4, "AZEITE DE OLIVA", 29.8);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (34, 6, "AZEITE DE OLIVA", 29.8);')

#consulta
sql = 'SELECT cli.nome, cp.produto, cp.valor FROM clientes cli '
sql += 'JOIN compras cp ON cli.id = cp.cliente_id '
sql += 'ORDER BY cli.nome, cp.produto'
cursor.execute(sql)

cliente = ''
#exibir a lista de clietnes e produtos comprados
for row in cursor.fetchall():
    if (row[0] != cliente):
        print('Nome do cliente: ', row[0])
        print('             Produto adquirido: ', row[1], ' preço: R$', row[2])
        cliente = row[0]
    else:
        print('             Produto adquirido: ', row[1], ' preço: R$', row[2])

conexao.commit()
conexao.close()

