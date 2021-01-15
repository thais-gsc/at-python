def variacao_pib():
    
    planilha = open("Assessment_PIBs - Planilha1.csv", 'r')
    projecoes = planilha.read()
    projecoes = projecoes.splitlines()
    
    pibs = []
    
    for i in range(1,len(projecoes)):
        p = projecoes[i]
        dados = p.split(',')
        pibs.append(dados)
    
    paises = []
    
    for j in range(len(pibs)):
        paises.append(pibs[j][0])
           
    for i in range(len(pibs)):
        del(pibs[i][0])
        
    variacoes = []
    
    #calcula a variação dos PIBS e adiciona à lista
    for i in range(len(pibs)):
        variacao = (float(pibs[i][7])/float(pibs[i][0]) - 1)*100
        variacao = round(variacao,2)
        variacoes.append(variacao)
        
    for pais in paises:
        print(f"{pais:30} \t Variação de {variacoes[paises.index(pais)]}%")
    