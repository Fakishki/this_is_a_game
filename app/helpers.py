from ipdb import set_trace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased
import time

engine = create_engine('sqlite:///development.db')
session = sessionmaker(bind=engine)()

# newest trial WORKS FOR EVERYTHING SO FAR!!!!  MAKE SURE YOU HAVE pass funcitons in for unused options.
def dialogue_block(texts, next_func=None, choices=None):
    for index, text in enumerate(texts):
        if index == len(texts) - 1 and choices:
            while True:
                print_slowly(text)
                user_input = input()
                if user_input.lower() in choices:
                    choices[user_input.lower()]()
                    break
        else:
            print_slowly(text)
            user_input = input()
            while user_input.lower() != text.lower():
                print_slowly(text)
                user_input = input()
    if next_func and not choices:
        next_func()




# old dialogue_block version works for all but the refactored choice WE CAN MAKE A NEW REFACTOR FOR CHOICE
# def dialogue_block(texts, next_func=None):
#     for text in texts:
#         print_slowly(text)
#         user_input = input()
#         while user_input.lower() != text.lower():
#             print_slowly(text)
#             user_input = input()
#     if next_func:
#         next_func()

# other old dialogue_block  version
# def dialogue_block(texts, next_func=None):
#     for index, text in enumerate(texts):
#         if index < len(texts) - 1:
#             print_slowly(text)
#             user_input = input()
#             while user_input.lower() != text.lower():
#                 print_slowly(text)
#                 user_input = input()
#         else:
#             print_slowly(text)
#     if next_func:
#         next_func()

# crazy old forgot_not version
# def forgot_not(prev_stanza):
#     print_rapidly("~" * 40)
#     dialogue_block(["Hey you forgot",
#                     "About the not",
#                     "Instead of or",
#                     "Make choice with not", prev_stanza()])
    # while True:
    #     print_slowly("Hey you forgot")
    #     user_input = input()

    #     if user_input.lower() == "hey you forgot":
    #         print_slowly("About the not")
    #         user_input = input()
    #         if user_input.lower() == "about the not":
    #             print_slowly("Instead of or")
    #             user_input = input()
    #             if user_input.lower() == "instead of or":
    #                 print_slowly("Make choice with not")
    #                 user_input = input()
    #                 if user_input.lower() == "make choice with not":
    #                     prev_stanza()
    #                     break

# These methods determine text printing speed

def print_very_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.08)
        # time.sleep(0)
    print()

def print_slower(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.05)
        # time.sleep(0)
    print()

def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.02)
        # time.sleep(0)
    print()

def print_kinda_slow(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.008)
        # time.sleep(0)
    print()

def print_rapidly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.004)
        # time.sleep(0)
    print()