#Jackson Weigand
# ceaser enc
#10/6/2021


import random

alpha = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

def read(filename):
   file = open(filename)
   info = file.read()
   file.close()
   return info

def write(filename, info):
    file = open(filename, "w+")
    file.write(info)
    file.close()

def encode(message,publick, privatek):
    code=""
    for letter in message:
        code += privatek[publick.find(letter)]
    return code
def decode(message,publick,privatek):
    code = ""
    for letter in message:
        code += publick[privatekey.find(letter)]
    return code
def makekey(text_str, keytype):
    if keytype == "private":
        random.seed(7)
    else:
        random.seed(103)
    text_str = list(text_str)

    random.shuffle(text_str)

    return ''.join(text_str)

# def makekey(keytype):
#     key = [] # create empty list
#     alphasize = len(alpha)
#     for letter in range(0, alphasize):
#         letter = random.randint(0, alphasize-1) # pick a new spot in the list
#     key.append(" ") # load the list with spaces
#     for i in range(0, alphasize):
#         letter = random.randint(0, alphasize-1) # picks a random spot in the list
#
#         while key[letter] != " ": # if that spo is not empty..
#         key[letter] = alpha[i] # if it is empty assign it
#
#     public = "".join(key)
#     return public

# public = shuffle_text(alpha, "public")
# private = shuffle_text(alpha, "private")

# print(public)
# print(alpha)
# print(private)
publickey=""
privatekey =""
while(1):
    task = input("D)ecode or E)ncode or R)ead keys or M)ake keys")

    if task.upper() == "D":
        code=input("Enter your message")
        print("Decoding")
        enc = decode(code,publickey,privatekey)
        print(enc)
    elif task.upper()=="R":
        print("Reading")
        publickey = read("publickey.txt")
        privatekey = read("privatekey.txt")

    elif task.upper()=="M":
        print("Making")
        publickey = makekey(alpha,"public")
        privatekey = makekey(alpha,"private")
        write("publickey.txt", publickey)
        write("privatekey.txt", privatekey)

    else:
        code = input("Enter your message ")
        enc = encode(code,publickey, privatekey)
        print(enc)