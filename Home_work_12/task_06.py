def generate_words(row: str) -> any:
    for word in row.split():
        yield word


for i in generate_words('мама  мыла раму'):
    print(i)

assert ['нет', 'повести', 'печальнее', 'на', 'свете'] == [i for i in generate_words('нет повести печальнее на свете')]
assert ['0', '1', '4', '9', '16', '25'] == [i for i in generate_words('0 1 4 9 16 25')]
assert ['чем', 'повесть', 'о', 'регулярках'] == [i for i in generate_words('чем повесть о регулярках')]

assert not ['мама', '!', 'мыла44', 'раму', '?'] == [i for i in generate_words('мама!  мыла44 раму ?')]
assert not ['London', ',', 'is', 'the', 'capital', 'of', "'GB'."] == [i for i in
                                                                      generate_words("London, is the capital of 'GB'.")]
