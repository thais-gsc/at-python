import matplotlib.pyplot as plt

def grafico_aplicacao():
    
    #receber os valores do usuário
    valor_inicial = float(input("Informe o valor inicial: "))
    rendimento = float(input("Informe o rendimento por período (%): "))
    aporte = float(input("Informe o valor do aporte a cada período: "))
    periodos = int(input("Informe a quantidade de períodos: "))
    
    rendimento = rendimento*0.01
    
    #criar listas
    valores = []
    tempo = []
    
    #calcula e adiciona o primeiro mês à lista
    montante = valor_inicial*(1 + rendimento) + aporte
    montante = round(montante,2)
    valores.append(montante)
    
    #calcula e adiciona do segundo mês em diante
    for contador in range(0, (periodos-1)):
        montante =  montante*(1 + rendimento) + aporte
        montante = round(montante,2)
        valores.append(montante)
        
    print(valores)
    
    #adiciona o número de períodos à lista
    for p in range(1,periodos+1):
        tempo.append(p)
        
    print(tempo)
       
    plt.plot(tempo, valores, 'r-')
    plt.title("Evolução do dinheiro aplicado")
    plt.xlabel("Períodos")
    plt.ylabel("Valor acumulado (R$)")
    plt.show()