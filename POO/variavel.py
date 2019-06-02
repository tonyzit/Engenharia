
##Bibliotecas necessárias
from prettytable import *
import os
##Interface utilizada pelas classes
class variavel():
    def calcular(self):
        pass

    def converter(self):
        pass

    def imprimeTabela(self):
        x = PrettyTable(self.unidadesMedida)
        tam = len(self.unidadesMedida)
        for i in range(1, tam):
            valor = list(range((tam-1)*(i-1)+1, (tam-1)*i+1))
            valor.insert(0, self.unidadesMedida[i])
            x.add_row(valor)
        x.set_style(MSWORD_FRIENDLY)
        print(x, "\n")