

import sqlite3
import tkinter as tk





c =  sqlite3.connect('nome.db')


cs = c.cursor()


cs.execute('''CREATE TABLE IF NOT EXISTS dados(
           
           nome TEXT,
           idade INTEGER           
           
           )''')


c.commit()


nome = input('Nome: ')
idade =  int(input('Idade:  '))


cs.execute('INSERT INTO dados values(?,?)', (nome, idade))


nome = input('Nome: ')
idade =  int(input('Idade:  '))


cs.execute('INSERT INTO dados values(?,?)', (nome, idade))


nome = input('Nome: ')
idade =  int(input('Idade:  '))


cs.execute('INSERT INTO dados values(?,?)', (nome, idade))
c.commit()



cs.execute('SELECT * FROM dados')
dados =  cs.fetchall()






for d in dados:
    print('nome:', d[0], 'idade:', d[1])


