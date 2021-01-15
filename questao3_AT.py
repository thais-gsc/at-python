def saude_financeira():
    
    #receber os dados de renda e gastos do usuário
    renda_total = float(input("Informe sua renda mensal total: "))
    moradia = float(input("Informe seus gastos mensais com moradia: "))
    educacao = float(input("Informe seus gastos mensais com educação: "))
    transporte = float(input("Informe seus gastos mensais com transporte: "))
    
    #calcular a porcentagem de cada um dos gastos em relação à renda total
    percentual_moradia = (moradia/renda_total)*100 
    percentual_educ = (educacao/renda_total)*100
    percentual_transp = (transporte/renda_total)*100
    
    #arredondar para 2 casas decimais
    percentual_moradia = round(percentual_moradia,2)
    percentual_educ = round(percentual_educ,2)
    percentual_transp = round(percentual_transp,2)
    
    #calcular qual deveria ser o máximo de cada gasto em relação à renda total
    max_moradia = renda_total*0.3
    max_educ = renda_total*0.2
    max_transp = renda_total*0.15
    
    #arredondar para 2 casas decimais
    max_moradia = round(max_moradia,2)
    max_educ = round(max_educ,2)
    max_transp = round(max_transp,2)
    
    print(f"\nDiagnóstico:")
    print(f"Sua renda total é R${renda_total}.\n")
    
    #verificar se estão acima do máximo ideal (30%, 20% e 15%, respectivamente)
    print(f"Seus gastos mensais com moradia equivalem a {percentual_moradia}% da sua renda total. O máximo recomendado é de 30%.", end=' ')
    if percentual_moradia > 30:
        print(f"Idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {max_moradia}.")
    else:
        print("Seus gastos estão dentro da margem recomendada.")
        
    print(f"Seus gastos mensais com educação equivalem a {percentual_educ}% da sua renda total. O máximo recomendado é de 20%.", end = ' ')
    if percentual_educ > 20:
        print(f"Idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {max_educ}.")
    else:
        print("Seus gastos estão dentro da margem recomendada.")
    
    print(f"Seus gastos mensais com transporte equivalem a {percentual_transp}% da sua renda total. O máximo recomendado é de 15%.", end = ' ')
    if percentual_transp > 15:
        print(f"Idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {max_transp}.")
    else:
        print("Seus gastos estão dentro da margem recomendada.")