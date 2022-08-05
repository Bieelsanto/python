from operator import index
from tokenize import Number


print('<==================>')
print('|Conversor de bases|')
print('<==================>')
print('Escreva um número: ')
n = input()
print('Qual a base do número digitado? [exemplo: 2]')
print('Base: ')
baseC=int(input())
print('Para qual base você deseja converter este número?')
print('Base: ')
base=int(input())
neg = False
if (int(n) == 0) or (int(n)==1):
    print(n)

if int(n)<0:
    n = n * -1
    neg = True

if baseC>base:
    res=''
    if int(n) < base:
        res = n
    else:
        c = False
        num = n
        while c == False:
            if  num//base > 1:
                res += str(int(num%base))
                num = num//base
                if num == base:
                    res += '0'
            else:
                res += '1'
                c = True
else:
    res=0
    exp=len(str(n))-1
    for x in range(len(str(n))):
        res += int(int(str(n)[x]) * (baseC**exp))
        exp-=1
print('<==================>')
print('O resultado é:')
if neg == False:
    print(res)
else:
    print('-',res)
print('<==================>')
    


