#ask for user input and a variable that stores result
word = input('Enter Text: ')
result = ''
#checks every character in text and reverses the case
for char in word:
    if char.islower():
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
        result += char
#print result
print('Text in reverse casing: ' , result)