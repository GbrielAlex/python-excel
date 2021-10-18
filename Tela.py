from PySimpleGUI import *


class InterfarcePrincipal:
    def __init__(self):
        # layout

        theme('DefaultNoMoreNagging')
        layout = [
            [Text("Cliente", size=(9, 0)), Input(size=(15, 0), key="cliente", background_color="White")],
            [Text("Atendente", size=(9, 0)), Input(size=(15, 0), key="Atendente", background_color="White")],
            [Text("Serviços", size=(9, 0)), Multiline(size=(30, 5), key="servico", background_color="White")],
            [Button("Salvar", size=(7, 0)), Button("Cancelar", size=(7, 0), key="Cancel")]


        ]

        # janela
        self.janela = Window("1° OFICIO ",
                             layout,
                             background_color="DimGrey",
                             font=("Arial", 14),
                             button_color=("Black", "White"),
                             size=(500, 250),



                             )

        # Extrair dados da tela

        self.button, self.values = self.janela.Read()

    def get__values(self):
        return self.values
