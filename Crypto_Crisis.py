#!/usr/bin/env python3
# Changing this file is out of scope.
from out_of_scope.Game import Crypto_Crisis

Crypto_Crisis.run()

# The run() function is defined as follows:
"""
def run():
    from hashlib import sha256
    print("Trying to execute File 'Crypto_Crisis_onload.py' ...")
    try:
        with open('Crypto_crisis_onload.py', 'r') as f:
            a = f.read().split('\n')
        print("Validating Hash...")
        hash_complete = 0
        for x in a:
            h = sha256()
            h.update(x.encode('utf-8'))
            hash_curr = h.hexdigest()
            hash_curr = int(hash_curr[:2], 16)
            hash_complete ^= hash_curr
        if hash_complete != 0:
            print(f"Got Hashresult {hash_complete}, Expected 0. The Supplied File was ignored.")
        else:
            print("... hash is correct.")
            print("There you go, sir:")
            subprocess.run(['python3', './Crypto_Crisis_onload.py', Crypto_Crisis.winner()])
    except Exception as e:
        print("Error occured:" + str(e))
"""
# Crypto_Crisis.winner() contains the flag you want so dearly