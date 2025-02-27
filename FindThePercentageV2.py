n = int(input())

lista_nomes  = [0]*n
notas = []

for i in range(n):
    entrada = input().split()
    nome = entrada[0]
    lista_nomes[i] = nome
   
    notas = []

    for j in range(3):
        notas.append(float(entrada[j+1]))
        print('nome :',nome,' notas: ',notas)

nome_busca = input()
for i in range(n):
    if lista_nomes[i]==nome_busca:
        soma = sum(notas[i])
        media = soma/3
        print(f"{media:.2f}")
        break
