from random import randint
n=int(input("введите размер стороны квадратной матрицы: "))
m=[[randint(0,100) for i in range(n)] for j in range(n)]
printM=str(m)
printM=printM.replace('],',']\n')
print(printM)

max1=[]
for i in range(n):
	max1.append(sorted(m[i])[-1])
max1=sorted(max1)[-1]
print("маскимальное число равно: "+str(max1))