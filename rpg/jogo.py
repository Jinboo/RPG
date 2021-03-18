from Personagens import ana
from Personagens import julia
from Personagens import leticia
from Personagens import mafe
from Personagens import mavi
from Personagens import pedro

def jogo():   
    personagens = ['ana', 'julia', 'leticia', 'mafe', 'mavi', 'pedro']

    total_fichas = {}
    ficha = {}
    for p in personagens:
        if p == 'ana':
            ficha = ana.ficha()
        elif p == 'julia':
            ficha = julia.ficha()
        elif p == 'leticia':
            ficha = leticia.ficha()
        elif p == 'mafe':
            ficha = mafe.ficha()
        elif p == 'mavi':
            ficha = mavi.ficha()
        elif p == 'pedro':
            ficha = pedro.ficha()

        total_fichas[p] = ficha

    print('P E R S O N A G E N S\n')

    for t in total_fichas:
        print('***********************************************\n')
        print('Nome: ' + total_fichas[t]['Nome'])
        print('Raça: ' + total_fichas[t]['Raça'])
        print('Classe: ' + total_fichas[t]['Classe'])
        print('Altura: ' + total_fichas[t]['Altura'])
        print('Idade: ' + total_fichas[t]['Idade'])
        print('\n')        
    
# Inicio
jogo()