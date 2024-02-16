
def register (login,password):
	import json


	with open('данные_1задание.json','r',encoding='utf-8') as f:
		data=json.load(f)
		if login in data.keys():
			print("такой пользователь уже есть")
			return
		else:
			data[login]=password
	with open('данные_1задание.json','w',encoding='utf-8') as f:
		json.dump(data,f)
		print('успешная регистрация')




login=input("придумайте свой логин: ")
password=input("придумайте  свой пароль: ")
register (login,password)