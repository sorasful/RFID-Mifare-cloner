import sys
import tty
import time
import text_utils as tu
from rfid_mifare_cloner import is_tag_reader_connected

def welcome_screen():
    """ Only shown when the user starts the CLI"""
    ascii_art = """
    ____  ______________     __  ____ ____                   ________                     
   / __ \/ ____/  _/ __ \   /  |/  (_) __/___ _________     / ____/ /___  ____  ___  _____
  / /_/ / /_   / // / / /  / /|_/ / / /_/ __ `/ ___/ _ \   / /   / / __ \/ __ \/ _ \/ ___/
 / _, _/ __/ _/ // /_/ /  / /  / / / __/ /_/ / /  /  __/  / /___/ / /_/ / / / /  __/ /    
/_/ |_/_/   /___/_____/  /_/  /_/_/_/  \__,_/_/   \___/   \____/_/\____/_/ /_/\___/_/                                                                                 
    """
    print(ascii_art)
    print(tu.write_text_color('#RaccoonProgrammer', tu.BLUE))


def first_screen():
    """ Screen where the user should plug his reader or has already. """
    if not is_tag_reader_connected():
        sys.stdout.write(tu.write_text_color('Please connect your tag reader', tu.RED))
        sys.stdout.flush()
    while not is_tag_reader_connected():
        time.sleep(0.2)
    sys.stdout.write(u"\u001b[1000D") # move cursor to left to erase previous message
    sys.stdout.write(tu.write_text_color('Tag reader detected and connected ! ', tu.GREEN))


def command_line():
    welcome_screen()
    first_screen()

if __name__ == '__main__':
    command_line()