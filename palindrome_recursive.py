"""Find palindromes (letter palingrams) in a dictionary file."""

import load_dictionary
file = input("Enter the name of your file (must be in the same directory):\n")
word_list = load_dictionary.load(file)
pali_list = []

def is_palindrome(word):
    if len(word) <= 1: #base case
        return True
    elif word[0] == word[-1]:
        new_word = word[1:-1]
        if is_palindrome(new_word):
            return True
    
for w in word_list:
    if is_palindrome(w):
        pali_list.append(w)

print(*pali_list, sep="\n")
print(f"Number of palindromes found: {len(pali_list)}")

'''    
for word in word_list:
    if word == "" or len(word) == 1:
        pali_list.append(word)
        continue

    while word[0] == word[-1]:
        new_word = word[1:-1]
        if word == "" or len(new_word) == 1:
            pali_list.append(new_word)
            break
'''