def count_words(book_text):
    word_list = book_text.split()
    wordcount = len(word_list)
    return(wordcount)

def count_letters(book_text):
    lowercase_letters = book_text.lower()
    letters = list(lowercase_letters)
    lettercount = {}
    for letter in letters:
        if letter in lettercount:
            lettercount[letter] += 1
        else:
            lettercount[letter] = 1
    return(lettercount)

def split_dict(alpha_count):
    lettercount_d = []
    for key, value in alpha_count.items():
        x = {}
        x["char"] = key
        x["num"] = value
        lettercount_d.append(x)
    return lettercount_d

def sort_letters(lettercount_d):
    return lettercount_d["num"]
    

def is_an_alpha(lettercount_us):
    alpha_count = {}
    for key, value in lettercount_us.items():
        if key.isalpha():
            alpha_count[key] = value
    return alpha_count