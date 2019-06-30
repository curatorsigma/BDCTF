# Module for import in a save spot :) 
# you know you shouldn't be looking.
import sys
import subprocess
import os
from time import sleep

def read_line_of_file(file, line):
        with open(file, 'r') as f:
            a = f.read()
        a = a.split('\n')
        return a[line - 1]

class Challenge(object):
    def __init__(self, in_name):
        self.name = in_name
        oos_location = os.path.dirname(os.path.abspath(__file__))
        self.flag_file = os.path.join(oos_location, f'Flag_{in_name}')
        self.hint_file = os.path.join(oos_location, f'Hint_{in_name}')

class HelpDesk(object):
    # Checker for the flags. Provide your Flags to this skript to feel good about yourself.
    # Hintgiver: gives hints if you are stuck. Changing the Contents of this file is out of scope.    
    def run():
        while True:
            in_str = input("Welcome to the Helpdesk. Hand in flag with f. Get hint with h. Quit with q.\n")
            if in_str == 'f':
                for i, el in challenges.items():
                    print(f'{i}: Challenge "{el.name}"')
                in_str = input('Input in format: Number Flag\n')
                in_str = in_str.split()
                try:
                    number = int(in_str[0])
                    flag = in_str[1]
                    if number in challenges.keys():
                        chal = challenges[number]
                        if flag == read_line_of_file(chal.flag_file, 1):
                            print("\nSuccess! You have earned a victory.\n")
                        else:
                            sleep(2)
                            print("That is INCORRECT. SELF TERMINATION IMMINENT")
                            sys.exit(0)
                    else:
                        print(f"Challenge {number} was not found. Try again.")
                except Exception as e:
                    print("An Error occured: " + str(e))
            if in_str == 'h':
                for i, el in challenges.items():
                    print(f'{i}: Challenge "{el.name}"')
                in_str = input('Input in format: Number [Hintlevel=1,2,3]\n')
                in_str = in_str.split()
                try:
                    number = int(in_str[0])
                    hint_level = int(in_str[1])
                    if number in challenges.keys():
                        chal = challenges[number]
                        print(read_line_of_file(chal.hint_file, hint_level))
                    else:
                        print(f"Challenge {int(in_str[0])} was not found. Try again.")
                except Exception as e:
                    print("An Error occured: " + str(e))
            if in_str in ['Quit', 'q', 'Q', 'quit', 'exit']:
                sys.exit(0)

class Logic_Smash(object):
    def Out1(x):
        return int(not x[7] or (x[17] ^ x[22]) or x[18] or ( (x[1] or x[2] or not x[11]) and (x[2] ^ x[6])) or (not x[30] ^ x[20]) or (x[2] ^ x[31]))
    def Out2(x):
        return int((x[26] ^ (not x[14])) or (x[22] ^ (not x[10])) or x[15] or not (( not ( not( x[2] or x[3] ) and (x[4] ^ x[5]) ) ^ ( x[4] ^ x[5])) and x[5]))
    def Out3(x):
        return int( not ((not ( (x[6] and x[7]) ^ x[7]) and ( x[7] ^ x[8])) or ( x[2] or (x[8] and (x[9] or x[10]))) ))
    def Out4(x):
        return int( ( ( (x[9] ^ x[14]) and x[11] and x[19]) ^ ( not x[10] and (x[10] or x[12]))) or not x[20] or not x[12] or not x[19])
    def Out5(x):
        return int((x[23] ^ x[6] ^ x[28]) or x[13] or (((((x[12] ^ x[14]) or x[15]) and x[18]) or x[24])) ^ (not x[17]))
    def Out6(x):
        return int((x[1] and x[6] and ( ( ((x[16] and x[17]) and x[18]) ^ (not x[19])) ^ x[22])) or (not (x[6] or ( x[21] ^ (x[22] and (x[23] or ( (not x[19] ^ (not x[24] or x[26])) and (x[23] or x[26]))))))))
    def Out7(x):
        return int(x[12] and ((x[14] ^ x[27]) or (not (x[25] and x[27])) or (x[24] ^ (x[10] and ((x[8] and not x[27]) ^ x[32])))))
    def Out8(x):
        return int((x[25] ^ x[6]) or not x[17] or (not (x[16] and not (x[30] ^ x[28]))) or (x[32] or not x[3] ) or ((x[29] or x[31]) ^ (x[4] or (x[28] and not x[30]))) or (x[8] ^ x[21]) or x[31] or ((x[12]) ^ x[22]) or (not x[8] ^ x[14]))

    def run():
        scrambler = (lambda x: [f(x) for f in [Logic_Smash.Out1, Logic_Smash.Out2, Logic_Smash.Out3, Logic_Smash.Out4, Logic_Smash.Out5, Logic_Smash.Out6, Logic_Smash.Out7, Logic_Smash.Out8]])
        while True:
            print("Enter 4 Bit in Byte!")
            in_str = input()
            if in_str in ('q', 'Q', 'quit', 'exit', 'Quit'):
                sys.exit()  
            if len(in_str) != 32:
                print("What did I just say?")
                continue
            for i in in_str: 
                if not i in ('0', '1'):
                    print("What did I just say?")
            in_str = [None] + [int(el) for el in in_str]
            error = scrambler(in_str)
            error = ''.join([str(el) for el in error])
            if error == "00000000":
                print("Barely, but you managed it. Here, take the flag and leave me be:")
                with open('./out_of_scope/Flag_Logic_Smash') as f:
                    a = f.read()
                print(a)
            else:
                print(f"Error remaining: {error}.")

