def area(a,b,c):
	if (a>0)*(b>0)*(c>0):
		p=(a+b+c)/2
		S=(p*(p-a)*(p-b)*(p-c))**(1/2)
		return S
	else:
		print('стороны треугольника заданы неправильно')

a=float(input("задайте сторону стреугольника а:"))
b=float(input("задайте сторону стреугольника b:"))
c=float(input("задайте сторону стреугольника c:"))

S=area(a,b,c)
print("площадь трейгольника равна: "+str(S))