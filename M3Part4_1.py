
def register (login,password):
	data={}
	data[login]=password
	import json
	with open('данные_1задание.json','w',encoding='utf-8') as f:
		json.dump(data,f)


login=input("придумайте свой логин: ")
password=input("придумайте  свой пароль: ")
register (login,password)