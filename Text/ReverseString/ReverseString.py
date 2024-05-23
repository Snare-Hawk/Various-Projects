# Reverse a String - Enter a string and the program will reverse it and print it out.

print("Please input a word to be reversed: ", end="")
word = input()
for i in range(len(word) - 1, -1, -1):
    print(word[i], end="")