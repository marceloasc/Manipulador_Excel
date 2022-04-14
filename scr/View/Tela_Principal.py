from tkinter import *
from functools import partial
from tkinter.filedialog import askopenfilename

from scr.View import Tela_Adicionar as ta
from scr.View import Tela_Excluir as te

from scr.Functions.Utils import Determinar_Local_de_Abertura as abrir


def PegarCaminhoAdd(add, entr):
    caminho = entr.replace("\\", "/")
    add['command'] = partial(ta.Tela_Adicionar, caminho)


def PegarCaminhoRemo(remo, entr):
    caminho = entr.replace("\\", "/")
    remo['command'] = partial(te.Tela_Excluir, caminho)


def Tela_Principal():
    janela = Tk()
    abrir.Centralizar(janela)
    janela.maxsize(800, 300)
    janela.minsize(800, 300)
    janela.title("Manipulador Excel")

    texto_informar = Label(janela,
    text="Selecione a planilha e inicie as operações: ", fg='#808080')
    texto_informar.place(relx=0.10, rely=0.10)
    texto_informar.config(font=("Ubuntu", 14))

    aviso = Label(janela,
    text="formatos aceitos: .xlsx, .xlsm, .xltx, .xltm ", fg='#808080')
    aviso.place(relx=0.10, rely=0.2)
    aviso.config(font=("Ubuntu", 12))

    caminho = []

    Selecionar_Planilha = Button(janela,
                               text="Selecionar planilha",
                               command=lambda: caminho.append(askopenfilename(filetypes=([("Arquivo Excel", "*.xlsx; *.xlsm *.xltx; *.xltm")]), title='Selecionar planilha')),
                               activebackground='#345',
                               activeforeground='white'
    )
    Selecionar_Planilha.place(relx=0.10, rely=0.40)

    adicionar = Button(janela,
                       text="Adicionar Item",
                       command=lambda: PegarCaminhoAdd(adicionar, caminho[-1]),
                       activebackground='#345',
                       activeforeground='white'
    )
    adicionar.place(relx=0.10, rely=0.65)

    remover = Button(janela, text="Excluir Item",
                     command=lambda: PegarCaminhoRemo(remover, caminho[-1]),
                     activebackground='#345',
                     activeforeground='white'
    )
    remover.place(relx=0.26, rely=0.65)

    janela.mainloop()



