def Count_letter_in_word(letter, text):
    counter = 0
    for i in range(len(text)):
        if text[i] == letter:
            counter += 1
    return counter

print(Count_letter_in_word(
    'e', 'You never get a second chance to make a first impression'
))
