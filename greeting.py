from ascii_art import Logo
from print_utils import Show_output


class Greeting :
    def __init__(self):
        self.asc_art = Logo()
        self.show = Show_output()

    def greet(self) :
        '''print the logo and welcome'''
        print(self.asc_art.logo)
        print("** welcome to the caesar cipher ***")
        self.show.line_printer()