import subprocess
import re
import logging

# Add here others models
TAG_READERS = [
    'ACR122U'
]


def get_plugged_devices():
    """ Return the usb devices connected using the `lsusb``command"""
    output = subprocess.check_output('lsusb', shell=True)
    devices_names = re.findall('ID \w{4}:\w{4} (.*)', output.decode('utf-8'))
    return devices_names


def is_tag_reader_in_devices(devices_names):
    """ Return True if the reader is plugged in. """
    return any([reader in device for device in devices_names for reader in TAG_READERS])


def is_tag_reader_connected():
    return is_tag_reader_in_devices(get_plugged_devices())


def create_dump_tag(name: str):
    """ Create a file .dmp which contains data of cards"""
    try:
        subprocess.check_call(f"mfoc -P 500 -O {name}.dmp", shell=True, stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)
        return True
    except Exception as e:
        return False


def write_new_tag(tag_to_copy: str , destination: str):
    """ Writes the tag_to_co """
    try:
        subprocess.check_call(f"nfc-mfclassic W a {tag_to_copy}.dmp {destination}.dmp", shell=True,
                                 stderr=subprocess.STDOUT)
        return True   # Return true because it will return 0 and it will be considerd as False.
    except Exception as e:
        logging.error(f'Could\'t write_new_tag  : \n {e}')
        return False

if __name__ == '__main__':
    from cli import command_line
    command_line()