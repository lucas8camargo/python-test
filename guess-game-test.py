import random 

chances = 2 
PC = random.randint(0, 10) 

print('\nVoce tem tres chances\n')

Nj = int(input('Digite um numero de 0 a 10: '))

while chances != 0: 

	if Nj == PC:
		print('\nAcertou\n')		
		break
	else:
		print('\nErrou\n')
		Nj = int(input('Tente outro numero: '))		
	chances -= 1

print('\nFim de jogo\n')
print(f'Numero sorteado: {PC}')