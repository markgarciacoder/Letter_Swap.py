word = input("Enter a word: ")
letter = input("Enter a letter: ")

word_list = list(word)

for i in range(len(word_list)):
    if word_list[i] == letter:
        word_list[i] = '*'

print(word_list)