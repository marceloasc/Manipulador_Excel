from tkinter import *
from functools import partial

from scr.View import Tela_Adicionar as ta
from scr.View import Tela_Excluir as te
from scr.Functions.Utils import Determinar_Local_de_Abertura as abrir


def PegarCaminhoAdd(add, entr):
    caminho = entr.replace("\\", "/")
    add['command'] = partial(ta.Tela_Adicionar, caminho)


def Tela_Principal():
    janela = Tk()
    abrir.Centralizar(janela)
    janela.maxsize(800, 300)
    janela.minsize(800, 300)
    janela.title("Manipulador Excel")

    texto_informar_caminho = Label(janela,
    text="Informe o caminho junto ao nome do arquivo.xlsx e aperte ENTER: ", fg='#808080')
    texto_informar_caminho.place(relx=0.10, rely=0.10)
    texto_informar_caminho.config(font=("Ubuntu", 14))

    entrada = Entry(janela, font=("Ubuntu", 14))
    entrada.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.16)

    adicionar = Button(janela,
                       text="Adicionar Item",
                       command=entrada.bind("<Return>",
                                            (lambda event: PegarCaminhoAdd(adicionar, entrada.get()))),
                       activebackground='#345',
                       activeforeground='white'
    )
    adicionar.place(relx=0.10, rely=0.60)

    remover = Button(janela, text="Excluir Item",
                     command=te.Tela_Excluir,
                     activebackground='#345',
                     activeforeground='white'
    )
    remover.place(relx=0.28, rely=0.60)

    janela.mainloop()


Tela_Principal()
