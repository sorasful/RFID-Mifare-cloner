from RFID_mifare_cloner.text_utils import bright_color, WHITE, RESET


def test_bright_colors():
    assert bright_color(WHITE) == "\u001b[37;1m"
    assert bright_color(RESET) == "\u001b[0m"
