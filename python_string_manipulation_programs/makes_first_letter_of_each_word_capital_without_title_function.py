#ask for user input and a variable to hold result
words = input('Enter Text: ')
result = ''
#splits the word and capitalize the first letters
for word in words.split():
    result += word.capitalize() + ' '
#print result
