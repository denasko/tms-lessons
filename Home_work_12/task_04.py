class WordIterable:
    def __init__(self, row: str):
        self.row = row.split()
        self.count = -1

    def __iter__(self) -> any:
        return self

    def __next__(self) -> str:
        self.count += 1
        if len(self.row) == self.count:
            raise StopIteration()
        return self.row[self.count]


text = ('Я увидел тебя у станка '
        'нежный взор твой меня озадачил '
        'ты стояла в руках теребя '
        'рукоятку продольной подачи '
        'я сказал тебе '
        'ваши черты несомненно полны благородства '  # Стихотворение про заводик :з
        'мне в ответ улыбаешься ты '
        'без отрыва от производства '
        'и не будет ни ветра ни туч '
        'только ты и я в этом мире '
        'хочешь я подарю тебе ключ ? '
        'двадцать два на двадцать четыре')

for word in WordIterable(text):
    print(word)


