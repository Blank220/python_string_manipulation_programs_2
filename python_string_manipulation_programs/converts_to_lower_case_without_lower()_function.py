#ask for user input and created a variable that stores the result
word = input('Enter Text: ')
result = ''
#convert each letter in lowercase
for char in word:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char
#print result