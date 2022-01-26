def load_words():
    with open('english-words/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

if __name__ == '__main__':
    english_words = load_words()
    
    #extract five letter words
    print(len(english_words))
    five_letter_words = []
    for x in english_words:
        if(len(x) == 5):
            five_letter_words.append(x)
    print(five_letter_words)

