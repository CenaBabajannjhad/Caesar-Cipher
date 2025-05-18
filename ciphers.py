from alphabet import alphabet_list , len_alphabet_list

def encrypt(text , shift) :
    encrypted_message = ""
    
    for char in text :
        if(char != " ") :
            shifted_char_index = alphabet_list.index(char) + shift

            # If the index goes out of range
            if shifted_char_index >= len_alphabet_list :
                out_of_range_value = shifted_char_index - len_alphabet_list
                encrypted_message += alphabet_list[out_of_range_value]
            else :
                encrypted_message +=  alphabet_list[alphabet_list.index(char) + shift]
        else :
            encrypted_message += char
    
    return encrypted_message


def decrypt(text , shift) :
    decrypted_message = ""

    for char in text :
        if(char != " ") :
            shifted_char_index = alphabet_list.index(char) - shift   
            # If the index goes out of range
            if shifted_char_index < 0 :
                out_of_range_value = len_alphabet_list - abs(shifted_char_index)  
                decrypted_message += alphabet_list[out_of_range_value - len_alphabet_list]
            else :
                decrypted_message += alphabet_list[shifted_char_index]

        else :
            decrypted_message += char

    return decrypted_message