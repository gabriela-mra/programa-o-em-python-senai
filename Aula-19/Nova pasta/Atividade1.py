import sqlite3

criando = sqlite3.connect('atividade1.db')

cursor = criando.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS dados(
    nome TEXT,
    idade INTEGER,
    email INTEGER,
    endereço TEXT,
    trabalho TEXT,
    graduação TEXT
               
)''')

criando.commit()

# nome = input('Nome: ')
# idade =  int(input('Idade:  '))
# email =  int(input('E-mail:  '))
# endereço =  int(input('Endereço:  '))
# trabalho =  int(input('Trabalho:  '))
# graduação =  int(input('Graduação:  '))

# cursor.execute('INSERT INTO dados values(?,?)', (nome, idade, email, endereço, trabalho, graduação))

# nome = input('Nome: ')
# idade =  int(input('Idade:  '))
# email =  int(input('E-mail:  '))
# endereço =  int(input('Endereço:  '))
# trabalho =  int(input('Trabalho:  '))
# graduação =  int(input('Graduação:  '))

# cursor.execute('INSERT INTO dados values(?,?)', (nome, idade, email, endereço, trabalho, graduação))

# nome = input('Nome: ')
# idade =  int(input('Idade:  '))
# email =  int(input('E-mail:  '))
# endereço =  int(input('Endereço:  '))
# trabalho =  int(input('Trabalho:  '))
# graduação =  int(input('Graduação:  '))

# cursor.execute('INSERT INTO dados values(?,?)', (nome, idade, email, endereço, trabalho, graduação))

# nome = input('Nome: ')
# idade =  int(input('Idade:  '))
# email =  int(input('E-mail:  '))
# endereço =  int(input('Endereço:  '))
# trabalho =  int(input('Trabalho:  '))
# graduação =  int(input('Graduação:  '))

# cursor.execute('INSERT INTO dados values(?,?)', (nome, idade, email, endereço, trabalho, graduação))

# nome = input('Nome: ')
# idade =  int(input('Idade:  '))
# email =  int(input('E-mail:  '))
# endereço =  int(input('Endereço:  '))
# trabalho =  int(input('Trabalho:  '))
# graduação =  int(input('Graduação:  '))

# cursor.execute('INSERT INTO dados values(?,?)', (nome, idade, email, endereço, trabalho, graduação))

# nome = input('Nome: ')
# idade =  int(input('Idade:  '))
# email =  int(input('E-mail:  '))
# endereço =  int(input('Endereço:  '))
# trabalho =  int(input('Trabalho:  '))
# graduação =  int(input('Graduação:  '))

# cursor.execute('INSERT INTO dados values(?,?)', (nome, idade, email, endereço, trabalho, graduação))