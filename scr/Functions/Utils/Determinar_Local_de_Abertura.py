def Centralizar(janela):
    Largura_Tela = janela.winfo_reqwidth()
    Altura_Tela = janela.winfo_reqheight()

    pos_Direita = int(janela.winfo_screenwidth() / 3 - Largura_Tela)
    pos_Baixo = int(janela.winfo_screenheight() / 2 - Altura_Tela)

    return janela.geometry("+{}+{}".format(pos_Direita, pos_Baixo))

