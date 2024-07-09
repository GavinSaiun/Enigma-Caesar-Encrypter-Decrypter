
"""
I started off with assuming that each number is associated to a letter
the only clue was something related to Japan and America in 1941
Main guess was Pearl Harbor in 1941 Decemeber Seven
19 17 17 19 14 20 23 18 19 8 12 16 19 8 3 21 8 25 18 14 18 6 3 18 8 15 18 22 18 11

Strategy 1:
i first thought it was a caesar cipher, and decoded the numbers into their respective letters
after cycling throught all shifts, i reasoned it to be improbable

Strategy 2
i assumed each number is associated with a letter, with not relation to its position
I noticed that Harbor has 2 r's spaced exactly 2 spaces away
So i looked for 2 numbers that are both the same, spaced as such and has enought space to fit the word Harbor
i narrowed it down to  8 3 21 8 and 18 6 3 18 8 15 18 22 18 
i substituted the letters:

8 3 21 8
R B  O R
I assummed the numbers before this sequence is probably PEARL HARBOR
23 18 19 8 12 16 19 8 3 21 8
P  E  A  R L  H  A  R B O  R
Map each number to each respective Letter and work back
{P: 23, E: 18, A: 19, R: 8, L: 12, H: 16, B: 3, O: 21}
A _ _ A _ _ P E A R L, H A R B O R, _ E _ E _ _ E R B E_ E _
guessed that the first word is ATTACK based on the 2 consecutive letters 
T: 17, C: 14, K: 20
A T T A C K, P E A R L, H A R B O R, _ E C E _ B E R   _ E_ E _
Resembles December Seven
since pearl harbor happened on DECEMBER SEVEN
THAT WAS MY FINAL GUESS
ATTACK PEARL HARBOR DECEMBER SEVEN

"""