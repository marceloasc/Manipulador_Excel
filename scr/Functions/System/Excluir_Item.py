from openpyxl import Workbook, load_workbook


def Excluir_Item(caminho, entrada):
    coluna = entrada[0]
    linha = entrada[1]

    wb = load_workbook(caminho)
    ws = wb.active

    ws[f'{coluna}' + f'{linha}'] = None

    wb.save(caminho)
