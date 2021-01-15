def juros_compostos():
    
    #receber os valores do usuário
    valor_inicial = float(input("Informe o valor inicial: "))
    rendimento = float(input("Informe o rendimento por período (%): "))
    aporte = float(input("Informe o valor do aporte a cada período: "))
    periodos = int(input("Informe a quantidade de períodos: "))
    
    #converter a porcentagem
    rendimento = rendimento*0.01
    
#montante no primeiro mês = valor_inicial*(1 + rendimento) + aporte

#montante no segundo mês = montante*(1 + rendimento) + aporte
#montante no segundo mês = (valor_inicial*(1 + rendimento) + aporte)*(1 + rendimento) + aporte
#montante no segundo mês = valor_inicial*((1 + rendimento)**2) + aporte*(1 + rendimento) + aporte

#montante = valor_inicial*((1 + rendimento)**periodos) + aporte*((1 + rendimento)**(range(periodos - 1))
    
    
    contador = 0
    
    #calcula primeiro mês
    montante = valor_inicial*(1 + rendimento) + aporte
    print(f"Após {contador+1} períodos, o montante será de R${round(montante,2):.2f}.")
    
    #a partir do segundo mês, multiplica (periodos - 1) vezes
    for contador in range(0, (periodos-1)):
        montante =  montante*(1 + rendimento) + aporte
        print(f"Após {contador+2} períodos, o montante será de R${round(montante,2):.2f}.")
