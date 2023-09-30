# Напишите функцию get_longest_word, которая на вход принимает текст
# (только английские слова и пробелы), и возвращает самое длинное слово
# из этого текста.
# Для разбиения строки на слова используйте функцию split.

def get_longest_word(text: str) -> str:
    return max(text.split(), key=len)


print(get_longest_word("Скажи ка дядя ведь не даром я пайтон выучил с уроком Буевича Димы"))
# я пытался складно))
print(get_longest_word("People who lives in glass houses should not throw stones"))
