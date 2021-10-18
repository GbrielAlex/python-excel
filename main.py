from Servico import Serviço
from openpyxl import load_workbook
from Tela import InterfarcePrincipal
from PySimpleGUI import *

atendimento = []
n = 0
cont = 1
finish = True
excell_file = load_workbook("planilhaClientes.xlsx")
aba_ativa = excell_file.active


for cell in aba_ativa["A"]:
    cont += 1

while finish:
    temp = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
    screen = InterfarcePrincipal()

    client = screen.get__values()["cliente"]
    professional = screen.get__values()["Atendente"]
    service = screen.get__values()["servico"]

    data = temp[0:10]
    hour = temp[11:]
    event, values = screen.janela.read()

    if event == WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        finish = False

    atendimento.append(Serviço(client, service, professional, data, hour))
    if finish:
        aba_ativa[f"A{cont}"] = atendimento[n].get__data()
        aba_ativa[f"B{cont}"] = atendimento[n].get__horario()
        aba_ativa[f"C{cont}"] = atendimento[n].get__nome_cliente()
        aba_ativa[f"D{cont}"] = atendimento[n].get__atendente()
        aba_ativa[f"E{cont}"] = atendimento[n].get__tipos_servico()

    excell_file.save("planilhaClientes.xlsx")
    cont += 1
    n += 1
    screen.janela.Close()
