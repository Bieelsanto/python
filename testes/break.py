vendas=[150, 1300, 100, 2000, 120]
meta=130

for venda in vendas:
    if venda<meta:
        print('A loja não ganha bônus')
        break
    print(venda)