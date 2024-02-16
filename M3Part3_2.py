

#удаляем пункутацию
def del_punct(s):
	s_without_punct='' 
	import string 
	for i in s:
		if not i in string.punctuation: 
			s_without_punct+=i
	return s_without_punct


#набираем список коротких слов
def word_list(s_without_punct):
	s_without_punct=s_without_punct.split()
	small_words=[]
	for i in s_without_punct:
		if len(i)<5:
			small_words.append(i)
	return small_words


#выписываем в строчку все уникальные короткие слова
def writer_words(small_words):
	small_words=set(small_words)
	finalstr=''
	for i in small_words:
		finalstr+=i+' '
	finalstr=finalstr.capitalize()
	print(finalstr)


#основная часть программы
s='''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошёл с ума, то ли я - того...
На столе записка от неё смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''

s_without_punct=del_punct(s)
small_words=word_list(s_without_punct)
writer_words(small_words)

