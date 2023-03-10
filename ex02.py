print('Sequência de Fibonacci')

valor = int(input('Digite um número para testar  '))

t1 = 0
t2 = 1
t3 = 0

print('calculando...')

cont = 0

while cont < 100:
   t3 = t1 + t2
   t1 = t2
   t2 = t3
   cont += 1
   if valor==t3:
    print('{} esta incluso na sequencia de fibonnaci'.format(valor))
print('-> FIM')


