n = int(input())

lista = [0]*n
# print('lista aqui',lista)
for i in range(n):
    lista[i] = i +1

resultado =""

for elemento in lista:
    resultado+=str(elemento)

print(resultado)
