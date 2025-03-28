#ask for user input and a suffix to check 
word = input('Enter Text: ')
suffix = input('Enter suffix to be check: ')
#checks if the text ends with the suffix provided
result = word[-len(suffix):] == suffix
#print the result
print('The word ends with suffix?: ' , result)