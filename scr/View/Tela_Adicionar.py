from tkinter import *
from functools import partial

from scr.Functions.Utils import Determinar_Local_de_Abertura as abrir
from scr.Functions.System import Adicionar_Item as add


def EnviarDadosAdd(enviar, caminho, entrada, janela):
    enviar['command'] = partial(add.Adicionar_Item, caminho, entrada, janela)


def Tela_Adicionar(caminho):
    janela = Tk()
    abrir.Centralizar(janela)
    janela.maxsize(600, 300)
    janela.minsize(600, 300)
    janela.title("Adicionar - manipulador excel")

    texto_informar_item = Label(janela,
    text="Item espaço coluna e linha e aperte ENTER: ", fg='#808080')
    texto_informar_item.place(relx=0.10, rely=0.1)
    texto_informar_item.config(font=("Ubuntu", 14))

    entrada_Item = Entry(janela)
    entrada_Item.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.1)

    adicionar = Button(janela, text="Adicionar",
                       command=entrada_Item.bind("<Return>",
                       (lambda event: EnviarDadosAdd(adicionar, caminho, entrada_Item.get(), janela))),
                       activebackground='#345',
                       activeforeground='white')
    adicionar.place(relx=0.10, rely=0.60)

    janela.mainloop()



