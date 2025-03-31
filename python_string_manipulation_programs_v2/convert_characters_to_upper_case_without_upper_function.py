#ask for user input and a variable for storing result
word = input('Enter Text: ')
result = ''
#converts the given text into upper case without upper function
for char in word:
    if 'a' <= char <= 'z':
        result += chr(ord(char) -32)
    else:
        result += char

#prints the result, text in upper casing