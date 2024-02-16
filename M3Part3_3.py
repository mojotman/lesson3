
#Делит число на состовляющие цифры
def splitNumber(n):
	numbers1=[]
	dellit=10
	check=0
	while check != n:
		numbers1.append(int((n%dellit-check)*10/dellit))
		check=n%dellit
		dellit*=10
	numbers2=[] #перевернем для удоства
	for i in range((len(numbers1)-1),-1,-1):
		numbers2.append(numbers1[i])
	return(tuple(numbers2))

#дробит матрицу
def splitMatrix(N):
	split_N=[]
	for i in N:
		split_N.append(splitNumber(i))
	return(split_N)




N=[594,93]
N=splitMatrix(N)
compare_factor=[]
for i in range(len(N)):
	compare_factor.append(N[i][0])
max(compare_factor)
print(max(compare_factor))
