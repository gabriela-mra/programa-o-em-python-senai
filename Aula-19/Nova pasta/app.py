import sqlite3


con = sqlite3.connect('cadastro.db')
cursor = con.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,            
        nome TEXT NOT NULL,
        email TEXT NOT NULL 
   )
''')


# crud


def criar_cliente(nome, email):
    cursor.execute('INSERT INTO clientes (nome, email) values(?,?)', (nome, email))
    con.commit()


def listar_clentes():
    cursor.execute('SELECT * FROM clientes')
    return cursor.fetchall()


def atualizar_mail(id_cliente, novo_email):
    cursor.execute('UPDATE clientes SET email=? WHERE id = ?', (novo_email, id_cliente))
    con.commit()


def deletar_cliente(id_cliente):
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente,))
    con.commit()


criar_cliente('Ana', 'ana@gmail.com')
criar_cliente('Lucas', 'Lucas@gmail.com')
print('Inserindo ... ')
print(listar_clentes())


# atualizar
print('Atualizando ...')
atualizar_mail(1,'ana_1@gmail.com')
print(listar_clentes())


# delete


print('deletando ... ')
deletar_cliente(1)
print(listar_clentes())


con.close()