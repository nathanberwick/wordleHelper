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
        if len(newYellow) > 1:
            print ("too big! extracting first letter")
            newYellow = newYellow[0]
            print (newYellow)
        yellow.append(newYellow)
        
print ("enter used letters. Press enter when finished")
used = []
usedCheck = True
while usedCheck:
    string = 'enter used letter: '
    newUsed = str(input(string))
    if not newUsed:
        print ("exiting used")
        usedCheck = False
    else:
        if len(newUsed) > 1:
            print ("too big! extracting first letter")
            newUsed = newUsed[0]
            print (newUsed)
        used.append(newUsed)
        
#print possible words

print("possible words are")
possible_words = []
for x in five_letter_words:
    #do stuff
    
print (possibe_words)

#value = str(input("do you wish to continue [y/n]"))
#
#if value == "y":
#    True
#if value == "n":
#    False
#
