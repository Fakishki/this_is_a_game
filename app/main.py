from ipdb import set_trace

from helpers import *
from responses_b import *
from responses_c import *
from responses_f import *
import os
import platform

if __name__ == '__main__':
    def main_menu():
        while True:
            print_very_slowly("This is a game")
            user_input = input()
            if user_input.lower() == "this is a game":
                print_very_slowly("It's kind of lame")
                user_input = input()
                if user_input.lower() == "it's kind of lame":
                    print_very_slowly("To play along")
                    user_input = input()
                    if user_input.lower() == "to play along":
                        print_very_slowly("Repeat the same")
                        user_input = input()
                        if user_input.lower() == "repeat the same":
                            b001()
                            break
    
    def clear_console():
        system = platform.system()
        if system == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    
    clear_console()
    print_slower("This program was created as a tech demo.")
    print_slower("It's designed to explore potential methods to give users choice in a text-based game.")
    print_slower("The program functions like a poetry-based game of simon says.")
    print_slower("You will be given a line, and must enter that line in response, to move on to the next line in the stanza.")
    print_slower("You don't have to worry about capitalization, but your spelling and punctuation must be correct")
    print_slower("At certain points, you'll be given the opportunity to choose between two options using the word NOT.")
    print_slower("The game will introduce and (try to) explain this concept to you (poorly). Just go with it...")
    while True:
        print_slower("When you're ready to start, please type the word START and hit <enter>")
        user_input = input()
        if user_input.lower() == "start":
            clear_console()
            main_menu()