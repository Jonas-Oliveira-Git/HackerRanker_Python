n = int(input())

A = list(map(int,input().split()))

top1 = 0
top2 = 0
top3 = 0

aux = 0

for i in range(n):
    if A[i] > top1 :
        top1 = A[i]
        A[i] = aux
        aux = 0

for j in range (0,n):
    if A[j] < top1 and A[j]>top2:
        top2 = A[j]
        A[j] = aux
        aux = 0
        print('top2 : ',top2)

print('primeiro lugar :',top1)
# print(top2)
        

