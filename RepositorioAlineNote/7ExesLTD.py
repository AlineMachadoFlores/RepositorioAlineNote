
#1 - crie uma lista vazia
#2 - utilize print para exibir lista de compras a cada adição ou remoção de itens da lista
#3 - utilize append para adicionar itens a lista
#4 - adicione remove para remover itens da lista

#Respostas:
#1
listafarmacia = []

#2
print(listafarmacia)

#3
listafarmacia.append("shampoo")
listafarmacia.append("condicionar")
print(listafarmacia)

#4
listafarmacia.remove("shampoo")
listafarmacia.remove("condicionar")
print(listafarmacia)

#Remova um número se ele existir



#Tarefa: Leia quatro inteiros e crie uma lista. Leia um valor alvo e remova se ele estiver na lista. Mostre o tamanho antes e depois.
 #Use: int(), input(), in, remove(), len(), print()
 #Tipos: int, list.
 #Conceitos: teste de pertencimento, tratamento simples de remoção, função len().
num1 = int(input("Digite um numero inteiro:"))
num2 = int(input("Digite outro numero inteiro:"))
num3 = int(input("Digite mais um numero inteiro:"))
num4 = int(input("Digite maais um numero inteiro:"))

lista = [num1, num2, num3, num4]

print("Numeros digitados:", lista) 
print("O tamanho da lista antes é:", len(lista))


remover = int(input("Digite um numero para remover:"))
if remover in lista:
    lista.remove(remover)
    print("Número removido.")
else:
    print("Número não encontrado na lista.")
print("O tamanho da lista depois é:", len(lista))



#Atualizar elemento com uma operação

#Tarefa: Crie uma lista com três inteiros. Atualize o último elemento para a soma dos dois primeiros. Exiba a lista.
#Use: int(), input(), indexação lista[i], print()
#Tipos: int, list.
#Conceitos: operadores aritméticos (+), acesso/atribuição por índice.


num1 = int(input("Digite um numero inteiro:"))
num2 = int(input("Digite outro numero inteiro:"))
num3 = int(input("Digite mais um numero inteiro:"))
numeros = [num1, num2, num3]
print("Lista original:", numeros)
numeros[2] = num1+num2
print("Lista atualizada:", numeros)





#Notas: subtituir a menor nota, ordenar e recalcular a média
#Tarefa: Leia três notas (float) em uma lista. Calcule a média. Substitua a menor nota por uma nova informada. Ordene a lista e mostre a nova média.
#Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(), print()
#Tipos: float, list.
#Conceitos: mutabilidade, ordenação in-place, média aritmética.

notas = [float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: ")), float(input("Digite a terceira nota: "))]
notas2 = [notas[0], notas[1], notas[2]]
print("Notas digitadas: ", notas)
media = sum(notas) / len(notas)
print("A média das notas é: ", media)

menor_nota = min(notas)


nova_nota = float(input("Digite a nova nota: "))
indice_menor = notas.index(menor_nota)
notas[indice_menor] = nova_nota

notas.sort()
print("A lista ordenada é: ", notas)

media_nova = sum(notas) / len(notas)
print("A nova média é: ", media_nova)