# Напишите функцию get_most_frequent_word, которая на вход принимает
# текст (только английские слова и пробелы), и возвращает
# самое часто встречающееся слово. Если таких слов несколько - верните любое.
def get_most_frequent_word(text: str) -> str:
    txt_dict = dict.fromkeys(text.split(), 0)
    for i in text.split():
        txt_dict[i] += 1
    return max(txt_dict, key=txt_dict.get)#Можно было отсортировать дикт по значению и вернуть первое зн.



print(get_most_frequent_word("Please help me to learn Python Python"))
print((get_most_frequent_word("if i don't learn Python i go to the ZAVOD")))
