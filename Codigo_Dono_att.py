from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import smtplib
import email.message
from datetime import datetime
from pathlib import Path
import uuid

# Ler o arquivo txt que está o email 
arquivo = open('email.txt', 'r')
email_send = arquivo.read()
arquivo.close()
# Enviar o email com o codigo pro dono entrar
data = datetime.today().strftime('%d-%m-%Y %H:%M')
tabela_vendas = pd.read_excel("banco/Historico_vendas.xlsx")
tabela = pd.read_excel("banco/Produtos.xlsx")
token2 = uuid.uuid4()
def enviar_email():
    print(token2)
    corpo_email = f"""
    <div class="col-6">
              <div class="form-group">
                <div class="card" style="width: 20rem;">
                  <img class="card-img-top" src="https://www.promobit.com.br/blog/wp-content/uploads/2021/06/15195956/ar/1200/kabum.jpg" style="width: 250px" alt="Card image cap">
                  <div class="card-body">
                    <h5 class="card-title">Olá, Seja bem vindo</h5>
                    <p class="card-text">SEU TOKEN ESTÁ ABAIXO</p>
                    <div class="row-3 mt-1">
                      <div class="col-14">
                        <td valign="center" align="center" height="55" style="background-color:#d8d8d8">{token2}</td>
                      </div>
                </div>
              </div>
            </div>
    </div>
    """
    msg = email.message.Message()
    msg['Subject'] = "NOVO TOKEN GERADO"
    msg['From'] = 'ianfk2019@gmail.com'
    msg['To'] = email_send
    password = 'Digite a senha do email aqui para a API conseguir enviar emails automaticos'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    messagebox.showinfo("LOJA DE ELETRÔNICOS", "Token enviado com sucesso para o email")


# Programa----------------------------------------------------

cor1 ='#040404' # preto
cor2 ='#f3c259' # amarelo
cor3 ='#484a83' # azul

janela = Tk() # Cria a janela
janela.title('Loja de Eletronicos') # Altera o titulo da janela
janela.geometry('500x300') # Altera o tamanho da janela
janela.config(bg=cor2) # Altera a cor de fundo da janela

janela.iconphoto(True, PhotoImage(file='imagens/icone_k.png')) # Altera o icon da janela
janela.resizable(width=False, height=False) # Impede que a janela possa mudar de tamanho 
# Funções e janelas
    
