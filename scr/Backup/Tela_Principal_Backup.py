from tkinter import *
import scr.View.Tela_Adicionar as ta
import scr.View.Tela_Excluir as te

def Tela_Principal():
    janela = Tk()
    janela.geometry("800x300")
    janela.title("Manipulador Excel")

    texto_informar_caminho = Label(janela,
    text="Informe o caminho da planilha para iniciar as operações: ", fg='#808080')
    texto_informar_caminho.place(relx=0.10, rely=0.10)
    texto_informar_caminho.config(font=("Ubuntu", 14))

    entrada = Entry(janela)
    entrada.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.0600)

    adicionar = Button(janela, text="Adicionar Item",
    activebackground='#345',
    activeforeground='white', command=ta.Tela_Adicionar)
    adicionar.place(relx=0.10, rely=0.60)

    remover = Button(janela, text="Excluir Item",
           activebackground='#345',
           activeforeground='white', command=te.Tela_Excluir)

    remover.place(relx=0.28, rely=0.60)

    janela.mainloop()


Tela_Principal()
