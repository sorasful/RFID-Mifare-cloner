import subprocess
import logging
from exceptions import NotClassifMifareTagException, TagNotFoundException
import sys
import shutil


def check_dependencies_installled():
    assert sys.version >= "3"  # Should be python 3.6 at least

    if not shutil.which("nfc-list"):
        print(
            "nfc-list not found, make sure it's installed and in your PATH. See README.md"
        )
        sys.exit(1)
    if not shutil.which("mfoc"):
        print(
            "nfc-list not found, make sure it's installed and in your PATH. See README.md"
        )
        sys.exit(1)


def is_tag_reader_connected():
    output = subprocess.check_output("nfc-list", shell=True)
    return not "No NFC device found" in output.decode("utf-8")


def create_dump_tag(name: str):
    """ Create a file .dmp which contains data of cards"""
    try:
        output = subprocess.check_output(
            f"mfoc -P 500 -O {name}.dmp", shell=True, stderr=subprocess.STDOUT
        )
        if "Found Mifare" in output.decode("utf-8"):
            return True
    except Exception as e:
        output = e.output.decode("utf-8")
        if "only Mifare Classic" in output:
            raise NotClassifMifareTagException()
        elif "No tag found." in output:
            raise TagNotFoundException()
        else:
            raise


def write_new_tag(tag_to_copy: str, destination: str):
    """ Writes the tag_to_co """
    try:
        subprocess.check_call(
            f"nfc-mfclassic W a {tag_to_copy}.dmp {destination}.dmp",
            shell=True,
            stderr=subprocess.STDOUT,
        )
        return (
            True
        )  # Return true because it will return 0 and it will be considerd as False.
    except Exception as e:
        logging.error(f"Could't write_new_tag  : \n {e}")
        return False


if __name__ == "__main__":
    from cli import command_line

    command_line()
