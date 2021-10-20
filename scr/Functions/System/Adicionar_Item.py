from openpyxl import Workbook, load_workbook


def Adicionar_Item(caminho, entrada):
    item = entrada[0:-3]
    coluna = entrada[-2]
    linha = entrada[-1]

    wb = load_workbook(caminho)
    ws = wb.active

    ws[f'{coluna}'+f'{linha}'] = item

    wb.save(caminho)




