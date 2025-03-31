#asks for user input
word = input('Enter Text: ')
#checks if all chars is in lowercase
is_lower = True
for char in word:
    if 'A' <= char <= 'Z':
        is_lower = False
        break
#prints the boolean result