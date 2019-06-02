from variavel import *

class Vazao(variavel):
    def __init__(self):
        ## Array contendo as unidades de medida utilizadas para conversão de unidades
        self.unidadesMedida = [" ", "m^3/h", "m^3/min", "m^3/s",
                          "GPM", "BPH", "BPD", "pé^3/h", "pé^3/min"]
        ## Array de coeficientes para conversão de unidades
        self.coeficientes = [1, 0.016667, 0.00027778, 4.40287, 6.28982, 150.956, 35.314, 0.588579,
                        60, 1, 0.016667, 2641721, 3773892, 9057.34, 2118.8802, 353147,
                        3600, 60, 1, 15850.33, 22643.35, 543440.7, 127132.81, 2118.884,
                        0.22712, 0.0037854, 0.00006309, 1, 1.42857, 34.2857, 8.0208, 0.13368,
                        0.158987, 0.0026497, 0.000044161, 0.7, 1, 24, 5.614583, 0.0935763,
                        0.0066245, 0.00011041, 0.00000184, 0.029167, 0.041667, 1, 0.23394, 0.0038990,
                        0.0283168, 0.00047195, 0.0000078657, 0.124676, 0.178108, 4.2746, 1, 0.016667,
                        1.69901, 0.028317, 0.00047195, 7.480519, 10.686, 256.476, 60, 1]

    def converter(self,vazao=None):  # Método para a conversão de Vazão
            print("Converter unidades de medida de Vazão\n\n")
            self.imprimeTabela()
            print("O valor da coluna vertical é a unidade inicial.")
            print("A coluna na horizontal apresenta a unidade desejada.")
            escolha = int(
                input("\nDigite o número relacionado com a opção desejada: "))

            if(vazao == None):
                vazao = float(input("Digite o valor inicial da conversão: "))
            conv = vazao * self.coeficientes[escolha-1]
            unSaida = escolha % 8
            print("Resultado da conversão: {0:.2f} {1} ".format(
                conv, self.unidadesMedida[8 if unSaida == 0 else unSaida]))

## Classe de vazão mássica que herda caracteristicas da classe vazão
class massica(Vazao):
    def calcular(self):  # Método para cálculo da vazão mássica

        self.tempo = 0.0

        print("1. Para massa em razão do tempo.")
        print("2. Para produto da vazão volumétrica pela densidade.\n")
        a = int(input("\nInforme como deseja calcular a Vazão Mássica: "))

        if a == 1:
            os.system("cls")
            self.massa = float(
                input("informe o valor da massa em kilogramas(kg): "))
            while self.tempo == 0.0:
                self.tempo = float(
                    input("Informe o valor do tempo em segundos(s): "))
            self.vazao = self.massa/self.tempo
            print("O valor da vazão mássica é: {0} kg/s\n".format(self.vazao))
        elif a == 2:
            os.system("cls")
            print("1. SIM\n0. NÃO")
            if(int(input("\nPossui o valor da vazão volumetrica?: "))):
                self.vazvol = float(
                    input("\nDigite o valor da vazão volumétrica:"))
            else:
                os.system("cls")
                self.vazvol = volumetrica().calcular(1)
            densidade = float(input("\nDigite o valor da densidade:"))
            vazao = self.vazvol*densidade

            print("O valor da Vazão Mássica é: {0} kg/s ".format(vazao))


## Classe de vazão volumétrica que herda caracteristicas da classe vazão
class volumetrica(Vazao):
    def calcular(self,ver=0):  # Método para cálculo da vazão volumétrica
        tempo = 0.0
        print("1. Para volume em razão do tempo.\n")
        print("2. Para velocidade da vazão multiplicada pela área da seção transversal.")
        a = int(input("Informe como deseja calcular a Vazão Volumétrica: "))
        if a == 1:
            volume = float(
                input("informe o valor do volume em metros cúbicos(m³): "))
            while tempo == 0.0:
                tempo = float(
                    input("Informe o valor do tempo em segundos(s): "))
                vazao = volume/tempo
        elif a == 2:
            velocidade = float(input("informe a velocidade da vazão em m/s: "))
            area = float(input("Informe a área de seção transversal em m²: "))
            vazao = velocidade*area
        if ver == 1:
            return vazao
        print("O valor da vazão volumétrica é:{0} m³/s ", vazao)

        print('Deseja converter o valor da vazão? \n')
        if(int(input("1. SIM \n\n0. NÃO\n"))):
            os.system("cls")
            self.converter(vazao)
        else:
            os.system('cls')
