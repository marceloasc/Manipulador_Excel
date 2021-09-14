from tkinter import *


def Tela_Adicionar():
    janela = Tk()
    janela.geometry("600x300")
    janela.title("Adicionar")

    texto_informar_itens = Label(janela,
    text="Informe os itens que serão adicionados: ", fg='#808080')
    texto_informar_itens.place(relx=0.10, rely=0.1)
    texto_informar_itens.config(font=("Ubuntu", 14))

    entrada = Entry(janela)
    entrada.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.08)

    adicionar = Button(janela, text="Adicionar",
    activebackground='#345',
    activeforeground='white')
    adicionar.place(relx=0.10, rely=0.60)

    janela.mainloop()


Tela_Adicionar()
