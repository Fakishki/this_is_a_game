from helpers import dialogue_block, print_rapidly, print_slowly, print_very_slowly
import sys

def f001():
    print_rapidly("~" * 40)
    dialogue_block(["You might like this game",
                    "But I wouldn't blame",
                    "If all of the typing",
                    "Was becoming mundane"], f002)

def f002():
    print_rapidly("~" * 40)
    dialogue_block(["There's more I should say",
                    "If you'd rather not play",
                    "I can just write away",
                    "You don't need to reply",
                    "Shall we give that a try?\
                        (No repeating, just type YES or NO)"],
                   choices={"yes": f003,
                            "no": f003})
                         


def f003():
    print_rapidly("~" * 40)
    print_rapidly("~" * 40)
    print_rapidly("~" * 40)
    print_rapidly("~" * 40)
    print_slowly("""
      The end
    """)

    print_very_slowly("Goodbye.  Okay.  We're done.")
    sys.exit()

# def forgot_not():
#     print_rapidly("~" * 40)
#     dialogue_block(["Hey you forgot",
#                     "About the NOT",
#                     "Instead of OR",
#                     "Select with NOT"], c004)

# Holding tank for yet-to-be-created pass functions

