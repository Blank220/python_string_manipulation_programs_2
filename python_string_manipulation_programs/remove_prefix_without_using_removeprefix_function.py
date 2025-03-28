#ask user to input text and the prefix to be remove
word = input('Enter Text: ')
prefix = input('Enter the prefix to be remove: ')
#remove the prefix
if word.startswith(prefix):
    word = word[len(prefix):]
#print result
print('Removed the prefix:' , word)