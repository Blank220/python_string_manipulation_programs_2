#ask for user input and character to locate
word = input('Enter Text: ')
char = input('Character to find: ')
#finds the character's index starting from last
for i in range(len(word) -1, -1, -1):
    if word[i] == char:
        print(f'{char} found at index {i}')
        break
else:
    print(f'{char} is not in text')