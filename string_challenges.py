def get_last_letter(word):
    return word[-1]


# Вывести последнюю букву в слове
word = "Архангельск"
print(get_last_letter(word))


def get_count_letter(word, letter="а"):
    return word.count(letter)


# Вывести количество букв "а" в слове
word = "Архангельск"
print(get_count_letter(word))


def get_count_vowel(word):
    count_vowel = 0
    vowels = ["а", "е", "ё", "ы", "я", "у", "и", "о", "э", "ю"]
    for vowel in vowels:
        count_vowel += get_count_letter(word, vowel)
    return count_vowel


# Вывести количество гласных букв в слове
word = "Архангельск"
print(get_count_vowel(word.lower()))


def get_words_sentence(sentence):
    return sentence.split()


# Вывести количество слов в предложении
sentence = "Мы приехали в гости"
print(len(get_words_sentence(sentence)))


def get_first_letters(sentence):
    text = ""
    for word in get_words_sentence(sentence):
        text += word[0] + "\n"
    return text


# Вывести первую букву каждого слова на отдельной строке
sentence = "Мы приехали в гости"
print(get_first_letters(sentence))


def get_middle_len_word(sentence):
    middle_len = 0
    count_len = 0
    list_words = get_words_sentence(sentence)
    for word in list_words:
        count_len += len(word)
    middle_len = count_len / len(list_words)
    return str(middle_len)


# Вывести усреднённую длину слова в предложении
sentence = "Мы приехали в гости"
print(get_middle_len_word(sentence))