def janela3(): #menu Dono 1, Adicionar produto ou editar estoque
    janela_3 = Toplevel()
    janela_3.title('Loja de Eletronicos')
    janela_3.iconphoto(False, PhotoImage(file='imagens/icone_k.png'))
    janela_3.geometry('500x300')
    janela_3.config(bg=cor2) 
    janela_3.resizable(width=False, height=False)

    def janela4(): # Adicionar novo produto ao estoque/a tabela excel
        janela_4 = Toplevel()
        janela_4.geometry('600x250')
        janela_4.config(bg=cor2) 
        janela_4.resizable(width=False, height=False)
        janela_4.title('Loja de Eletronicos')

        Label(janela_4, width=22, height=2, text='Digite o nome do produto: ', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=0)
        entry_item = Entry(janela_4, width=10)
        entry_item.grid(row=1, column=0)

        Label(janela_4, width=20, height=2, text='Digite o preço: ', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=1)
        entry_preço = Entry(janela_4, width=10)
        entry_preço.grid(row=1, column=1)

        Label(janela_4, width=20, height=2, text='Digite a Quantidade: ', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=2)
        entry_quanti = Entry(janela_4, width=10)
        entry_quanti.grid(row=1, column=2)

        Label(janela_4, width=20, height=2, text='Digite imagem: ', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=3)
        entry_img = Entry(janela_4, width=10)
        entry_img.grid(row=1, column=3)

        def adicionar(): # Função para adicionar o produto
                    tabela = pd.read_excel("banco/Produtos.xlsx")
                    produto = entry_item.get()
                    preço = entry_preço.get()
                    quantidade = entry_quanti.get()
                    imagem = entry_img.get()

                    if (tabela['Produto'] == produto).any(): # Se o produto já existir então não é adicionado
                        messagebox.showwarning("PRESTE ATENÇÃO!!!", "O PRODUTO JÁ EXISTE NO ESTOQUE!!!")
                    else:     
                        if (entry_img.get() != '') and (preço.replace('.','',1).isdigit()) and (entry_quanti.get() != '' and entry_quanti.get().isdigit()) and (entry_preço.get() != ''):
                            preço2 = float(preço)
                            tabela = tabela.append({'Produto' : produto, 'Preço' : preço2,'Qt estoque': quantidade,'Imagem': imagem} , ignore_index=True)
                            tabela.to_excel("banco/Produtos.xlsx", index=False)
                            messagebox.showinfo("LOJA DE ELETRÔNICOS", "Produto adicionado com sucesso!")
                        else:
                            messagebox.showwarning("PRESTE ATENÇÃO!!!", "Se você inserir letras nas colunas de preço ou estoque ou se você não inserir nada, o produto não será adicionado ao estoque.")

        Button(janela_4,command=adicionar, width=10, height=2, text='Adicionar', font='Arial 11', fg= cor1, bg=cor2).place(x=260, y=100)
        janela_4.mainloop()
        
    def janela5(): # Menu Dono edições estoque
            janela_5 = Toplevel()
            janela_5.geometry('600x300')
            janela_5.config(bg=cor2) 
            janela_5.resizable(width=False, height=False)
            janela_5.title('Loja de Eletronicos')

            def janela6(): # deletar algum produto
                janela_6 = Toplevel()
                janela_6.geometry('500x150')
                janela_6.config(bg=cor2) 
                janela_6.resizable(width=False, height=False)
                janela_6.title('Loja de Eletronicos')

                Label(janela_6, width=20, height=2, text='Informe o produto: ', bg=cor2, fg=cor1, font='Arial 8 bold').pack()
                entry_prod = Entry(janela_6, width=10)
                entry_prod.pack()

                def deletar(): # Função para deletar o produto
                    tabela = pd.read_excel("banco/Produtos.xlsx")
                    pdel = entry_prod.get()
                    if (tabela['Produto'] == pdel).any():
                        indexNames = tabela[tabela['Produto']== pdel].index
                        tabela.drop(indexNames, inplace = True)
                        tabela.to_excel("banco/Produtos.xlsx", index=False)
                        messagebox.showinfo("LOJA DE ELETRONICOS", "Produto removido com sucesso!")
                    else: messagebox.showerror("PRESTE ATENÇÃO!!!", "O produto informado não existe no estoque!")
                Button(janela_6,command=deletar, width=20, height=2, text='Deletar Produto', font='Arial 9', fg= cor1, bg=cor2).pack(pady=20)

                janela_6.mainloop()


            def janela7(): # Mostrar o estoque
                janela_7 = Toplevel()
                janela_7.geometry('800x500')
                janela_7.config(bg=cor2) 
                janela_7.resizable(width=False, height=False)
                tabela = pd.read_excel("banco/Produtos.xlsx")
                janela_7.title('Loja de Eletronicos (ESTOQUE)')
                if (len(tabela_vendas) > 0):
                    main_frame = Frame(janela_7)
                    main_frame.pack(fill=BOTH, expand=1)
                    main_frame.config(bg=cor2)
                    # Cria uma janela
                    my_canvas = Canvas(main_frame)
                    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                    my_canvas.config(bg=cor2)
                    # Add uma scrollbar a janela
                    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
                    my_scrollbar.pack(side=RIGHT, fill=Y)

                    # Configura o Canvas
                    my_canvas.configure(yscrollcommand=my_scrollbar.set)
                    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

                    # Crie OUTRO quadro DENTRO do Canvas
                    second_frame = Frame(my_canvas)
                    second_frame.config(bg=cor2)
                    # Adicione esse novo frame a uma janela na tela
                    my_canvas.create_window((100,0), window=second_frame, anchor="nw")
                    Label(second_frame, width=22, height=2, text='PRODUTO', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=0)
                    Label(second_frame, width=20, height=2, text='PREÇO', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=1)
                    Label(second_frame, width=20, height=2, text='ESTOQUE', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=2)
                    Label(second_frame, width=20, height=2, text='IMAGEM', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=3)
                    for i in range(len(tabela)):
                        Label(second_frame, width=20, height=1, text=tabela['Produto'][i], bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=i+1, column=0)
                        Label(second_frame, width=20, height=1, text=(f"R${tabela['Preço'][i]: .2f}"), bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=i+1, column=1)
                        Label(second_frame, width=20, height=1, text=tabela['Imagem'][i], bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=i+1, column=3)   
                        if(tabela["Qt estoque"][i] <= 20):
                            Label(second_frame, width=20, height=1, text=(f"{tabela['Qt estoque'][i]} Und"), bg=cor2, fg='red', font='Arial 8 bold').grid(row=i+1, column=2)
                        else: Label(second_frame, width=20, height=1, text=(f"{tabela['Qt estoque'][i]} Und"), bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=i+1, column=2)
                    for j in range(len(tabela)):
                        if(tabela["Qt estoque"][j] <= 20): 
                            messagebox.showwarning("PRESTE ATENÇÃO!!!", f"O estoque de {tabela['Produto'][j]} está precisando de reposição")
                janela_7.mainloop()

            def janelaedit(): # Janela para editar produtos
                janela_edit = Toplevel()
                janela_edit.geometry('600x250')
                janela_edit.config(bg=cor2) 
                janela_edit.resizable(width=False, height=False)
                janela_edit.title('Loja de Eletronicos')
                messagebox.showwarning("PRESTE ATENÇÃO!!!", "Se você inserir letras nas colunas de preço ou estoque, a alteração não será feita no banco de dados")
                Label(janela_edit, width=22, height=2, text='Digite o novo nome', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=0)
                entry_new = Entry(janela_edit, width=10)
                entry_new.grid(row=1, column=0)

                Label(janela_edit, width=20, height=2, text='Digite o novo preço:', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=1)
                entry_preço = Entry(janela_edit, width=10)
                entry_preço.grid(row=1, column=1)

                Label(janela_edit, width=20, height=2, text='Digite a nova quantidade:', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=2)
                entry_quanti = Entry(janela_edit, width=10)
                entry_quanti.grid(row=1, column=2)

                Label(janela_edit, width=20, height=2, text='Digite a nova imagem:', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=3)
                entry_img = Entry(janela_edit, width=10)
                entry_img.grid(row=1, column=3)

                Label(janela_edit, width=20, height=2, text='Produto que deseja editar:', bg=cor2, fg=cor1, font='Arial 8 bold').place(x=250, y= 130)
                entry_item = Entry(janela_edit, width=20)
                entry_item.place(x=250, y= 160)

                def editar(): # Função para editar os produtos
                    tabela = pd.read_excel("banco/Produtos.xlsx")
                    nome = entry_item.get()
                    preço = entry_preço.get()
                    if (tabela['Produto'] == nome).any():
                        if ((entry_img.get() == '') and (preço == '') and (entry_quanti.get()) == '' and (entry_new.get() == '')):
                            messagebox.showwarning("PRESTE ATENÇÃO!!!", "Você não pode deixar todos os campos de edição vazios")
                        else:
                            if (entry_img.get() != ''):
                                tabela.loc[tabela["Produto"]==nome, "Imagem"] = entry_img.get()
                            
                            if (preço != '' and preço.replace('.','',1).isdigit()):
                                preço2 = float(preço)
                                tabela.loc[tabela["Produto"]==nome, "Preço"] = preço2

                            if (entry_quanti.get() != '' and entry_quanti.get().isdigit()):
                                tabela.loc[tabela["Produto"]==nome, "Qt estoque"] = int(entry_quanti.get())

                            if(entry_new.get() != ''):
                                tabela.loc[tabela["Produto"]==nome, "Produto"] = entry_new.get()
                            messagebox.showinfo("LOJA DE ELETRONICOS", "Produto editado com sucesso!")
                            tabela.to_excel("banco/Produtos.xlsx", index=False)
                    else: messagebox.showerror("PRESTE ATENÇÃO", "Este produto não existe no estoque")
                    
                Button(janela_edit,command=editar, width=10, height=2, text='Editar', font='Arial 11', fg= cor1, bg=cor2).place(x=250, y= 80)

            def h_vendas(): # Mostrar historico de vendas
                janela_h = Toplevel()
                janela_h.geometry('800x500')
                janela_h.config(bg=cor2) 
                janela_h.resizable(width=False, height=False)
                tabela_vendas = pd.read_excel("banco/historico_vendas.xlsx")
                janela_h.title('Loja de Eletronicos')
                if (len(tabela_vendas) > 0):
                    main_frame = Frame(janela_h)
                    main_frame.pack(fill=BOTH, expand=1)
                    main_frame.config(bg=cor2)

                    my_canvas = Canvas(main_frame)
                    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                    my_canvas.config(bg=cor2)

                    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
                    my_scrollbar.pack(side=RIGHT, fill=Y)

                  
                    my_canvas.configure(yscrollcommand=my_scrollbar.set)
                    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

                  
                    second_frame = Frame(my_canvas)
                    second_frame.config(bg=cor2)
                    
                    my_canvas.create_window((100,0), window=second_frame, anchor="nw")
                    Label(second_frame, width=22, height=2, text='USUARIO', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=0)
                    Label(second_frame, width=20, height=2, text='PRODUTO', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=1)
                    Label(second_frame, width=20, height=2, text='PREÇO', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=2)
                    Label(second_frame, width=20, height=2, text='DATA', bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=0, column=3)
                    for i in range(len(tabela_vendas)):
                        Label(second_frame, width=20, height=1, text=tabela_vendas['Usuario'][i], bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=i+1, column=0)
                        Label(second_frame, width=20, height=1, text=tabela_vendas['Produto'][i], bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=i+1, column=1)
                        Label(second_frame, width=20, height=1, text=(f"R${tabela_vendas['Preço'][i]:.2f}"), bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=i+1, column=2)
                        Label(second_frame, width=20, height=1, text=tabela_vendas['Data'][i], bg=cor2, fg=cor1, font='Arial 8 bold').grid(row=i+1, column=3)
                else:
                    Label(janela_h, width=60, height=20, text="NENHUMA VENDA REALIZADA", bg=cor2, fg=cor1, font='Arial 12 bold').pack()
                    messagebox.showinfo("ATENÇÃO", "A loja ainda não realizou nenhuma venda")
                janela_h.mainloop()
            def mais_est():
                janela_mais = Toplevel()
                janela_mais.geometry('800x500')
                janela_mais.config(bg=cor2) 
                janela_mais.resizable(width=False, height=False)
                janela_mais.title('Loja de Eletronicos (ESTOQUE)')
                tabela = pd.read_excel("banco/Produtos.xlsx")
                Label(janela_mais, width=20, height=2, text='Informe o produto: ', bg=cor2, fg=cor1, font='Arial 8 bold').pack()
                entry_prop = Entry(janela_mais, width=10)
                entry_prop.pack()
                Label(janela_mais, width=30, height=2, text='Informe as unidades adicionais: ', bg=cor2, fg=cor1, font='Arial 8 bold').pack()
                entry_und = Entry(janela_mais, width=10)
                entry_und.pack()
                def altestoque():
                    prop = entry_prop.get()
                    und = entry_und.get()
                    if (prop != '' and und != ''):
                        if (tabela['Produto'] == prop).any():
                            if(und.isdigit()):
                                tabela.loc[tabela["Produto"]==prop, "Qt estoque"] += int(und)
                                tabela.to_excel("banco/Produtos.xlsx", index=False)
                                messagebox.showinfo("LOJA DE ELETRONICOS", "Unidades adicionadas com sucesso")
                            else: messagebox.showerror("LOJA DE ELETRONICOS", "Por favor digite um valor válido para acrescentar ao produto")
                        else: messagebox.showerror("PRESTE ATENÇÃO!!!", "O produto informado não existe no estoque!")
                    else: messagebox.showerror("PRESTE ATENÇÃO!!!", "Por favor, não deixe nenhum dos campos em branco")
                Button(janela_mais,command=altestoque, width=20, height=2, text='Acrescentar no estoque', font='Arial 9', fg= cor1, bg=cor2).pack(pady=20)


            Button(janela_5,command=janelaedit, width=30, height=2, text='Editar um produto', font='Arial 9', fg= cor1, bg=cor2).pack(pady=10)
            
            Button(janela_5,command=janela6, width=30, height=2, text='Deletar um produto', font='Arial 9', fg= cor1, bg=cor2).pack(pady=10)

            Button(janela_5,command=janela7, width=30, height=2, text='Mostrar estoque', font='Arial 9', fg= cor1, bg=cor2).pack(pady=10)

            Button(janela_5,command=h_vendas, width=30, height=2, text='Mostrar histórico de vendas', font='Arial 9', fg= cor1, bg=cor2).pack(pady=10)

            Button(janela_5,command=mais_est, width=30, height=2, text='Aumentar o estoque de um produto', font='Arial 9', fg= cor1, bg=cor2).pack(pady=10)

            janela_5.mainloop()

    Button(janela_3,command=janela4, width=30, height=2, text='Adicionar Novo Produto', font='Arial 11', fg= cor1, bg=cor2).pack(pady=20)

    Button(janela_3,command=janela5, width=30, height=2, text='Editar estoque', font='Arial 11', fg= cor1, bg=cor2).pack(pady=20)


    janela_3.mainloop()
    

