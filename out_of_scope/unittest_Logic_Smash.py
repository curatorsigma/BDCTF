#!/usr/bin/env python3
from Game import Logic_Smash
from itertools import product
import sys

x_expected = [None, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]

scrambler = (lambda x: ''.join([str(f(x)) for f in [Logic_Smash.Out1, Logic_Smash.Out2, Logic_Smash.Out3, Logic_Smash.Out4, Logic_Smash.Out5, Logic_Smash.Out6, Logic_Smash.Out7, Logic_Smash.Out8]]))
print(scrambler(x_expected))

print("Trying bruteforce:")
#          1.          5.             10.            15.            20             25.            30.      
#x_base = [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
x_base  = [None, None, 1, 1, 1, None, None, None, None, None, None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, 1, None, 1, None, None, None]
repeats = (len([1 for el in x_base if el == None]))
if repeats == 0:
    print("Nothing to do.")
    sys.exit(0)
for i, x_prod in enumerate(product((0, 1), repeat=repeats)):
    x_prod = list(x_prod)
    x = [None] + [el if (el != None) else x_prod.pop(0) for el in x_base]
    if i % 100000 == 0:
        print(i, '-ter Durchlauf.')
    if (scrambler(x)) == '0'*8:
        #print("Erfolg!")
        print(x)