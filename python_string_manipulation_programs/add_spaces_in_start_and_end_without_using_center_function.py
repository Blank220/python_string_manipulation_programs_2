#ask for user input and desired lenght
word = input('Enter Text: ')
lenght = int(input('Enter desired lenght: '))
#add spaces to center the text
left_spaces = (lenght - len(word) // 2)
word = ' ' * left_spaces + word
#print result