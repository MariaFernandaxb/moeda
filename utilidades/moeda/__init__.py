def aumentar(preco=0, taxa=0, formato=False):
    res = (preco * taxa /100) + preco
    return res if not formato else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100) 
    return res if not formato else moeda(res)
    
def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxa_a=10, taxa_r=5):
    traço()
    print('RESUMO DO VALOR'.center(30))
    traço()
    print(f'Valor analisado: \t{moeda(preco)}')
    print(f'Dobro do valor: \t{dobro(preco, True)}')
    print(f'Metade do valor: \t{metade(preco, True)}')
    print(f'Reduzido em {taxa_r}% \t{diminuir(preco, taxa_r,True)}')
    print(f'Acréscimo de {taxa_a}% \t{aumentar(preco, taxa_a, True)}')
    traço()

def traço():
    print('-='*17)