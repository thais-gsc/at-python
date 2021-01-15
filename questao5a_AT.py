def projecao_pib():
    
    #abre o arquivo e separa os elementos em uma lista
    planilha = open("Assessment_PIBs - Planilha1.csv", 'r')
    projecoes = planilha.read()
    projecoes = projecoes.splitlines()
    
    #separa os elementos da primeira lista como outra lista
    anos = projecoes[0]
    anos = anos.split(',')
    del(anos[0]) #remove o elemento 'País'
    
    pibs = []
    
    #separa a lista inteira em listas separadas para cada país
    for i in range(1,len(projecoes)):
        p = projecoes[i]
        dados = p.split(',')
        pibs.append(dados)
    
    paises = []
    
    #adiciona apenas os primeiros elementos, no caso, os países
    for j in range(len(pibs)):
        paises.append(pibs[j][0])
        
    #remove os nomes dos países da lista de PIBs    
    for i in range(len(pibs)):
        del(pibs[i][0])
    
    #recebe as entradas do usuário e repete até receber uma entrada válida
    pais = input("Informe um país: ")
    
    while pais not in paises:
        print("País indisponível.")
        pais = input("Informe um país: ")
        
    ano = input("Informe um ano entre 2013 e 2020: ")
    
    while ano not in anos:
        print("Ano inválido.")
        ano = input("Informe um ano entre 2013 e 2020: ")
    
    #encontra na lista completa de PIBs o país escolhido
    indice1 = paises.index(pais)
    
    #dentro da lista do país, encontra o ano escolhido
    indice2 = anos.index(ano)
        
    print(f"Projeção do PIB de {pais} para o ano de {ano}: US${pibs[indice1][indice2]} trilhões")
    
