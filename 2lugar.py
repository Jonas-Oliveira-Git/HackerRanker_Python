n = int(input())

vetor = list(map(int,input().split()))
aux = 0


for i in range(n):
    for j in range(i+1,n):
         if vetor[i]<vetor[j]:
            aux = vetor[j]  
            vetor[j] = vetor[i]  
            vetor[i] = aux

MaiorValor=vetor[0]
Segundo = None

for k in range(1,n):
    if vetor[k]<MaiorValor:
        Segundo = vetor[k]
        break

if Segundo is not None:
    print(Segundo)








