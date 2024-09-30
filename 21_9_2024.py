#ageInput = input("I was born in: ")
from TeamAlphaClass import number


"""def check_vowel_consonant(letter):
    vowels = 'aeiouAEIOU'  # List of vowels (both lowercase and uppercase)

    if len(letter) == 1 and letter.isalpha():  # Check if input is a single letter
        if letter in vowels:
            return f"{letter} is a vowel."
        else:
            return f"{letter} is a consonant."
    else:
        return "Please enter a single letter."


# Example usage
letter = input("Enter a letter: ")
result = check_vowel_consonant(letter)
print(result)"""


#.....USING A WHILE LOOP:

""""number = 1
while(number < 10):
    print(f'I love Jesus ' + str(number))
    number+=1"""
#.....GETTING A NUMBER RANGE(25 - 50);
"""number = 25
while (number <= 50):
    print(number)
    number += 1"""

print('-------------------------------------------------------')

#.....GETTING EVEN NUMBERS DIVISIBLE BY 2;
"""number = 25
while (number <= 50):
    if number % 2 == 0:
        print(number)
    number +=1"""

print('-------------------------------------------------------')

#.....BREAK USING WHILE LOOP;
number = 25
while (number <= 50):
    number += 1

    if number % 2 == 0:
        if number == 40:
          break
        print(number)

#.....EXAMPLE 2;
number = 1
while (number < 10):
    print(number)

    if number == 5:
      break
    number += 1


print('-------------------------------------------------------')

#.....CONTINUE USING WHILE LOOP;
"""number = 25
while (number <= 50):
    number += 1
    if number % 2 == 0:
        if number == 40:
          continue
        print(number)"""

print('-------------------------------------------------------')

#COMBINE BOTH BREAK AND CONTINUE USING WHILE LOOP;
number = 1
while (number <= 100):
    number +=1

    if number %10 ==0:
        if number == 40:
            continue
        if number == 80:
            break
        print(number)
