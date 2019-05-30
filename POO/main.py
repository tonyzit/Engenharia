##Importa as os modulos contendo as classes do projeto
from pressao import *
from vazao import *
from nivel import *
from temperatura import *

##Menu Principal
def maind():
    print("Adams Siderúrgica S/A\n")
    print("1. Converter unidades de medida de pressao")
    print("2. Converter unidades de medida de Vazão Volumétrica")
    print("3. Calcular Pressão")
    print("4. Calcular Pressão Dinâmica")
    print("5. Calcular Vazão Volumétrica")
    print("6. Calcular Vazão Mássica")
    print("7. Converter temperatura")
    print("8. Calcular Nivel")
    escolha = int(input("\nDigite o número relacionado com a opção desejada:"))
    if escolha == 1:
        press = Pressao()
        press.converter()
    elif escolha == 2:
        vaz = volumetrica()
        vaz.converter()
    elif escolha == 3:
        press = Pressao()
        press.calcular()
    elif escolha == 4:
        p = dinamica()
        p.calcular()
    elif escolha == 5:
        vaz = volumetrica()
        vaz.calcular()
    elif escolha == 6:
        vaz = massica()
        vaz.calcular()
    elif escolha == 7:
        temp = Temperatura()
        temp.converter()
    elif escolha == 8:
        altura = input("\nDigite a altura do conteudo: ")
        areaBase = input("Digite a área da base do reservatório: ")
        niv = Nivel(areaBase,altura)
        niv.calcular()
    
    

if __name__ == "__main__":
    maind()
    
