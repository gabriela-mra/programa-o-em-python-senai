import customtkinter as ctk
import sqlite3
import tkinter as tk
from tkinter import messagebox

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')



criando = sqlite3.connect('atividade1.db')
cursor = criando.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS dados(
    nome TEXT,
    idade INTEGER,
    email INTEGER,
    endereço TEXT,
    trabalho TEXT,
    graduação TEXT
)
''')

def criar_dados():    
    nome  = nome_input.get()
    idade = idade_input.get()
    email = email_input.get()
    endereço = endereço_input.get()
    trabalho = trabalho_input.get()
    graduação = graduação_input.get()
    cursor.execute('INSERT INTO dados (nome, idade, email, endereço, trabalho, graduação) values(?,?,?,?,?,?,?)', (nome, idade, email, endereço, trabalho, graduação))
    criando.commit()
    messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO')

# def listar_clientes():
#     cursor.execute('SELECT * FROM dados')
#     return cursor.fetchall()

# def atualizar_email(id_cliente, novo_email):
#     cursor.execute('UPDATE clientes SET email=? WHERE id = ?', (novo_email, id_cliente))
#     criando.commit()


# def deletar_cliente(id_cliente):
#     cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente,))
#     criando.commit()


app = ctk.CTk()
app.title('AGENCIA DE MARKETING')
app.geometry('500x600')


ctk.CTkLabel(app, text =  'CADASTRO LEADS DA AGENCIA:').grid(row=0, column=0)


ctk.CTkLabel(app, text =  'Nome:').grid(row=1, column=1)
nome_input = ctk.CTkEntry(app)
nome_input.grid(row=2, column=1)  


ctk.CTkLabel(app, text =  'Idade:').grid(row=4, column=1)
idade_input = ctk.CTkEntry(app)
idade_input.grid(row=5, column=1)  

ctk.CTkLabel(app, text =  'E-mail:').grid(row=8, column=1)
email_input = ctk.CTkEntry(app)
email_input.grid(row=9, column=1)  

ctk.CTkLabel(app, text =  'Endereço:').grid(row=12, column=1)
endereço_input = ctk.CTkEntry(app)
endereço_input.grid(row=13, column=1)  

ctk.CTkLabel(app, text =  'Trabalho:').grid(row=16, column=1)
trabalho_input = ctk.CTkEntry(app)
trabalho_input.grid(row=17, column=1)

ctk.CTkLabel(app, text =  'Graduação:').grid(row=16, column=1)
graduação_input = ctk.CTkEntry(app)
graduação_input.grid(row=17, column=1)

btn =  ctk.CTkButton(app, text= 'Inserir', command=criar_dados)
btn.grid(row=24, column=1)




app.mainloop()