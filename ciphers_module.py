from alphabet import Alphabet

class Ciphers :

    def __init__(self):
        self.alphabet = Alphabet()
        self.alpha_len = self.alphabet.alphabet_list_len()
        self.alpha_list = self.alphabet.alphabet_list

    def encrypt(self , text , shift) :
        '''This method get text and shift for encrypting and return the encrypted text'''
        encrypted_message = ""
        for char in text :
            if(char != " ") :
                shifted_char_index = self.alpha_list.index(char) + shift

                # If the index goes out of range
                if shifted_char_index >= self.alpha_len :
                    out_of_range_value = shifted_char_index - self.alpha_len
                    encrypted_message += self.alpha_list[out_of_range_value]
                else :
                    encrypted_message +=  self.alpha_list[self.alpha_list.index(char) + shift]
            else :
                encrypted_message += char

        return encrypted_message



    def decrypt(self , text , shift) :
        '''This method get text and shift for decrypting and return the decrypted text'''
        decrypted_message = ""
        for char in text :
            if(char != " ") :
                shifted_char_index = self.alpha_list.index(char) - shift   
                # If the index goes out of range
                if shifted_char_index < 0 :
                    out_of_range_value = self.alpha_len - abs(shifted_char_index)  
                    decrypted_message += self.alpha_list[out_of_range_value - self.alpha_len]
                else :
                    decrypted_message += self.alpha_list[shifted_char_index]
            else :
                decrypted_message += char

        return decrypted_message