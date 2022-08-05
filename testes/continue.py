lista=[150, 1300, 100, 2000, 120]
vendedores=['João', 'Julia', 'Ana', 'José', 'Lucas']
meta=130

for venda in lista:
    if venda<meta:
        continue
    i=lista.index(venda)
    print(vendedores[i])