# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""


from collections import Counter
import string


"""
A popular and more efficient strategy to break a caesar cipher is to look at 
the most common letter in the decrypted message and assume it is one of the 
most popular letters in the alphabet. e.g. 'e' and shift back



https://thedetectivesociety.com/how-to-solve-ciphers/caesar-cipher/
"""

# Message to be Decrypted 
message = "Dro cui sc mvokb kxn dro cdkbc kbo crsxsxq lbsqrdvi"

#account for upper case letters
message = message.lower()

# Counts all letters in decrypted message
letter_counts = Counter(message)


# finds the most common letter in decrypted message
maxFreq = -1
maxLetter = None

# Stores the popular letter into its respective variable
for letter, freq in letter_counts.items(): 

    if freq > maxFreq and letter != " ":
        maxFreq = freq
        maxLetter = letter


print("Max Ocurring Letter:", maxLetter)

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Top 10 most popular letters ordered via popularity
# sourced from https://en.wikipedia.org/wiki/Letter_frequency
mostPopularLetters = {"e": 5, "t": 20, "a": 1, "o": 15, "i": 9, "n": 14, "s":19, "r": 18, "h":8, "l": 12}


# Finding the shift via subtraction between most popular letter in decrypted message and in English
maxLetterIndex = letters.index(maxLetter)
potentialShifts = []


for letter in mostPopularLetters:
    shift = ((maxLetterIndex + 1) - mostPopularLetters[letter])%26
    potentialShifts.append(shift)



for shift in potentialShifts:
    # Calculate the offset for the Caesar cipher
    offset = 26 - shift

    #create the Caesar cypher
    totalLetters = 26
    keys = {} #use dictionary for letter mapping
    invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict

    # Setting up the Keys and invKeys 
    for index, letter in enumerate(letters):

        
        if index < totalLetters: #lowercase 

            # Maps each letter to its shifted letter and stores into Keys
            keys[letters[index]] = letters[(index + offset)%26]

            # Maps each shifted letter to its original letter and stores into invKeys
            invkeys[letters[(index + offset)%26]] = letters[index]

        else: #uppercase
            keys[letters[index]] = letters[(index + offset)%26].upper()
            invkeys[letters[(index + offset)%26].upper()] = letters[index]


    #Decrypt
    encryptedMessage = []
    for letter in message:
        if letter == ' ': #spaces
            encryptedMessage.append(letter)
        else:
            encryptedMessage.append(keys[letter])
    
    print("Predicted Shift:", shift)
    print("Decrypted Message:", ''.join(encryptedMessage))