def janela2(): # Janela de Validação do dono
    enviar_email()
    janela_2 = Toplevel()
    janela_2.geometry('500x300')
    janela_2.config(bg=cor2) 
    janela_2.resizable(width=False, height=False)
    janela_2.title('VALIDANDO O PROPRIETARIO')
    janela_2.iconphoto(False, PhotoImage(file='imagens/icone_k.png'))
    Label(janela_2, width=25, height=2, text='Token de Confirmação: ', bg=cor2, fg=cor1, font='Arial 11 bold').pack()
    login_entry = Entry(janela_2, width=25)
    login_entry.pack(pady=5)

    Button(janela_2,command=janela_2.destroy, width=5, height=2, text='Sair', font='Arial 11', fg= cor1, bg=cor2).place(x=10, y=240)
    
    def confirmar():
        token = login_entry.get()
        token_fim = str(token2)
        if (token == token_fim):
            janela_2.destroy()
            janela3()
        elif(token != token_fim):
            messagebox.showerror("PRESTE ATENÇÃO!!!", "O token informado está incorreto")


    Button(janela_2,command=confirmar, width=10, height=2, text='Confirmar', font='Arial 11', fg= cor1, bg=cor2).pack(pady=10)

    login_erro = Label(janela_2, width=30, height=2, text='', bg=cor2, fg=cor1, font='Arial 11 bold')
    login_erro.pack()
    janela_2.mainloop()
