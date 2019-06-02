from variavel import *

class Pressao(variavel):
    ## Inicia os valores de area e pressão
        
    unidadesMedida = [' ', 'Kgf/cm^2', 'Ibf/pol^2', 'BAR',
                      'Pol Hg', 'Pol H2O', 'ATM', 'mmHg', 'mmH2O', 'kpa']
    coeficientes = [1, 14.233, 0.9807, 28.96, 393.83, 0.9678, 735, 10003, 98.0665,
                    0.0703, 1, 0.0689, 2.036, 27.689, 0.068, 51.71, 70329, 6.895,
                    1.0197, 14.504, 1, 29.53, 401.6, 0.98692, 750.06, 10200, 100,
                    0.0345, 0.4911, 0.03386, 1, 13.599, 0.0334, 25.399, 345.40, 3.3863,
                    0.002537, 0.03609, 0.00249, 0.07348, 1, 0.002456, 1.8665, 25.399, 0.24884,
                    1.0332, 14.696, 1.0133, 29.921, 406.933, 1, 760.05, 10335, 101.325,
                    0.00135, 0.019337, 0.00133, 0.03937, 0.5354, 0.001316, 1, 13.598, 0.13332,
                    0.000099, 0.00142, 0.00098, 0.00289, 0.03937, 0.00009, 0.07353, 1, 0.0098,
                    0.010197, 0.14504, 0.01, 0.29539, 4.0158, 0.009869, 7.50062, 101.998, 1]
    ## Inicia os valores de area e pressão
    def __init__(self):
        self.area = 0.0
        self.pressao = 0.0
        
    def calcular(self, ver=0):
        forca = float(input('Digite o valor da força exercida: '))
        while self.area == 0.0:
            self.area = float(
                input('Forneça o valor da área em que a força irá atuar: '))
        self.pressao = forca/self.area
        if(ver == 1):
            return self.pressao
        print('Pressão: ', self.pressao)
        print('Deseja converter o valor da Pressão? \n')
        if(int(input("1. SIM \n\n0. NÃO\n"))):
            self.converter(1)


    def converter(self,ver=0):
        print("Converter unidades de medida de Pressão\n\n")
        self.imprimeTabela()
        print("O valor da coluna vertical é a unidade inicial.")
        print("A coluna na horizontal apresenta a unidade desejada.")
        escolha = int(
            input("\nDigite o número relacionado com a opção desejada: "))

        if(ver==0):
            self.pressao = float(input("Digite o valor inicial da conversão: "))
        conv = self.pressao * self.coeficientes[escolha-1]
        unSaida = escolha % 9
        print("Resultado da conversão: {0:.2f} {1} ".format(
            conv, self.unidadesMedida[9 if unSaida == 0 else unSaida]))

#Classe para casos de pressão dinâmica
class preDin(Pressao):
    def __init__(self):
        self.pressao = 0.0
        self.area = 0.0
    def calcular(self):
        print("1. SIM\n0. NÃO\n")
        s = int(input("Possui o valor da pressão estática? "))
        if(s==1):
            pres = float(input("Digite o valor da pressão estática: "))
        elif(s==0):
            pres = super().calcular(1) 
        vol = float(input("Digite o valor do volume: "))
        self.pressao = (pres*(vol**2))/2
        print("Pressão dinamica: ", self.pressao)