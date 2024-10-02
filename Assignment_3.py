from audioop import reverse
from collections import Counter
#Light Assignments :
#  1.Fibonacci Sequence:
# Write a program that generates the Fibonacci sequence up to the nth term
# (where n is a positive integer input by the user) using a loop.

def fibonacci(n):
    n = abs(n) # converting 'n' to a positive number.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0 #....where (a) is the first number on the fibonacci sequence.
        b = 1 #....where (b) is the second number on the fibonacci sequence.
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return c #....Returning the sum of the previous 2 numbers in the sequence.
for i in range(0, 9): #...using a for loop to get the ninth term of the fibonacci index sequence.
    print('fibonacci(',i,')=', fibonacci(i))

print('-'*80)
#  2. Prime Numbers:
# Create a function that prints all prime numbers between 1 and 100 using a loop.
# A prime number is a number that is only divisible by 1 and itself.

"""a = int(input('Start of number series: '))
z = int(input('End of number series: '))

for number in range(a, z+1): #....Adding plus 1 to z to get the actual number.
    if number > 1:

        for i in range(2, number): #....performing a check to see if its prime number.
            if number % i==0:
                break
        else:
            print(number)"""

print('-'*80)
#  3.Character Count:
# Create a program that counts the occurrences of each character in a given string using a loop
# and prints the results in a dictionary format.

def character_count(text):

# Method 1;

  char_dictionary = {}
  for char in text:
    if char in char_dictionary:
        char_dictionary[char]+= 1
    else:
        char_dictionary[char] = 1

  return char_dictionary

text = "Create a program that counts the occurrences of each character in a given string using a loop"
outcome = character_count(text)
print(outcome)

print('-'*80)
# Method 2: Using counter method;

print(Counter(text))

print('-'*80)
#   4. Reverse a String:
# Using a loop, write a program that takes a user-input string and
# returns the string reversed (without using any built-in methods).

def reverse_string(input_string):
    reversed_string = ""

    # Looping through the string;
    for char in input_string:
        reversed_string = char + reversed_string

    return reversed_string


# Example usage

input_string = input("Enter a string: ")
reversed_str = reverse_string(input_string)
print("Reversed string:", reversed_str)

#METHOD 2: using the slicer method;

string = 'Happy Independent Nigeria!'
new_string = string[::-1]
print(new_string)

#   5. Count Vowels and Consonants:
# Create a program that takes a string as input and counts the number of vowels and consonants using a loop.

def vowel_consonant_count(sentence):

 vowels_count = 0
 vowels = 'aeiou'  # ....Set of vowels list.
 vowels = vowels.lower()
 consonants_count = 0

 for i in sentence:
    if i.isalpha(): #...To confirm i (Character) is an alphabet.
      if i in vowels:
        vowels_count +=1
      else:
        consonants_count +=1

 return vowels_count, consonants_count #...returning the outcomes

sentence = input('Enter a string: ')
vowels, consonants = vowel_consonant_count(sentence)
print(f"Vowels: {vowels}, Consonants: {consonants}")