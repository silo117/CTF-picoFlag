'''Here's the code that came with the PW Crack 3 scenario from picoCTF plus my additions.  The uncommented portion is what I did to find out which was the correct password.  With only
seven choices, it would have been easy enough to try them all, but I figure I'm not just trying to efficiently solve the problem, but also learn and practice new skills
so I should probably implement a code-based solution.  I simply ganked the list of possible passwords, then iterated through them comparing to see which one had a matching hash.
after figuring out it was the last one, I commented out my code, reran the code and put the correct pw in to get the flag.  I could have thrown in a conditional statement 
to print either the one that matched or the index of the matching choice, but, here I did elect to not spend that time coding because the scope of the problem was small.'''
import hashlib

'''### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level3.flag.txt.enc', 'rb').read()'''
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
j = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]#list of possibles, taken from what's line 52 here
for i in j:                                                 #iterating through
    print(hash_pw(i)== correct_pw_hash)                     #creating hash, checking against correct hash, and printing if True or False

'''
def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_3_pw_check()


# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]

'''
