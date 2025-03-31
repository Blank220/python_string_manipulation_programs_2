#ask for user input
word = input('Enter Text: ')
#remove spaces at the end of the input
for i in range(len(word) -1, -1, -1):
    if word [i] != ' ':
        break
#prints the result without spaces