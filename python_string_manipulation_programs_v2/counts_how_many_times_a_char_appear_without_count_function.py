#ask for user input and a char to count
word = input('Enter Text: ')
char = input('Enter a character to count:')
#count how many times the char appeared in the string
count = 0
for c in word:
    if c == char:
        count += 1
#prints the number of times it appeared