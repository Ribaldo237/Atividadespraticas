#Ativ1
#print("Descubra qual idade é maior.")
#idade1 = int(input("Digite a primeira idade: "))
#idade2 = int(input("Digite a segunda idade: "))
#if idade1 > idade2:
#   print("A primeira idade é maior que a segunda.")
#elif idade2 > idade1:
#   print("A segunda idade é maior que a primeira.")
#else:
#   print("As duas idades são iguais.")

#Ativ2
#palavra1 = input("Digite a primeira palavra: ")
#palavra2 = input("Digite a segunda palavra: ")
#if palavra1.lower() == palavra2.lower():
#    print("As palavras são iguais.")
#else: 
#    print("As palavras são diferestes.")

#Ativ3
#idade = int(input("Digite a sua idade: "))
#habilitacao = input("Você possui habilitção? Responda apenas com (sim/nao): ").strip().lower()
#if idade >= 18 and habilitacao == "sim":
#    print("Você é maior de idade e possui habilitação.")
#elif idade >= 18 and habilitacao == "nao":
#    print("Você é maoir de idade, e você já pode tirar a habilitação.")
#elif idade < 18 and habilitacao == "sim":
#    print("Você possui habilitação, porém não deveria pois ainda é menor de idade.")   
#elif idade < 18 and habilitacao == "nao":
#    print("Você ainda é menor de idade, por isso ainda não tem habilitação.")     
#else:
#    print("Por favor, responda as perguntas corretamente.")    

#Ativ4
#print("Verifique suas notas.")
#nota1 = float(input("Digite sua primeira nota: "))
#nota2 = float(input("Digite sua segunda nota: "))
#if nota1 >= 6 and nota2 >= 6:
#    print("As duas notas são maiores ou iguas a seis.")
#elif nota1 >= 6 and nota2 < 6:
#    print("Apenas a primeira nota é maior ou igual a seis.")
#elif nota1 < 6 and nota2 >= 6:
#    print("Apenas a segunda nota é maior ou igual a seis.")
#else:
#    print("Ambas as notas são menores que seis.")    

#Ativ5
#preco = float(input("Digite o preço do produto: "))
#preco -= preco * 0.05
#print(f"O preço do produto com 5% de desconto é igual á: {preco:.2f}")

#Ativ6
#print("Descubra o dobro do seu valor digitado.")
#valor = int(input("Digite o valor que você quer o dobro: "))
#valor *= 2
#print(f"O dobro do numero que você digitou é: {valor}")

#Ativ7
#frase = str(input("Digite sua frase: "))
#caractere = str(input("Digite seu caractere: "))
#if caractere in frase:
#    print("O caractere esta na frase.")
#else:
#    print("O caractere não esta na frase.")

#Ativ8
#frase = input("Digite sua frase: ")
#palavra = input("Digite sua palavra: ")
#if palavra in frase:#
#    print("A palavra está na frase.")
#else:
#    print("A palavra não está na frase.")

#Ativ9
#numero = int(input("Digite seu numero para saber se é par ou impar: "))
#if numero % 2 == 0:
#    print("O numero é par.")
#else:#
#    print("O numero é impar.")

#Ativ10
#nota = float(input("Digite a nota do aluno: "))
#if nota >= 6:
#    print("O aluno passou!")
#else:
#    print("O aluno não passou.")

#Ativ11
#numero = int(input("Digite um numero para saber se é positivo ou negativo e par ou impar: "))
#if numero > 0 and numero % 2 == 0:
#    print("O numero é positivo e par.")
#elif numero > 0 and numero % 2 != 0:
#    print("O numero é positivo e impar.")
#elif numero    < 0 and numero % 2 == 0:#
#    print("O numero é negativo e par.")
#elif numero < 0 and numero % 2 != 0:#
#    print("O numero é negativo e impar.")
#else:#
#    print("O numero é igual a zero.")

#Ativ12
#print("Calcule seu Indice de massa corporal.")
#peso = float(input("Digite seu peso: "))
#altura = float(input("Digite sua altura: "))
#imc = peso / (altura * altura)
#if imc < 18.5:
#    print("Você está abaixo do peso.")
#elif imc >= 18.5 and imc < 25:
#    print("Você está no peso ideal.")
#elif imc >= 25 and imc < 30:
#    print("Você está com sobrepeso.")
#elif imc >= 30 and imc < 35:
#    print("Você está obeso.")
#else:
#    print("Você está com obesidade mórbida.")

#Ativ13
#print("Faça login.")
#usuario = input("Digite o nome do usuário: ")
#senha = input("Digite sua senha: ")
#if usuario == "admin" and senha == "1234":
#    print("Login realizado com sucesso!")
#else:
#    print("Usuário ou senha incorretos.")    

#Ativ14
#print("Verifique os status de desconto na compra de 10 ou mias unidades.")
#produto_preco = float(input("Digite o preço do produto: "))
#produto_quantidade = int(input("Digite a quantidade do produto: "))
#total = produto_preco * produto_quantidade
#if produto_quantidade >= 10:
#    total -= total * 0.1
#    print(f"O valor com desconto é de: {total:.2f}")
#else:
#    print(f"O valor sem desconto é de: {total:.2f}")    
