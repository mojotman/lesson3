d={
'name1': 'id1',
'name2': 'id2',
'name3': 'id3',
}
keys1=d.keys()
value1=[]
for i in keys1:
	value1.append(d.get(i,'none'))
keys1=list(keys1)

newd={}
for i in range(len(value1)):
	newd[value1[i]]=keys1[i]
print(newd)
