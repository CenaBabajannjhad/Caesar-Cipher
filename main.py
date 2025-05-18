from greeting import greet
from print_utils import show_result
from ciphers import encrypt , decrypt

should_continue = True

greet()

while should_continue :
    direction = input("Type 'e' to encrypt, Type 'd' to decrypt: \n").lower()
    user_text = input("Type your message : ").lower()
    user_shift = int(input("Type the shift number : "))

    if direction == "e" :
        if user_text != "" and user_shift <= 26 :
            result = encrypt(user_text , user_shift)
            show_result(result , "encode")
            # check user want continue
            user_want_continue = input("Type 'y' if you want to go again. otherwise type 'n'. ").lower() 
            if user_want_continue == "n" : should_continue = False
        else : 
            print("Error\n Text cannot be left blank\n Or Shift must be lower then 26\n check it")

    elif direction == "d" :
        if user_text != "" and user_shift <= 26 :
            result = decrypt(user_text , user_shift)
            show_result(result , "decode")
            # check user want continue
            user_want_continue = input("Type 'y' if you want to go again. otherwise type 'n'. ").lower()
            if user_want_continue == "n" : should_continue = False
        else : 
            print("Error ,Text cannot be left blank.\n Or Shift must be lower then 26 \n check it")

