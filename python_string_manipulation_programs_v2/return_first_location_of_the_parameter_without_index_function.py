#ask for user input and character to find
word = input('Enter Text: ')
char = input('Enter character to find: ')
#Find the first appearance of char
for i in range(len(word)):
    if word[i] == char:
        print(f'{char} found at index {i}')
        break
else:
    print(f'{char} is not in text')