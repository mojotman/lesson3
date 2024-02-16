
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



def login_funcion(login,password):
	import json
	with open('данные_1задание.json','r',encoding='utf-8') as f:
		data=json.load(f)
		if login not in data.keys():
			print("неправильно введен логин")
			return
		else:
			if password==data[login]:
				print ('успешный вход в систему')
				print("секретная информация = 42")
			else:
				print("неправильно введен пароль")



while True:
	enter=input('вы хотите зарегистирроаться или войти в аккаунт? (рег/вход):')
	if enter=='рег':
		login=input("придумайте свой логин: ")
		password=input("придумайте  свой пароль: ")
		register (login,password)
	elif enter=='вход':
		login=input("введите свой логин: ")
		password=input("введите  свой пароль: ")
		login_funcion(login,password)
	else:
		print('программа вас не поняла. пишите "рег" или "вход"')
	exit=input('выйте из програмы?')
	if exit=='да':
		break
