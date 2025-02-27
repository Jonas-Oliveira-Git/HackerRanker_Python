n = int(input())

nomes = [0] * n
notas = []

for i in range(n):
    entrada = input().split()  # Divide a entrada em partes
    nome = entrada[0]         # O primeiro valor é o nome
    nomes[i] = nome
    
    aluno_notas = []  # Lista de notas do aluno

    # Itera sobre as 3 notas do aluno
    for j in range(3):
        aluno_notas.append(float(entrada[j + 1]))  # Adiciona cada nota à lista

    notas.append(aluno_notas)  # Adiciona a lista de notas do aluno à lista geral

query_name = input()

# Encontrar o aluno e calcular a média
for i in range(n):
    if nomes[i] == query_name:
        soma = sum(notas[i])  # Soma as notas do aluno
        media = soma / 3  # Calcula a média corretamente
        print(f"{media:.2f}")
        break
else:
    print("Aluno não encontrado")
