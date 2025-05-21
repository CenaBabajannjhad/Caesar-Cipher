from greeting import Greeting
from print_utils import Show_output
from ciphers_module import Ciphers

class CipherApp :

    def __init__(self):
        self.cipher = Ciphers()
        self.greeting = Greeting()
        self.show = Show_output()
        self.should_continue = True

    def get_user_input(self):
        '''this method get as user the direction , text , shift and return these'''
        direction = input("Type 'e' to encrypt, Type 'd' to decrypt : ").lower()
        text = input("Type your message : ").lower()
        shift = int(input("Type the shift number : "))
        return direction , text , shift

    def validate_user_input(self, text , shift):
        '''this method validate the user text not empty string and the shift be lower then 26 and grater than 0'''
        return text != "" and 0 <= shift <= 26
    
    def process(self):
        '''this method process on the user data'''
        self.greeting.greet()
        # process place
        while self.should_continue :
            direction , text , shift = self.get_user_input()

            if not self.validate_user_input(text , shift):
                print("Error: Text cannot be blank and shift must be between 0 and 26.")
                continue

            if direction == "e":
                result = self.cipher.encrypt(text , shift)
                self.show.show_result(result , "encode")

            elif direction == "d":
                result = self.cipher.decrypt(text , shift)
                self.show.show_result(result , "decode")

            else :
                print("Invalid direction, choose 'e' or 'd'.")


    def ask_continue(self):
        user_choice = input("Type 'y' to go again, or 'n' to exit: ").lower()
        if user_choice == 'n':
            self.should_continue = False


if __name__ == "__main__":
    app = CipherApp()
    app.process()
