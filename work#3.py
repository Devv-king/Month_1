glas = ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'о', 'у', 'ы', 'ё', 'ю', 'и', 'э']

while True:
    vowels = 0
    consonants = 0

    word = str(input("Input word: "))
    if word == "exit" or not word.isalpha():
        break
    word_length = len(word)
    for i in range(word_length):
        if word[i].lower() in glas:
            vowels += 1
        else:
            consonants += 1

    percent_vowels = vowels / word_length * 100
    percent_consonants = consonants / word_length * 100

    print("Слово: ", word)
    print("Количество букв: ", word_length)
    print("Согласных букв: ", consonants)
    print("Гласных букв: ", vowels)
    print("Гласные/Согласные:", round(percent_vowels, 2), "/", round(percent_consonants, 2))
