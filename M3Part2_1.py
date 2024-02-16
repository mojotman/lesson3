l=[1,4,1,6,"hello","a",5,"hello","hello"]
uniq=[]
same=[]
for i in range(len(l)):
	if l[i] in uniq:
		same.append(l[i])
	else:
		uniq.append(l[i]) 
print("список повторяющихся элементов: "+ str(set(same)))
