from tkinter import *
from functools import partial

from scr.Functions.Utils import Determinar_Local_de_Abertura as abrir
from scr.Functions.System import Excluir_Item as remo


def EnviarDadosRemo(enviar, caminho, entrada):
    enviar['command'] = partial(remo.Excluir_Item, caminho, entrada)


def Tela_Excluir(caminho):
    janela = Tk()
    abrir.Centralizar(janela)
    janela.maxsize(600, 300)
    janela.minsize(600, 300)
    janela.title("Excluir - manipulador excel")

    texto_informar_itens = Label(janela,
    text="Coluna e linha: ", fg='#808080')
    texto_informar_itens.place(relx=0.10, rely=0.1)
    texto_informar_itens.config(font=("Ubuntu", 14))

    entrada_Item = Entry(janela)
    entrada_Item.place(relx=0.1, rely=0.25, relwidth=0.2, relheight=0.1)

    excluir = Button(janela, text="Excluir",
                     command=entrada_Item.bind("<Return>",
                                               (lambda event: EnviarDadosRemo(excluir, caminho, entrada_Item.get()))),
                     activebackground='#345',
                     activeforeground='white')
    excluir.place(relx=0.10, rely=0.60)

    janela.mainloop()


