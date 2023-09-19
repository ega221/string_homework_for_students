"""
Вам дан список предложений.
предложения содержит только слова, которые разделены единичными пробелами.
Необзодимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> int:
    max_number_of_words = 0
    for sentence in sentences:
        number_of_words = len(sentence.split())

        if number_of_words > max_number_of_words:
            max_number_of_words = number_of_words

    return number_of_words
