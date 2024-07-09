# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""

import string
import enigma
import rotor

"""
A common strategy to decrypt a message without knowing the key is using cribs.
Cribs are by definition words that are known plaintext or suspected plaintext
at some point in an enciphered message. Once found out, they can use this
information to deduce the rotor settings and encrypt.

https://www.101computing.net/enigma-crib-analysis/
"""

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
print(capitalLetters)

# Encoded Message to be decypted
ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"
crib_substring = "Gdwm Qopjmw!"
print(crib_substring)

# Counts the number of attempts
counter = 0

# Run thourgh every possible key and see if the crib matches with its encrypted variant
for letter1 in capitalLetters:
    for letter2 in capitalLetters:
        for letter3 in capitalLetters:

            engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                            rotor.ROTOR_II, rotor.ROTOR_III,
                                             key=f"{letter1}{letter2}{letter3}",
                                              plugs="AA BB CC DD EE")
            
            decrypted_message = engine.encipher(ShakesHorribleMessage)
            counter+=1  
            
            if crib in decrypted_message:                    
                print(f"Enigma Key is: {letter1}, {letter2}, {letter3}")
                print(decrypted_message)
                print(f"{counter} Number of Keys Tried So far")
                
        


            
print(f"Total number of Possible Keys are {counter}")


"""
SECTION II PART C

Enigma Key is: R, K, T
To all my loyal Spider Monkeys! Half of you are to attack the enemy on their left flank.
Half of you are to attack the enemy on their right flank and the rest of you shall come 
with me down the middle! Hail Shakes!

"""


"""
SECTION II PART D

11772 Number of Keys Tried So far
Counter = 17576 different possible keys used 
Took My Computer 7.914 Seconds

Each Try would require the operator to take out the 3 rotors (5 seconds)
i assume that changing each rotor's initial position would take 5 seconds 
we would only have to change one rotor at a time and rotate it one position as the code above runs as such
AAA, AAB, AAC, AAD
Putting the rotors back (5 seconds)
15 seconds to setup one key
time to input message and decrypt = 15 seconds (can save time an just do it on the crib and see if it equals HAIL SHAKES)
Total time to decrypt using one key = 30 seconds
Total time to run through all keys = (17570 x 30)/3600 = 146.4 hours
Average time to run through all keys = 146.4/2 = 73.2 Hours
these times are based on the demonstration provided in https://www.youtube.com/watch?v=-mdSvGUd0_c

"""

"""
SECTION III PART E

Original Case
Number of rotors(3) combinations are 3x2x1 = 6
number of possible keys (starting position) is 26x26x26 = 17576
105,456 total ways to encrypt

Assuming that Shakes bought 2 extra rotors for 5 total, and a plugboard with 10 pairs
Number of possible rotors combinations are 5x4x3 = 60
Number of possible keys (starting positions) is 26x26x26 = 17576
Plugboard combinations are 26!/(6! 10! 2^10) = 150738274937250
total possible configurations = rotor combinations x possible keys x plugboard combinations
                              = 158 962 555 217 826 360 000 total combinations to try

Assuming that the modern day core can manage around 3 billion operations in a second (and assume it is solely using it on this program)
lets say it takes 1000 operations to decodes 1 message
1 core can try 3 million configurations in a second
158,962,555,217,826,360,000 / 3,000,000 = 5.3 x 10^13 seconds
                                        = 1,680,223 Years 

https://medium.com/@mihsathe/cracking-the-enigma-code-today-35c8a97f5e26#:~:text=So%20to%20try%20all%20possibilities,isn't%20an%20option%20today!
"""