#===========================================JANELA DE COMPRADOR===================================================
def janela_buy():
    tabela = pd.read_excel("banco/Produtos.xlsx")
    janela_buy = Toplevel()
    janela_buy.geometry('700x350')
    janela_buy.config(bg=cor2) 
    janela_buy.resizable(width=False, height=False)
    janela_buy.title('Loja de Eletronicos')
    
    
    main_frame = Frame(janela_buy)
    main_frame.pack(fill=BOTH, expand=1)
    main_frame.config(bg=cor2)
    # Cria uma janela
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_canvas.config(bg=cor2)
    # Adiciona a scrollbar a janela
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    # Configura a janela
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    # Crie OUTRO quadro DENTRO do Canvas
    second_frame = Frame(my_canvas)
    # Add um novo frame na janela do Canvas
    my_canvas.create_window((300,0), window=second_frame, anchor="nw")
    second_frame.configure(bg=cor2)
    imagembuy = PhotoImage(file="imagens/buy-icon-free-vector.png")
    imagem_produto = ""
    if (len(tabela) > 0):
        for thing in range(len(tabela)):
            price = tabela['Preço'][thing]
            imagem = tabela['Imagem'][thing]
            fileName = ("imagens/"+imagem+".png")
            fileObj = Path(fileName)
            if thing > 0:
                Label(second_frame, bg=cor2).pack()
            if(tabela['Qt estoque'][thing] > 0):
                if(fileObj.is_file() == True):
                    imagem_produto = PhotoImage(file="imagens/"+imagem+".png")
                elif(fileObj.is_file() == False):
                    imagem_produto = PhotoImage(file="imagens/not_found.png")
                w = Label(second_frame, width=150, height=150, image=imagem_produto)
                w.imagem = imagem_produto
                w.pack()
                Label(second_frame, width=15, height=1, text=(f'{tabela["Produto"][thing]}'), bg=cor2, fg=cor1, font='Arial 10 bold').pack()
            else:
                imagem_produto = PhotoImage(file="imagens/not_found.png")
                w = Label(second_frame, width=100, height=100, image=imagem_produto)
                w.imagem = imagem_produto
                w.pack() 
                Label(second_frame, width=20, height=1, text=(f'UNIDADES ESGOTADAS'), bg=cor2, fg='red', font='Arial 10 bold').pack()
                
            Label(second_frame, width=15, height=1, text=(f'Preço: R${price: .2f}'), bg=cor2, fg=cor1, font='Arial 10 bold').pack()
        Label(my_canvas, width=15, text='PRODUTO:', bg=cor2, fg=cor1, font='Arial 11 bold').pack(side= LEFT, padx=10)
        Label(my_canvas, width=15, text='USUARIO:', bg=cor2, fg=cor1, font='Arial 11 bold').place(x=6,y=185)
        nome_produto = Entry(my_canvas, width=15)
        nome_produto.pack(side= LEFT, padx=5)
        nome_user = Entry(my_canvas, width=15)
        nome_user.place(x=166,y=185)
        def comprar():
            tabela_vendas = pd.read_excel("banco/Historico_vendas.xlsx")
            tabela = pd.read_excel("banco/Produtos.xlsx")
            prod = nome_produto.get()
            user = nome_user.get()
            if (prod != '' and user != ''):
                if (tabela['Produto'] == prod).any():
                    estoque = int(tabela.loc[tabela["Produto"]==nome_produto.get(), "Qt estoque"])
                    if estoque > 0:
                        Preço = float(tabela.loc[tabela["Produto"]==nome_produto.get(), "Preço"])
                        tabela.loc[tabela["Produto"]==nome_produto.get(), "Qt estoque"] -= 1
                        tabela_vendas = tabela_vendas.append({'Produto' : nome_produto.get(), 'Usuario' : nome_user.get(), 'Preço': Preço, 'Data': data} , ignore_index=True)
                        tabela_vendas.to_excel("banco/Historico_vendas.xlsx", index=False)
                        tabela.to_excel("banco/Produtos.xlsx", index=False)
                        messagebox.showinfo("PARABENS", "Produto comprado com sucesso")
                    else: messagebox.showerror("PRESTE ATENÇÃO!!!", "Produto sem estoque")
                else:
                    messagebox.showerror("PRESTE ATENÇÃO!!!", "Não temos este produto em nossa loja!!")
            elif(prod == '' or user == ''):
                messagebox.showwarning("PRESTE ATENÇÃO!!!", "Não deixe o campo do produto ou nome em branco")
        Button(my_canvas,command=comprar, width=30, height=30, image=imagembuy).place(x=263,y=166)
    else:
        imagem_zero = PhotoImage(file="imagens/porta-fechada.png")
        img0 = Label(my_canvas, width=700, height=350, image=imagem_zero, bg='white')
        img0.imagem = imagem_produto
        img0.pack()
    janela_buy.mainloop()

Button(janela,command=janela2, width=10, height=2, text='Dono', font='Arial 11', fg= cor1, bg=cor2).place(x=200, y= 80)
Button(janela,command=janela_buy, width=10, height=2, text='Comprador', font='Arial 11', fg= cor1, bg=cor2).place(x=200, y= 180)
Button(janela,command=janela.destroy, width=5, height=2, text='Sair', font='Arial 11', fg= cor1, bg=cor2).place(x=10, y=240)
janela.mainloop()
