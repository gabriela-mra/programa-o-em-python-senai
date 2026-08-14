import customtkinter as ctk
import sqlite3


ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')


conn =  sqlite3.connect('dados.db')
cursor = conn.cursor()


cursor.execute('CREATE TABLE IF NOT EXISTS itens(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT )')
conn.commit()


select_id = None


# funções



def atualizar_lista():
    for widget in scroll.winfo_children():
        widget.destroy()
    cursor.execute('SELECT  * FROM itens ORDER BY id DESC')
    for item_id, nome in cursor.fetchall():
        btn = ctk.CTkButton(
        scroll,
        text=nome,
        anchor='w',
        fg_color=('gray'),
        text_color=('black'),
        hover_color='gray',
        )
        btn.pack(fill = 'x', padx = 2)    












# interface 
app = ctk.CTk()
app.title('CRUD COM CUSTOM TKINTER')
app.geometry('500x600')


# inputs:
entry =  ctk.CTkEntry(app, placeholder_text='DIGITE O ITÉM')
entry.pack(padx= 20, pady = (20,10), fill = 'x')


# sessão do  btn
btn_frame = ctk.CTkFrame(app, fg_color='transparent')
btn_frame.pack(padx = 20, fill = 'x')


btn_save =  ctk.CTkButton(btn_frame, text= 'salvar' , width=100)
btn_save.pack(side = 'left', expand = True, padx = 2)


btn_delete =  ctk.CTkButton(btn_frame, text= 'deletar', 
                            hover_color = 'yellow',
                            fg_color='red',
                            width =  100                           
                            )
btn_delete.pack(side = 'left', expand = True, padx = 2)


btn_clear  =  ctk.CTkButton(btn_frame, text='limpar',
                            hover_color = 'white',
                            fg_color='green',
                            width =  100 ,
                            border_width=2,
                            ) 


btn_clear.pack(side = 'left', expand = True, padx = 2)


scroll = ctk.CTkScrollableFrame(app)
scroll.pack(padx = 20, pady =  20, fill = 'both', expand  =  True)



atualizar_lista()


# listar .... 
app.mainloop()


