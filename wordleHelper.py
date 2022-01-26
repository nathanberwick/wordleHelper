def load_words():
    with open('english-words/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
    
word_length = 5

if __name__ == '__main__':
    english_words = load_words()
    
    #extract five letter words
    five_letter_words = []
    for x in english_words:
        if(len(x) == word_length):
            five_letter_words.append(x)
    #print(five_letter_words)
    
print ("enter green letters. Press enter to skip")
green = []
for counter in range(word_length):
    string = 'enter green letter ' + str(counter) + ': '
    newGreen = (input(string))
    if len(newGreen) > 1:
        print ("too big! extracting first letter")
        newGreen = newGreen[0]
        print (newGreen)
    green.append(newGreen)
    
print ("enter yellow letters. Press enter when finished")
yellow = []
yellowCheck = True
while yellowCheck:
    string = 'enter yellow letter: '
    newYellow = str(input(string))
    if not newYellow:
        print ("exiting yellows")
        yellowCheck = False
    else:
        yellow.append(input(string))
        
        

#for counter in range(word_length):
#    print(counter)

