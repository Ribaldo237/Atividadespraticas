#Ativ1
#contador = 0
#while contador <= 10:
#  print(contador)
#  contador += 1

#Ativ2
#soma = 0
#numero = 0
#while numero <= 100:
#  soma += numero
#  numero += 1
#print(f"A soma dos numero de 0 a 100 é: {soma}")

#Ativ3
#numero = int(input("Dijite o umero que voce deseja saber a tabuada: "))
#contador = 1
#while contador <= 10:
#  resultado = numero * contador
#  print(f"{numero} x {contador} = {resultado}")
#  contador += 1

#Ativ4
#contador = 10
#while contador >= 1:
#  print(contador)
#  contador -= 1
#print("Feliz ano novo!")

#Ativ5
#numero_max = int(input("Dijite o numero maximo que deseje contar: "))
#contador = 1
#while contador <= (numero_max):
#  print(contador)
#  contador += 1
#print("O numero atingiu o numero maximo.")

#Ativ6
#soma = 0
#while True:
#  numero = int(input("Digite os numero positivos qeu você quer somar (digite um numero negativo para sair):"))
#  if numero < 0:
#    break
#  soma += numero
#print(f"A soma dos numeros positivos é {soma}")

#Ativ7
#numero = int(input("Dijite o numero para mostra os resultados da taubada multiplos por 3: "))
#contador = 1
#while contador <= 10:
#  resultado = numero * contador
#  if resultado % 3 == 0:
#    print(f"{numero} x {contador} = {resultado}")
#  contador += 1

#Ativ8
#soma_notas = 0
#Quantidade_notas = 0
#while True:
#  nota = float(input("Digite a nota que deseja somar (dijite -1 para cancelar e somar tudo): "))
#  if nota == -1:
#    break
#  soma_notas += nota
#  Quantidade_notas += 1
#if Quantidade_notas > 0:
#  media = soma_notas / Quantidade_notas
# print(f"A quantidade de notas insiridas foram: {Quantidade_notas}")
#  print(f"A media das notas foi {media:.2f}")
#else:
#  print("Nenhuma nota foi inserida.")

#Ativ9
# contador = 1
# while contador <= 10:
#     print(contador)
#     contador += 1
# print("Termino da contagem.")

#Ativ10
# numero = 1 
# soma = 0
# while soma < 50:
#     soma += numero
#     print(f"O numero atual é {numero}, soma total: {soma}")
#     numero += 1

#Ativ11
# while True:
#     numero = int(input("Digite um numero entre 1 e 10: "))
#     if 1 <= numero <=10:
#         print(f"O numero que você digitou é valido: {numero}")
#         break
#     else:
#         print(f"O numero que você digitou não é valido: {numero}")

#Ativ12
# senha = "RobocoDeParede"
# while True:
#     senha_digitada = input("Digite a senha: ")
#     if senha_digitada == senha:
#         print("Senha correta, bem-vindo pedreiro.")
#         break
#     else:
#         print("Senha incorreta, você não é pedreiro.")

#DesafPrat1
# soma = 0
# numero = 0
# while numero <= 100:
#     if numero % 2 == 0:
#         soma += numero
#     numero += 1
# print(f"A soma dos numeros pares de 1 a 100 é: {soma}")

#DesafPrat2
# numero = 1
# while numero <= 50:
#     if numero % 2 != 0:
#       print(numero)
# numero += 1

#DesafPrat3
# a ,b = 0, 1
# contador = 0
# while contador <= 20:
#     print(a)
#     a, b = b, a + b
#     contador += 1

#DesafPrat4
# numero = int(input("Digite o numero que deseja saber o fatorial: "))
# fatorial = 1
# while numero > 1:
#     fatorial *= numero
#     numero -= 1
# print(f"O fatorial do numero escolhido é {fatorial}.")

#DesafPrat5
# inicio = int(input("Digite o numero de ínicio do intervalo: "))
# fim = int(input("Digite o numero do final do intervalo: "))
# if inicio % 2 != 0:
#     inicio +=1
# while inicio <= fim:
#     print(inicio)
#     inicio += 2

#DesafPrat6
# numero = int(input("Digite o numero para fazer a contagem até zero exibindo os numero pares no processo: "))
# while numero >= 0:
#     if numero % 2 == 0:
#         print(numero)
# numero += 1   

#DesafPrat7
# numero = int(input("Digite um número: "))
# while numero >= 10:
#     soma = 0
#     while numero > 0:  
#         soma += numero % 10  
#         numero //= 10  
#     numero = soma  
# print("A soma dos dígitos até ser um único dígito é:", numero)

#DesafPrat8
# numero = int((input("Digite o numero que deseja:")))
# while numero != 1:
#     print(numero)
#     if numero % 2 == 0:
#         numero //= 2
#     else:
#         numero = 3 * numero + 1
# print(numero)

#DesafPrat9
# import random
# numero_secreto = random.randint(1, 100)
# tentativas = 0
# print("Um numero foi escolhido entre 1 e 100, advinhe qual!")
# while True:
#     palpite = int(input("Digite seu numero: "))
#     tentativas += 1
#     if palpite < numero_secreto:
#         print("O numero é maior, tente de novo.")
#     elif palpite > numero_secreto:
#         print("O numero é menor, tente de novo.")
#     else:
#         print(f"Parabens voce acertou o numero. Voce tentou {tentativas} vezes ate acertar")
#         break