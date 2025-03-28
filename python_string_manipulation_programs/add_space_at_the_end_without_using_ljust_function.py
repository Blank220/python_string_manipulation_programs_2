#ask for user input and the desired limit
word = input('Enter Text: ')
lenght = int(input('Enter desired lenght: '))
#add spaces as needed
if len(word) < lenght:
    word += ' ' * (lenght - len(word))
#print the result
print('Text after adding spaces: ' , word)