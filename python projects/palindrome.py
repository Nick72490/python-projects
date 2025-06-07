import string

word = input("input a word:")

checker = word.lower().replace(" ", "")

for char in string.punctuation:
    checker = checker.replace(char, "")

reversed = checker[::-1]

print(checker)

if checker == reversed:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
