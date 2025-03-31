#asks for user input and desired lenght of string
text = input('Enter String: ')
lenght = int(input('Enter desired lenght: '))
#add zeros at the start without zfill()
if len(text) < lenght:
    text = '0' * (lenght -len(text)) + text
#prints the result with zeros