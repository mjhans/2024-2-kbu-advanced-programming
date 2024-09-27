word = input("Enter a word: ")
print(word)
# 문자열을 reverse 한다.
reversed_word = word[::-1]
print(reversed_word)

if word == reversed_word:
    print("palindrome")
else:
    print("not palindrome")