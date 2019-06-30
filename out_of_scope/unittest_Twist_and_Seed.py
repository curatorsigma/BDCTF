#!/usr/bin/env python3
import subprocess
import os
import sys
import asyncio

def write_tokens_to_file(list):
    with open('tmp_tokens', 'a+') as f:
        for x in encountered_tokens:
            print(x, file=f)

def read_tokens_from_file():
    out_list = []
    with open('tmp_tokens', 'r') as f:
        for l in f:
            out_list.append(l)
    return out_list



# get input from childprocess
async def read_input(process):
    to_proc = await process.stdout.readline()
    to_proc = [chr(el) for el in to_proc]
    to_proc = to_proc[:-1]
    to_proc = ''.join(to_proc)
    return to_proc

# main method
async def main():
    # set first token
    next_token = encountered_tokens[0] if len(encountered_tokens) > 0 else "a"
    
    # create new instances (to get new seeding)
    i = 1
    while True:
        print("Erzeuge neuen Seed", i//3)
        try:
            # create a new childprocess
            proc = await asyncio.create_subprocess_shell(sys.executable + ' ' + script_file, 
                                stdin=subprocess.PIPE, 
                                stdout=subprocess.PIPE
            )
        
            # listen for input
            hitflag = 0
            while True:
                if hitflag > 0:
                    hitflag -= 1
                if i%3 == 0 and hitflag == 0:
                    i += 1
                    proc.kill()
                    break
                if i%1000 == 0:
                    write_tokens_to_file(encountered_tokens)



                p_output = await read_input(proc)
                if p_output == '':
                    pass
                # got input:
                else:
                    i += 1
                    #print(f'Input finished processing: {p_output}')
                    if p_output == "Incorrect Token supplied. Expected Token:":
                        p_token_ex = await read_input(proc)
                        # we have the next token that we have to expect.
                        if p_token_ex in encountered_tokens:
                            hitflag = 2
                            print("Found duplicate Token.")
                            # next we will send the token that followed last time
                            next_token = encountered_tokens[encountered_tokens.index(p_token_ex)+1]
                            continue
                        encountered_tokens.append(p_token_ex)
                    elif p_output == "Enter your MFA-Token:":
                        # we send the token we think is correct
                        proc.stdin.write(f'{next_token}\n'.encode('utf-8'))
                        await proc.stdin.drain()
                        continue
                    else:
                        print("Unknown Input:  " + p_output)
                        breakpoint()
                        continue
        except Exception as e:
            raise e
        finally:
            write_tokens_to_file(encountered_tokens)
            proc.kill()

        

if __name__ == '__main__':
    # Skriptfile to be executed
    source = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(source, '../')
    source = os.path.normpath(source)
    script_file = os.path.join(source, 'Twist_and_Seed.py')

    # initialize tokens
    encountered_tokens = read_tokens_from_file()


    # and run
    asyncio.run(main())