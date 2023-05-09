from helpers import *
from responses_c import c001
from responses_d import d001

def b001():
    print_rapidly("~" * 40)
    dialogue_block(["That's very good",
                    "You understood",
                    "To repeat back",
                    "Just as you should"], b002)
    
def b002():
    print_rapidly("~" * 40)
    dialogue_block(["There will come times",
                    "Amongst these rhymes",
                    "You'll have to choose",
                    "To continue this climb"], b003)

def b003():
    print_rapidly("~" * 40)
    dialogue_block(["Like when I say",
                    "Choose yay or nay",
                    "You'll maybe pick",
                    "Choose yay NOT nay"], b004)

def b004():
    print_rapidly("~" * 40)
    dialogue_block(["Or it could play",
                    "The other way",
                    "Switch them around",
                    "Choose nay NOT yay"], b005)
    
def b005():
    print_rapidly("~" * 40)
    dialogue_block(["Now we come to",
                    "A choice for you",
                    "Choosing is fun",
                    "Choose one or two"],
                   choices={"choose one not two": c001,
                            "choose two not one": d001,
                            "choose one or two": forgot_not,
                            "choose two or one": forgot_not})

def forgot_not():
    print_rapidly("~" * 40)
    dialogue_block(["Hey you forgot",
                    "About the NOT",
                    "Instead of OR",
                    "Select with NOT"], b005)

# Below is the old version of this code.  It was refactored for two reasons:
# 1. The refactored code is much shorter, using a dialogue_block helper function from our helpers file
# 2. The refactored code allows the user to just go back to the current line when they make an error
#         (The old code made the user restart the stanza)

# def b001():
#     print_rapidly("~" * 40)
#     while True:
#         print_slowly("That's very good")
#         user_input = input()

#         if user_input.lower() == "that's very good":
#             print_slowly("You understood")
#             user_input = input()
#             if user_input.lower() == "you understood":
#                 print_slowly("Remember this")
#                 user_input = input()
#                 if user_input.lower() == "remember this":
#                     print_slowly("And you'll git gud")
#                     user_input = input()
#                     if user_input.lower() == "and you'll git gud":
#                         b002()
#                         break

# def b002():
#     print_rapidly("~" * 40)
#     while True:
#         print_slowly("There will come times")
#         user_input = input()

#         if user_input.lower() == "there will come times":
#             print_slowly("Amongst these rhymes")
#             user_input = input()
#             if user_input.lower() == "amongst these rhymes":
#                 print_slowly("You'll have to choose")
#                 user_input = input()
#                 if user_input.lower() == "you'll have to choose":
#                     print_slowly("So we can climb")
#                     user_input = input()
#                     if user_input.lower() == "so we can climb":
#                         b003()
#                         break

# def b003():
#     print_rapidly("~" * 40)
#     while True:
#         print_slowly("Like when I say")
#         user_input = input()

#         if user_input.lower() == "like when i say":
#             print_slowly("Choose yay or nay")
#             user_input = input()
#             if user_input.lower() == "choose yay or nay":
#                 print_slowly("You'll maybe pick")
#                 user_input = input()
#                 if user_input.lower() == "you'll maybe pick":
#                     print_slowly("Choose yay NOT nay")
#                     user_input = input()
#                     if user_input.lower() == "choose yay not nay":
#                         b004()
#                         break             

# def b004():
#     print_rapidly("~" * 40)
#     while True:
#         print_slowly("Or it could play")
#         user_input = input()

#         if user_input.lower() == "or it could play":
#             print_slowly("The other way")
#             user_input = input()
#             if user_input.lower() == "the other way":
#                 print_slowly("Switch them around")
#                 user_input = input()
#                 if user_input.lower() == "switch them around":
#                     print_slowly("Choose nay NOT yay")
#                     user_input = input()
#                     if user_input.lower() == "choose nay not yay":
#                         b005()
#                         break

# def b005():
#     print_rapidly("~" * 40)
#     while True:
#         print_slowly("Now I'll ask you")
#         user_input = input()

#         if user_input.lower() == "now i'll ask you":
#             print_slowly("Pick one or two")
#             user_input = input()
#             if user_input.lower() == "pick one or two":
#                 print_slowly("Choosing is fun")
#                 user_input = input()
#                 if user_input.lower() == "choosing is fun":
#                     print_slowly("Choose one or two")
#                     user_input = input()
#                     if user_input.lower() == "choose one not two":
#                         c001()
#                         break
#                     elif user_input.lower() == "choose two not one":
#                         d001()
#                         break
#                     elif user_input.lower() == "choose one or two":
#                         forgot_not()
#                         break
#                     elif user_input.lower() == "choose two or one":
#                         forgot_not()
#                         break



# def forgot_not():
#     print_rapidly("~" * 40)
#     while True:
#         print_slowly("Hey you forgot")
#         user_input = input()

#         if user_input.lower() == "hey you forgot":
#             print_slowly("About the NOT")
#             user_input = input()
#             if user_input.lower() == "about the not":
#                 print_slowly("Instead of OR")
#                 user_input = input()
#                 if user_input.lower() == "instead of or":
#                     print_slowly("Make choice with NOT")
#                     user_input = input()
#                     if user_input.lower() == "make choice with not":
#                         b005()
#                         break
