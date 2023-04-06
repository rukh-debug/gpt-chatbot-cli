import termcolor
import time

def print_char_by_char(start_string, text):
    print(start_string, end=" ")
    for char in text:
        print(termcolor.colored(char, 'light_yellow'), end='', flush=True)
        time.sleep(0.01)
    print()

def print_whole_but_color(start_string, text):
    print(start_string, end=" ")
    print(termcolor.colored(text, 'light_yellow'), end='', flush=True)
    print()