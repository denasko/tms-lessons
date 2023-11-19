import re


# text = 'Echte liebe nur der Borusse'
# gen = (i for i in re.findall(r'[а-яА-Я]|[a-zA-Z]+', text))

def generate_words(row: str) -> any:
    for word in re.findall(r'[а-яА-Яa-zA-Z]+', row):
        yield word


assert ['See', 'the', 'city', 'burn', 'on', 'the', 'other', 'side'] == [i for i in generate_words(
    'See the city burn on the other side')]
assert {'I': 'I', 'love': 'love', 'zavod': 'zavod'} == {i: i for i in generate_words('I love zavod')}
