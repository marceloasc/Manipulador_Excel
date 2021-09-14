from tkinter import *


def Tela_Excluir():
    janela = Tk()
    janela.geometry("600x300")
    janela.title("Excluir")

    texto_informar_itens = Label(janela,
    text="Informe o numero da linha que será excluida: ", fg='#808080')
    texto_informar_itens.place(relx=0.10, rely=0.1)
    texto_informar_itens.config(font=("Ubuntu", 14))

    entrada = Entry(janela)
    entrada.place(relx=0.1, rely=0.25, relwidth=0.2, relheight=0.08)

    excluir = Button(janela, text="Excluir",
    activebackground='#345',
    activeforeground='white')
    excluir.place(relx=0.10, rely=0.60)


    janela.mainloop()


Tela_Excluir()
