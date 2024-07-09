# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import enigma
import rotor

"""
Enigma Machine is a cipher device used in WW2. Core components include rotor
and plugboard. Usually most enigmas have 5-8 rotors, in which 3 are chosen. Each
Rotor contains 26 scrambled letters and as the operator presses a letter to be 
ciphered, the rotor would rotate. As the first rotor makes a full rotation, the 
second rotor would rotate one place and so on. Thus, the key is everchanging. 

To decrypt a message, one must have the initial key set up and knowledge of both
the rotors used and plugboard settings.

https://en.wikipedia.org/wiki/Enigma_machine
"""

#Enigma machine and it initial parameters
engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="ABC",
                                plugs="AA BB CC DD EE")

print(engine)


# Part a)
message = "Hello World"

print("Message:", message)

secret = engine.encipher(message)

print("Encoded Message:", secret)

#Write code to decrypt message below

#To decrypt the above encoded message, we must reset the enigma machine
#back to its initial settings (e.g. key/rotor initial position).

engine.rotor1.state = 'A'
engine.rotor2.state = 'B'
engine.rotor3.state = 'C'

decrypted_message = engine.encipher(secret)
print("decrypted message:", decrypted_message)


#Part b)
ShakesHorribleMessage = "Vxye ajgh D yf? Ptn uluo yjgco L ws nznde czidn. Bsj ccj qdbk qjph wpw ypxvu!"

#Shake's Key is SSC, thus, we must use such key to decrypt
engine.rotor1.state = 'S'
engine.rotor2.state = 'S'
engine.rotor3.state = 'C'

decrypted_message = engine.encipher(ShakesHorribleMessage)
print("decrypted message:", decrypted_message)        

    