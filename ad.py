def first_word(word):
    for i in word:
        if not i.isalpha() and i != ' ':
            word = word.replace(i,'')
    return word.split()[0].strip()










