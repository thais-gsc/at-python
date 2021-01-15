import matplotlib.pyplot as plt

def grafico_pib():
    
    planilha = open("Assessment_PIBs - Planilha1.csv", 'r')
    projecoes = planilha.read()
    projecoes = projecoes.splitlines()
    
    anos = projecoes[0]
    anos = anos.split(',')
    del(anos[0])
    
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
    
    pais = input("Informe um país: ")
    
    while pais not in paises:
        print("País indisponível.")
        pais = input("Informe um país: ")
    
    indice1 = paises.index(pais)
    
    float_pibs = []
    
    for elemento in pibs[indice1]:
        elemento = float(elemento)
        float_pibs.append(elemento)
    
    plt.plot(anos, float_pibs)
    plt.title(f"Projeção do PIB de {pais} para os anos 2013 a 2020")
    plt.xlabel("Anos")
    plt.ylabel("PIB em trilhões de US$")
    plt.show()