print("Please input a word to be reversed: ", end="")
word = input()
for i in range(len(word) - 1, -1, -1):
    print(word[i], end="")