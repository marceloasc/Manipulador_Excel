from tkinter import *
from scr.Functions.Utils import Determinar_Local_de_Abertura as abrir


def Tela_Excluir():
    janela = Tk()
    abrir.Centralizar(janela)
    janela.maxsize(600, 300)
    janela.minsize(600, 300)
    janela.title("Excluir - manipulador excel")

    texto_informar_itens = Label(janela,
    text="Informe o numero da linha que será excluida: ", fg='#808080')
    texto_informar_itens.place(relx=0.10, rely=0.1)
    texto_informar_itens.config(font=("Ubuntu", 14))

    entrada = Entry(janela)
    entrada.place(relx=0.1, rely=0.25, relwidth=0.2, relheight=0.1)

    excluir = Button(janela, text="Excluir",
    activebackground='#345',
    activeforeground='white')
    excluir.place(relx=0.10, rely=0.60)

    janela.mainloop()


