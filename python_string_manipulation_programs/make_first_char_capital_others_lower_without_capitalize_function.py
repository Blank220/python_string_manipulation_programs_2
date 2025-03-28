#ask for user input
word = input('Enter Text: ')
#capitalize the first letter and lowercase preceeding chars
if word:
    result = word[0].upper() + word[1:].lower()
else:
    result = word
#print the result
print('Capitalized text: ' , result)