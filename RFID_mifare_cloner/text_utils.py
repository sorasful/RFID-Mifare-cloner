
# COLORS
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = "\u001b[0m"


def bright_color(color: str):
    """ Return the bright version of color, doens't work for RESET"""
    return f'{color};1'

def write_text_color(text: str, color:str):
    """Write the text in a color then reset the color."""
    return f'{color}{text}{RESET}'
