import os
import sys
import time
import text_utils as tu
from rfid_mifare_cloner import is_tag_reader_connected, create_dump_tag, write_new_tag
from exceptions import TagNotFoundException, NotClassifMifareTagException


def welcome_screen():
    """ Only shown when the user starts the CLI"""
    ascii_art = """
    ____  ______________     __  ____ ____                   ________                     
   / __ \/ ____/  _/ __ \   /  |/  (_) __/___ _________     / ____/ /___  ____  ___  _____
  / /_/ / /_   / // / / /  / /|_/ / / /_/ __ `/ ___/ _ \   / /   / / __ \/ __ \/ _ \/ ___/
 / _, _/ __/ _/ // /_/ /  / /  / / / __/ /_/ / /  /  __/  / /___/ / /_/ / / / /  __/ /    
/_/ |_/_/   /___/_____/  /_/  /_/_/_/  \__,_/_/   \___/   \____/_/\____/_/ /_/\___/_/                                                                                 
    """
    print(tu.write_text_color(ascii_art, tu.YELLOW))
    print(tu.write_text_color('#RaccoonProgrammer ' + '\n' * 2, tu.bright_color(tu.BLUE)))


def first_screen():
    """ Screen where the user should plug his reader or has already. """
    if not is_tag_reader_connected():
        sys.stdout.write(tu.write_text_color('Please connect your tag reader', tu.bright_color(tu.RED)))
        sys.stdout.flush()
    while not is_tag_reader_connected():
        time.sleep(0.4)
    sys.stdout.write(u"\u001b[1000D") # move cursor to left to erase previous message
    sys.stdout.write(tu.write_text_color('Tag reader detected and connected ! ', tu.bright_color(tu.GREEN)))
    sys.stdout.write('\n'* 5)
    sys.stdout.flush()
    time.sleep(0.5)


def dump_card_screen(tag_to_copy=True):
    """ The screen where the user will put his card he wants to duplicate on the reader. """
    initial_text = 'Put the tag you want to duplicate on the reader. ' if tag_to_copy else 'Put the destination tag to clone to. '
    sys.stdout.write(tu.write_text_color(initial_text, tu.bright_color(tu.RED)))
    sys.stdout.flush()

    valid_tag = False
    while not valid_tag:
        try:
            create_dump_tag('to-copy' if tag_to_copy else 'destination')  # should success or raise something.
            valid_tag = True
        except TagNotFoundException:
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(" " * 80)  # Clear the previous line which is longer that this one.
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(tu.write_text_color(initial_text, tu.bright_color(tu.RED)))
            sys.stdout.flush()
            time.sleep(0.2)

        except NotClassifMifareTagException:
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(tu.write_text_color('This tag is not a classic mifare tag, it won\'t work... Please try another',
                                                 tu.bright_color(tu.RED)))
            sys.stdout.flush()
            time.sleep(0.2)

        except KeyboardInterrupt:
            sys.exit()

        except:
            pass  # Occasionnal errors when trying to access to the device too many times ...

    sys.stdout.write(u"\u001b[1000D")  # move cursor to left to erase previous message
    sys.stdout.write(tu.write_text_color('Card successfully copied ! ', tu.bright_color(tu.GREEN)))
    if tag_to_copy:
        sys.stdout.write(tu.write_text_color('Please, remove the tag from the reader within 10 seconds', tu.bright_color(tu.CYAN)))
    else:
        sys.stdout.write(tu.write_text_color('Don\'t remove the tag, we are processing to the copy of the tag. This shouldn\'t be long ', tu.bright_color(tu.CYAN)))
    sys.stdout.write('\n' * 2)
    sys.stdout.flush()
    if tag_to_copy:
        time.sleep(10)

def write_tag_screen():
    """ The screen when the card is being duplicated to the destination file """

    if write_new_tag(tag_to_copy='to-copy', destination='destination'):
        sys.stdout.write(tu.write_text_color('Card succesfully duplicated ! You can now test it !\n Enjoy !', tu.bright_color(tu.GREEN)))
    else:
        sys.stdout.write(tu.write_text_color('An error has occured, please retry.', tu.bright_color(tu.RED)))
    sys.stdout.flush()


def command_line():
    welcome_screen()
    first_screen()
    dump_card_screen(tag_to_copy=True)  # We first copy data we want to duplicate
    dump_card_screen(tag_to_copy=False)  # then we copy on the destination tag
    write_tag_screen()

    # clean files
    os.remove('to-copy.dmp')
    os.remove('destination.dmp')


if __name__ == '__main__':
    command_line()
