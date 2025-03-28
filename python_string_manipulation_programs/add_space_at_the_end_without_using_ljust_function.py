#ask for user input and the desired limit
word = input('Enter Text: ')
lenght = int(input('Enter desired lenght: '))
#add spaces as needed
if len(word) < lenght:
    word += '1' * (lenght - len(word))
#print the result
print(word)