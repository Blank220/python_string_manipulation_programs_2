#asks for user input and another input for checking
word = input('Enter Text: ')
starts = input('Enter prefix to check: ')
#checks if text starts with the given input
starts_with = word[:len(starts)] == starts
#prints the result
print('Text starts with the prefix??: ', starts_with)