import re


class WordIterable:
    def __init__(self, row: str):
        self.row = re.findall(r"[а-яА-Я]+", row)
        self.count = -1

    def __iter__(self) -> any:
        return self

    def __next__(self) -> str:
        self.count += 1
        if len(self.row) == self.count:
            raise StopIteration()
        return self.row[self.count]


text = "мама. мыла? Раму!"
for i in WordIterable(text):
    print(i)

assert ["весь", "мир", "театр"] == [i for i in WordIterable("весь мир театр")]
assert ["и", "люди", "в", "нем", "актеры"] == [i for i in WordIterable("и люди в нем - актеры")]
assert ["у", "них", "свои", "есть", "выходы", ] == [i for i in WordIterable("у них свои есть выходы ,")]
assert ["уходы", "и", "каждый", "не", "одну", "играет", "роль"] == [i for i in
                                                                    WordIterable("уходы и каждый не одну играет роль.")]
