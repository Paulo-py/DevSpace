# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

opcao = input("Escolha a operação desejada: \n 1 - Adição \n 2- Subtração \n 3 - Multiplicação \n 4 - Divisão")

def adicao():
	numero1 = input("Digite o primeiro número: ")
	numero2 = input("Digite o segundo numero: ")
	soma = numero1 + numero2
	print(f"O resultado da soma é {soma}")

def subtracao():
	numero1 = input("Digite o primeiro número: ")
	numero2 = input("Digite o segundo numero: ")
	subtracao = numero1 - numero2
	print(f"O resultado da soma é {subtracao}")

def multiplicacao():
	numero1 = input("Digite o primeiro número: ")
	numero2 = input("Digite o segundo numero: ")
	multiplicacao = numero1 * numero2
	print(f"O resultado da soma é {multiplicacao}")

def divisao():
	numero1 = input("Digite o primeiro número: ")
	numero2 = input("Digite o segundo numero: ")
	soma = numero1 + numero2
	print(f"O resultado da soma é {soma}")

if opcao == 1:
	adicao()
elif opcao == 2:
	subtracao()
elif opcao == 3:
	multiplicacao()
elif opcao == 4:
	divisao
else:
	print("Operação escolhida incorreta.")
