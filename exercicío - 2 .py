import os
os.system('cls')

# ENTRADA.

primeiro_numero = int(input('Digite sua primeira nota:   '))
segundo_numero = int(input('Digite sua segunda nota;    '))
falta = int(input('Digite sua falta:    '))
media = (primeiro_numero + segundo_numero) / 2

#PROCESSAMENTO.

if media >= 7 and falta  <= 40:
    resultado = ( 'APROVADO')

else:
    resultado = ('REPROVADO')


# SAÍDA.

print(f'sua media foi: {media}')
print(f'sua quantidade de falta foi: {falta}')
print(f'primeira nota: {primeiro_numero}')
print(f'segunda nota: {segundo_numero}')
print(f'sua quantidade de falta {falta}')
print(resultado)