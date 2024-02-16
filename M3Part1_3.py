n=int(input("введите целое число: "))
n=abs(n)
sum1=0
dellit=10
check=0
while check != n:
	sum1+=(n%dellit-check)*10/dellit
	check=n%dellit
	dellit*=10
print("сумма цифр числа равна: "+str(sum1))