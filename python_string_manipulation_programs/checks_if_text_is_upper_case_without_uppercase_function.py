#asks for user input and a variable that contains boolean for checking
word = input('Enter Text: ')
upper_case = True
#checks if char is upper
for char in word:
    if 'a' <= char <= 'z':
        upper_case = False
        break
#print result