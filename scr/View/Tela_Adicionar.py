from tkinter import *
from scr.Functions.Utils import Determinar_Local_de_Abertura as abrir


def Tela_Adicionar():
    janela = Tk()
    abrir.Centralizar(janela)
    janela.maxsize(600, 300)
    janela.minsize(600, 300)
    janela.title("Adicionar - manipulador excel")

    texto_informar_itens = Label(janela,
    text="Informe os itens que serão adicionados: ", fg='#808080')
    texto_informar_itens.place(relx=0.10, rely=0.1)
    texto_informar_itens.config(font=("Ubuntu", 14))

    entrada = Entry(janela)
    entrada.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.1)

    adicionar = Button(janela, text="Adicionar",
    activebackground='#345',
    activeforeground='white')
    adicionar.place(relx=0.10, rely=0.60)

    janela.mainloop()


