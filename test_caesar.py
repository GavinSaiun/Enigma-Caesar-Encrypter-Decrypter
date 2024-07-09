# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
import string

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = "The sky is clear and the stars are shining brightly"
 
#type your message here
print("Message:", message)


#create the Caesar cypher 

"""
Caesar Cipher is a substitution cipher in which each letter in the alphabet
is mapped onto another letter by some fixed position 
e.g. if shift is 3, A would be mapped onto D

Offset: the number that each letter would be shifted down
keys: dictionary mapping each letters to its respective encrypted letter
invkeys: used to map encypted letter to its original letter for decryption

https://en.wikipedia.org/wiki/Caesar_cipher
https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
"""

# Set up the initial parameters 
offset = 10

totalLetters = 26   
keys = {} 
invkeys = {} 

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

print("Cypher Dict:", keys)


#Encrypt message
encryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(keys[letter])
print("Encrypted Message:", ''.join(encryptedMessage))


#Decrypt message
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage))