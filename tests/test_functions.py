from RFID_mifare_cloner.rfid_mifare_cloner import is_tag_reader_in_devices
from RFID_mifare_cloner.text_utils import bright_color, WHITE, RESET


def test_find_tag_reader_success():
    """ Find the tag reader if it's connected """
    devices_names = ['Ralink Technology, Corp. RT5372 Wireless Adapter', 'Linux Foundation 2.0 root hub',
                     'Advanced Card Systems, Ltd ACR122U']

    assert is_tag_reader_in_devices(devices_names) is True


def test_find_tag_reader_fail():
    """ Find the tag reader if it's connected """
    devices_names = ['Ralink Technology, Corp. RT5372 Wireless Adapter', 'Linux Foundation 2.0 root hub']
    assert is_tag_reader_in_devices(devices_names) is False


def test_bright_colors():
    assert bright_color(WHITE) == '\u001b[37;1m'
    assert bright_color(RESET) == '\u001b[0m'
