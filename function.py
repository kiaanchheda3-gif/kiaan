# def square(n):
#     return n * n

# print (square(5))
# print (square(12))
# print (square(0))

# print ()

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#     if is_even(n):
#         print("The number is even.")
#     else:
#         print("The number is odd.")

# for i in range(1, 11):
#     if is_even(i):
#         print(f"{i} is even.")
#     else:
#         print(f"{i} is odd.")

#  print ()

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
word = input("Enter a word: ")
vowel_count = count_vowels(word)
print(f"The word '{word}' contains {vowel_count} vowels.")