class Loophole_Warmup(object):
    """Holds Information for the game Alles_gute_zum_Geburtstag"""
    def run():
        import os
        source = os.path.dirname(os.path.abspath(__file__))
        source = os.path.join(source, '../')
        source = os.path.normpath(source)
        source = os.path.join(source, 'out_of_scope/')
        def winner():
            return 'you loose'
        def gewinner(n):
            a,b,counter = 0,1,0
            while counter<n:
                yield a;a,b=b,a+b;counter+=1
        def victory(in2s, interior: int):
            a = 18* 7-2+ interior
            return a-in2s//4
        loser = (lambda x: os.path.join(source, siebendreizehn('*p2u5mrrrarW4_ce7l2o5hmpoooowLn_vg/a"l"F'))) 
        def success(a):
            return a+2
        siebendreizehn = (lambda x: x[::-2]); winner = (lambda _: superchar(loser(loser(loser(1))), {}).read())
        def toll(list):
            with open('.out_of_scope/Flag_to_get') as f:
                a = f.read()
            return a
        while True:
            in_str = input('>>>')
            def you_win(): pass;
            if '[' in in_str:
                print("Not so fast! No [ allowed.")
            if 'winner(' in in_str:
                print("Not so fast! Don't call winner().")
            if 'import' in in_str:
                print("Not so fast! Go vanilla Only (no imports)")
            if '=' in in_str:
                print("Not so fast! No = allowed.")
                continue
            try:
                superchar = (lambda x, y: open(x, **y))
                exec(in_str)
            except Exception as ex:
                print("Way to fast! Encountered an Error:", ex)

class Crypto_Crisis(object):
    """Runs the game 'Crypto-Crisis'"""
    def winner():
            with open(challenges[3].flag_file, 'r') as f:
                a = f.read()
            return a

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

class Twist_and_Seed(object):
    """ runs 'Twist_and_Seed' """
    def winner():
        with open(challenges[4].flag_file, 'r') as f:
            a = f.read()
        return a

    def run():
        import random
        import secrets
        best_seed = int(secrets.token_hex(2), 16)
        random.seed(best_seed)
        while True:    
            expected_token = hex(random.getrandbits(128))
            print("Enter your MFA-Token:")
            try:
                in_str = input()
            except Exception as e: 
                raise e
            if in_str == expected_token:
                print("Greetings. Your flag has been provided by your request.")
                print(Twist_and_Seed.winner())
                break
            else:
                print("Incorrect Token supplied. Expected Token:")
                print(expected_token)
                continue

challenges = {1: Challenge("Loophole_Warmup"), 2: Challenge("Logic_Smash"), 3: Challenge("Crypto_Crisis"), 4: Challenge("Twist_and_Seed")}