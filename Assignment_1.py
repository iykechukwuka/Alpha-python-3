#1. A. Create a string variable greeting with the value "Hello, World!" and perform the following operations:
from itertools import count
from operator import index
from shlex import quote

greeting = "Hello, World!"

#B. Print the string in all uppercase.
x = greeting.upper()
print(x)

#C. Print the string in all lowercase.
y = greeting.lower()
print(y)

#D. Replace "World" with your name.
z = "Hello, World!"
print(z.replace("World!", "Iyke!"))

seperator = "-----------------------------------------------------"
print(seperator)

#2. Given the string quote = "The only limit to our realization of tomorrow is our doubts of today.", perform the following:
quote = "The only limit to our realization of tomorrow is our doubts of today."

#A. Find the index of the word "doubts."
word = "doubts"
word_index = quote.index(word)
print(f"The index of the word 'doubts' is {word_index}")

print(quote.find("doubt"))

#B. Count how many times the letter "o" appears.
o_count = quote.lower().count("o")
print(f"The letter 'o' appeared {o_count} times")

#C. Check if the string starts with "The" and ends with "today."
if quote.startswith("The") and quote.endswith("today."):
    print("True")
else:
    print("False")

seperator = "-----------------------------------------------------"
print(seperator)

#3. Given the string text = "Data Science", write a program to:

text = "Data Science"

#A. Count how many times the letter "a" appears in the string.
a_count = text.lower().count("a")
print(f"The letter 'a' appeared {a_count}")

#B. Count the total number of characters in the string, excluding spaces.
total_char = len(text.replace(" ",""))
print(f"The total number of characters in the text string is {total_char}") #After removing the space " " between the words.
