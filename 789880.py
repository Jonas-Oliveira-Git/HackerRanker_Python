n = int(input())

dados = []
aux = 0
score_second = 0
second_place_times = 0
delta = 0

for i in range (n):
    name = input()
    score = float(input())
    dados.append((name,score))

for j in range(n):
    for k in range(j+1,n):
        if dados[k][1] < dados[j][1] or (dados[k][1] == dados[j][1] and dados[k][0] < dados[j][0]):
            aux = dados[k]  
            dados[k] = dados[j]  
            dados[j] = aux  

for  x in range (n):
    if dados[x][1] == dados[0][1]:
        delta = delta+1
        
score_second = dados[delta][1]


for l in range (n):
    if dados[l][1] == score_second:
        second_place_times = second_place_times + 1

dados_ordenados = tuple(sorted(dados))

for m in range(n):
    if dados[m][1] == score_second:
        print(dados[m][0])


