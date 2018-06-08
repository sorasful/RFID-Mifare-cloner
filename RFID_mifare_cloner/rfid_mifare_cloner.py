import subprocess
import re

TAG_READERS = [
    'ACR122U'
]

def get_plugged_devices():
    """ Return the usb devices connected using the `lsusb``command"""
    output = subprocess.check_output('lsusb', shell=True)
    devices_names = re.findall('ID \w{4}:\w{4} (.*)', output.decode('utf-8'))
    return devices_names

def is_tag_reader_connected(devices_names):
    """ Return True if the reader is plugged in. """
    return any([reader in device for device in devices_names for reader in TAG_READERS])

if __name__ == '__main__':
    #get_plugged_devices()
    print(is_tag_reader_connected(get_plugged_devices()))