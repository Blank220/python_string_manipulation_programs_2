#asks for user input and lenght of spaces
word = input('Enter Text: ')
lenght = int(input('Enter desired lenght: '))
#add spaces at the start as needed
if len(word) < lenght:
    word = ' ' * (lenght - len(word)) + word
#prints the result with spaces in beginning
print('Text after right justification: ', word)