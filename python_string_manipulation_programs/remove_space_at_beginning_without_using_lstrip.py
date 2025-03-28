#ask for user input
word = input('Enter text: ')
#remove leading spaces without using lstrip
for i in range(len(word)):
    if word[i] != ' ':
        break
#print result
print('String without leading spaces:' , word[i])