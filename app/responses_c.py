from helpers import dialogue_block, print_rapidly, print_slowly
from responses_f import f001

def c001():
    print_rapidly("~" * 40)
    dialogue_block(["You've chosen one",
                    "This will be fun",
                    "Path one begins",
                    "In a dungeon"], c002)

def c002():
    print_rapidly("~" * 40)
    dialogue_block(["Actually no",
                    "Instead we'll go",
                    "To Taco Bell",
                    "For burritos"], c003)

def c003():
    print_rapidly("~" * 40)
    dialogue_block(["The menu is",
                    "A giant list",
                    "Of things to eat",
                    "With sauce packets"], c004)
    
def c004():
    print_rapidly("~" * 40)
    dialogue_block(["And now we're brought",
                    "A choice of what",
                    "Sauce drives you wild",
                    "Choose mild or hot"],
                   choices={"choose mild not hot": f001,
                            "choose hot not mild": f001,
                            "choose mild or hot": forgot_not,
                            "choose hot or mild": forgot_not})

def forgot_not():
    print_rapidly("~" * 40)
    dialogue_block(["Hey you forgot",
                    "About the NOT",
                    "Instead of OR",
                    "Select with NOT"], c004)

# Holding tank for yet-to-be-created pass functions

def e001():
    pass


    
# def c004():
#     print_rapidly("~" * 40)
#     while True:
#         print_slowly("And now we're brought")
#         user_input = input()
#         if user_input.lower() == "and now we're brought":
#             break

#     while True:
#         print_slowly("A choice of what")
#         user_input = input()
#         if user_input.lower() == "a choice of what":
#             break

#     while True:
#         print_slowly("Sauce drives you wild")
#         user_input = input()
#         if user_input.lower() == "sauce drives you wild":
#             break

#     while True:
#         print_slowly("Choose mild or hot")
#         user_input = input()
#         if user_input.lower() == "choose mild not hot":
#             e001()
#             break
#         elif user_input.lower() == "choose hot not mild":
#             f001()
#             break
#         elif user_input.lower() == "choose mild or hot":
#             forgot_not()
#             break
#         elif user_input.lower() == "choose hot or mild":
#             forgot_not()
#             break

# works but sends back to the start of the stanza
# def c004():
#     print_rapidly("~" * 40)
#     while True:
#         print_slowly("And now we're brought")
#         user_input = input()

#         if user_input.lower() == "and now we're brought":
#             print_slowly("A choice of what")
#             user_input = input()
#             if user_input.lower() == "a choice of what":
#                 print_slowly("Sauce drives you wild")
#                 user_input = input()
#                 if user_input.lower() == "sauce drives you wild":
#                     print_slowly("Choose mild or hot")
#                     user_input = input()
#                     if user_input.lower() == "choose mild not hot":
#                         e001()
#                         break
#                     elif user_input.lower() == "choose hot not mild":
#                         f001()
#                         break
#                     elif user_input.lower() == "choose mild or hot":
#                         forgot_not()
#                         break
#                     elif user_input.lower() == "choose hot or mild":
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
#                         c004()
#                         break