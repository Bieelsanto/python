print('===================================')
algo = input('Digite algo aleatório: ')
print('===================================')
print('Informações do que você digitou:')
print('Qual o tipo?........{}'.format(type(algo)))
print('É tudo maiúsculo?...{}'.format(algo.isupper()))
print('É tudo minúsculo?...{}'.format(algo.islower()))
print('É tudo alfabeto?....{}'.format(algo.isalpha()))
print('É tudo número?......{}'.format(algo.isnumeric()))
print('É alfanumérico?.....{}'.format(algo.isalnum()))
print('É ilustrável?.......{}'.format(algo.isprintable()))
print('É capitalizado?.... {}'.format(algo.istitle()))
print('===================================')