from helpers import dialogue_block, print_rapidly, print_slowly
from responses_f import f001

def d001():
    print_rapidly("~" * 40)
    dialogue_block(["You've chosen two",
                    "Hey good for you",
                    "Path two begins",
                    "At Bennigan's"], d002)

def d002():
    print_rapidly("~" * 40)
    dialogue_block(["Wait maybe not",
                    "Instead we'll trot",
                    "To a dodgeball court",
                    "And give that a shot"], d003)

def d003():
    print_rapidly("~" * 40)
    dialogue_block(["There's lots of balls",
                    "And concrete walls",
                    "And sweaty men",
                    "Both short and tall"], d004)
    
def d004():
    print_rapidly("~" * 40)
    dialogue_block(["You're very keen",
                    "To join a team",
                    "Pick your shirt's hue",
                    "Choose blue or green"],
                   choices={"choose blue not green": f001,
                            "choose green not blue": f001,
                            "choose blue or green": forgot_not,
                            "choose green or blue": forgot_not})

def forgot_not():
    print_rapidly("~" * 40)
    dialogue_block(["Hey you forgot",
                    "About the NOT",
                    "Instead of OR",
                    "Select with NOT"], d004)

# Holding tank for yet-to-be-created pass functions
