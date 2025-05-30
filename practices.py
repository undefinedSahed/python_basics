import utils.session
import random
import math


# username generator

def generate_username():
    full_name = input("Enter your full name: ")
    words = full_name.lower().split()
    
    words.append(str(random.randrange(1, 99)))
    
    result = "_".join(words)
    return "_".join(words)


print(generate_username())



# # Palindrome Checker

def is_palindrome():
    
    word = input("Enter the word: ")
    clean_word = word.lower().replace(" ", "")
    reversed_clean_word = clean_word[::-1]
     
    if clean_word == reversed_clean_word:
        return f"The word \'{word}\' is a palindrome"
    else:
        return f"The word \'{word}\' is not a palindrome"

print(is_palindrome())


# Custom Censor

def check_bad_language():
    bad_words = { "idiot", "stupid", "dumb", "fool", "loser", "moron", "shut up", "suck", "crap", "jerk" }
    given_text = input("Enter message: ")
    
    separated_text = given_text.lower().split()
    
    result_text = []
    
    for word in separated_text:
        if word in bad_words:
            replaced_word = word.replace(word, "***")
            result_text.append(replaced_word)
        else:
            result_text.append(word)
            
    return " ".join(result_text) 
        
print(check_bad_language())        



# Word Reverser

def reverse_word():
    given_text = input("Enter the text to reverse: ")
    separated_text = given_text.split()
    
    result_text = []
    for word in separated_text:
        reversed_word = word[::-1]
        result_text.append(reversed_word)
    
    return " ".join(result_text)

print(reverse_word())


# Email masker

def mask_email():
    given_email = input("Enter your email: ")
    
    if "@" not in given_email:
        return "Invalid email"
    
    username, domain = given_email.split("@", 1)
    
    if len(username) < 1 :
        return "Invalid email"
    
    
    masked_username = username[0] + "*" * (len(username) - 2) + username[-1]
    
    return f"{masked_username}@{domain}"


print(mask_email())
    
    
    
# Simple calculator

def calculate_operation():
    try :
        valid_operations = { "+", "-", "*", "/" }
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        
        if operation not in valid_operations: 
            return "Invalid operation"
        
        num2 = float(input("Enter second number: "))
        
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 == 0:
                return "Error: Division by Zero"
            else: 
                return num1 / num2
        
    except ValueError:
        return "Invalid number"
    
print(calculate_operation())


# Odd/Even Detector

def check_even_odd():
    try: 
        given_number = int(input("Enter a number "))
        
        if given_number % 2 == 0:
            return f"You entered {given_number} which is an even number"
        else :
            return f"You entered {given_number} which is an odd number"
    except ValueError:
        return "Invalid number"
    
print(check_even_odd())


# Area Calculator

def calculate_area():
    print("Choose  a shape to calculate area")
    print("1. Circle")
    print("2. Square")
    print("3. Triangle")
    print("4. Rectangle")
    
    choice = input("Enter your choice (1/2/3/4) : ")
    
    try:
        if choice == "1":
            radius = float(input("Enter the radius of the circle: "))
            area = math.pi * (radius ** 2)
            return area
        elif choice == "2":
            width = float(input("Enter the width of length: "))
            area = width ** 2
            return area
        elif choice == "3":
            height = float(input("Enter the height of triangle: "))
            base = float(input("Enter the base of triangle: "))
            area = 1/2 * height * base
            return area
        elif choice == "4":
            length = float(input('Enter the length of rectangle: '))
            width = float(input("Enter the width of rectangle: "))
            area = length * width
            return area
        else:
            return "You haven't entered any choice"    
                      
    except ValueError:
        return "Invalid value"
    
print(calculate_area())    