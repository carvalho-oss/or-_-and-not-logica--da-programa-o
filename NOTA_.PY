import os
os.system ('cls')

nota= int(input('Digite sua nota:  '))

if nota > 0 and nota >= 10:
    print (f'{nota} está entre 0 e 10')
else:
    resultado = (' nao esta entre 0 e 10 ')