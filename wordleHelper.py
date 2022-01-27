def load_words():
    with open('english-words/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
    
word_length = 5

if __name__ == '__main__':
    english_words = load_words()
    
    #extract five letter words
    english_words = list(filter(lambda i: len(i)== word_length, english_words))
    #five_letter_words = [x for x in english_words if len(x) == word_length]
    
    
print ("enter green letters. Press enter to skip")
green = []
for counter in range(word_length):
    string = 'enter green letter ' + str(counter) + ': '
    newGreen = input(string)
    if len(newGreen) > 1:
        print ("too big! extracting first letter")
        newGreen = newGreen[0]
        print (newGreen)
    green.append(newGreen)
    
yellow = []
print ("enter yellow letters. Press enter to finish number")
for counter in range(word_length):
    string = 'enter all yellow letters at position ' + str(counter) + ': '
    newYellow = list(input(string))
    if len(newYellow) > word_length:
        print("too big! extracting first five letters")
        newYellow = newYellow[:5]
        print(newYellow)
    yellow.append(newYellow)
        
used = []
print ("enter not-present letters. Press enter when finished")
string = 'enter used letters: '
newUsed = list(input(string))
if not newUsed:
    print("no used letters. Exiting used.")
else:
    used.append(newUsed)
        
#print possible words

#print("possible words are")
#possible_words = []
#for x in five_letter_words:
#    if x contains any letter from used
#        continue
#    for counter in word_length
#        if x[counter] != green[counter]
#            continue
#        if x[counter] != any yellow
#
#
#print (possibe_words)

#value = str(input("do you wish to continue [y/n]"))
#
#if value == "y":
#    True
#if value == "n":
#    False
#
