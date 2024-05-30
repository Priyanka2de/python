# 1. Convert an integer to decimal

num1 = 123

print(type(num1))

print(type(float(num1)))

# 2. Convert a string of integer to decimal

num2 = "123"

print(type(num2))

print(type(float(num2)))

# 3. Count the number of Vowels in a word

word = "priyanka"

vowels = "aeiouAEIOU"

count = 0

for letters in word:
    if letters in vowels:
        count = count + 1

print(count)

# 4. Count the number of Consonants in a word

word = "priyanka"

vowels = "aeiouAEIOU"

count = 0

for letters in word:
    if letters not in vowels:
        count = count + 1

print(count)

# 5. Count the occurrence of character in a word

word = "priyanka"

occurrence_of_a = 0

for characters in word:
    if characters == "a":
        occurrence_of_a = occurrence_of_a + 1
print(occurrence_of_a)

#------------------------------------------------

word = "priyanka"

occurrence_of_each_character = {}

for character in word:
    if character not in occurrence_of_each_character:
        occurrence_of_each_character[character] = 1
    else:
        occurrence_of_each_character[character] += 1

print(occurrence_of_each_character)

#--------------------------------------------------

word = "priyanka is good girl"

occurrence_of_each_character = {}

for character in word:
    if character not in occurrence_of_each_character:
        occurrence_of_each_character[character] = 1
    else:
        occurrence_of_each_character[character] += 1

print(occurrence_of_each_character)

# 6. Count the occurrence of words in a sentence

sentence = "Priyanka is a good girl but she is good at nothing"
word = "good"

list_of_words = sentence.split(" ")
count_of_good = 0

for words in list_of_words:
    if words == word:
        count_of_good += 1
print(count_of_good)

#-----------------------------------------------------------------

sentence = "Priyanka is a good girl but she is good at nothing"

list_of_words = sentence.split(" ")
occurrence_of_each_word = {}

for words in list_of_words:
    if words not in occurrence_of_each_word:
        occurrence_of_each_word[words] = 1
    else:
        occurrence_of_each_word[words] += 1
print(occurrence_of_each_word)

# 7. Reverse a string

name = "Priyanka"

print(name[::-1])

#-------------------------------------------
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#
# Syntax
# range(start, stop, step)
#
# Parameter Values
#
# Parameter	Description
# start	    Optional. An integer number specifying at which position to start. Default is 0
# stop	    Required. An integer number specifying at which position to stop (not included).
# step	    Optional. An integer number specifying the incrementation. Default is 1

name = "Priyanka"
reversed_name = " "
for i in range(len(name)-1, -1, -1):
    reversed_name = reversed_name.join(name[i])

print(reversed_name)    # ???????????????????????

# 8. Check for Palindrome



# 9. Count the white space in a string

sentence = "Priyanka is a good girl but she is good at nothing"
count_of_whitespace = 0
for i in sentence:
    if i == " ":
        count_of_whitespace += 1

print(count_of_whitespace)

# 10. Count the occurrence of space,numbers,words,characters in a string

sentence = "Priyanka is a good girl but she is good at only 3 things"

count_of_whitespace = 0
for i in sentence:
    if i == " ":
        count_of_whitespace += 1

print(f"count of white space {count_of_whitespace}")

list_of_words = sentence.split(" ")
count_of_each_word = {}

for words in list_of_words:
    if words not in count_of_each_word:
        count_of_each_word[words] = 1
    else:
        count_of_each_word[words] += 1
print(f"count of each word {count_of_each_word}")


# 11. Fibonacci series

# 12. Maximum and minimum number from a list

num_list = [4, 6, 9, 3, 1, 8, 13, 11]
maximum = 0
for x in num_list:
    if x > maximum:
        maximum = x

print(maximum)

minimum = num_list[0]
for i in range(len(num_list)-1):
    if num_list[i] < minimum:
        minimum = num_list[i]

print(minimum)
