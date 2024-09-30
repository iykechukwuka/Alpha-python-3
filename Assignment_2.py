#(1)...Check for Vowel or Consonant
#Write a Python program that checks if a given letter is a vowel or a consonant.
#-Vowels: 'a', 'e', 'i', 'o', 'u' (consider both uppercase and lowercase letters)
from Assignment_1 import total_char


def vowel_consonant(alphabet):

    vowels = 'a','e','i','o','u','A','E','I','O','U' #Considering both uppercase and lowercase letters.

    if len(alphabet) == 1 and alphabet.isalpha(): #Checking the command input is a singular alphabet or letter
        if alphabet in vowels:
            return f'{alphabet} is a Vowel.'
        else:
            return f'{alphabet} is not a vowel but a Consonant.'
    else:
        return 'Please check if your input is correct.'

alphabet = input("Enter a letter: ")
output = vowel_consonant(alphabet)
print(output)

print('------------------------------------------------------------------')

# (2)....Divisibility Check
#Write a Python program that checks if a number is divisible by 3 and 5.
def divisibility_check(number):

    x = number #Asigning number as a value of x

    if x % 3 == 0 and x % 5 == 0:
        return f'{x} is divisible by both 3 and 5' #- If divisible by both, print "Divisible by both"
    elif x % 3 == 0:
       return f'{x} is divisible by 3' #- If divisible by only 3, print "Divisible by 3"
    elif x % 5 == 0:
       return f'{x} is divisible by 5' #- If divisible by only 5, print "Divisible by 5"
    else:
        return f'{x} is Not divisible by 3 or 5' # Otherwise, print "Not divisible by 3 or 5"

x = int(input('Enter a Number: '))
output = divisibility_check(x)
print(output)

print('------------------------------------------------------------------')

#write a Python program to check the type of triangle (equilateral, isosceles, or scalene) based on the lengths of its sides.

def triangle_type(a, b, c):

     #check sides x,y,z forms a triangle.
    if a + b > c and a + c > b and b + c > a:
       #All sides equal (Equilatral traingle)
        if a == b and b == c:
          return 'Equilateral triangle'
       #Two sides are equal(Isosceles)                                                                                                                                                                                                              # Two sides are equal
        elif a == b or b == c or c == a:
            return 'Isosceles triangle'
       #All side are different(Scalene)
        else:
           return 'Scalene triangle'
    else:
        return 'The sides no not form a valid triangle'

a = float(input('Enter the length of side 1: '))
b = float(input('Enter the length of side 2: '))
c = float(input('Enter the length of side 3: '))

output = triangle_type(a, b, c)
print(output)


print('------------------------------------------------------------------')

first_line = float(input('the first line value: '))
second_line = float(input('the second line value: '))
third_line = float(input('the third line value: '))

if first_line==second_line==third_line:
    print('All sides equal Equilatral traingle')
elif first_line==second_line or second_line==third_line or first_line==third_line:
    print('Two sides are equal Isosceles')
else:
    print('All side are different Scalene')