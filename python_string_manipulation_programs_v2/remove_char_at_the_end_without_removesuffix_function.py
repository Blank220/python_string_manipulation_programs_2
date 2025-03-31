#asks for user input and suffix to be remove
word = input('Enter Text: ')
suffix = input('Enter suffix to be remove: ')
#removes the suffix indicated
if word.endswith(suffix):
    word = word[:-len(suffix)]
#prints the result
print('The Text Without Suffix Indicated: ', word)