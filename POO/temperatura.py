from variavel import *

class Temperatura(variavel):
    
    def converter(self):
        print("Digite o valor da temperatura e sua unidade original(Ex. 56 c): ")
        ent = input().split()
        temp = int(ent[0])
        unidade = ent[1].lower()
        if unidade == 'c':
            tempc = temp
        elif unidade == 'f':
            tempc = (temp-32)/1.8
        elif unidade == 'k':
            tempc = (temp-273)
        elif unidade == 'r':
            tempc = (temp - 491)/1.8
        print("K : Kelvin\nC : Celsius\nF : Farenheit\nR : Rankine")
        print("Digite a unidade desejada de conversão: ")
        uniSaida = input().lower()
        if uniSaida == 'c':
            temp = tempc
        elif uniSaida == 'f':
            temp = tempc * 1.8 + 32
        elif uniSaida == 'k':
            temp = tempc + 273
        elif uniSaida == 'r':
            temp = temp * 1.8 + 491
        print("{:.1f}".format(temp), uniSaida)