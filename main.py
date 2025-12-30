"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kamila Kynčl
email: kamilka.frolikova@gmail.com
"""
import re
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

#slovník s uživatelskými jmény a hesly 
users = { "bob": "123",
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"
         }

#uživatelský vstup
username = input ("username:")
password = input ("password:")
print("-" * 40)

# ověření přihlášení 
import sys 
if username in users and users [username] == password:
    print(f"Welcome to the app, {username}.\nWe have 3 texts to be analyzed.")
else:
    print("unregistered user, terminating the program..")
    sys.exit()

print("-" * 40)

#výběr textu
try:
    TEXT = int(input("Enter a number btw. 1 and 3 to select:"))
    if TEXT not in [1, 2, 3]:
        print("Invalid choice, terminating the program..")
        sys.exit()

except ValueError:
    print("Invalid input, please enter a number.")
    sys.exit()
selected_text = TEXTS[TEXT - 1]

print("-" * 40)

#rozdělení textu na slova a další naše požadavky 
words = selected_text.split()
clean_words = [word.strip(",.!?-") for word in words]
total_words = len(clean_words)
titlecase_words = sum(1 for word in clean_words if word.istitle())
uppercase_words = sum(1 for word in clean_words if word.isupper())
lowercase_words = sum(1 for word in clean_words if word.islower())

numer = [int(num) for num in re.findall(r'\b\d+\b', selected_text)]
total_numbers = len(numer)
sum_numbers = sum(numer)

print("There are " ,total_words, " words in the selected text.")
print("There are " ,titlecase_words, " titlecase words.")
print("There are " ,uppercase_words, " uppercase words.")
print("There are " ,lowercase_words, " lowercase words.")
print("There are " ,total_numbers, " numeric strings.")
print("The sum of all the numbers" ,sum_numbers)

print("-" * 40)

# počítání výskytu délek slov
length_counts = {}
for word in clean_words:
    length = len(word) #délka slova
    if length in length_counts:
        length_counts[length] += 1 #zvýšíme počet
    else:
        length_counts[length] = 1 #přidáme novou délku

#výpis výsledku
print("LEN|  OCCURENCES  |NR.")

print("-" * 40)

for length in sorted(length_counts): #seřazení podle délky 
    print(f"{length}\t | {"*" * length_counts[length]:20} | {length_counts[length]}")
    
    



















    




