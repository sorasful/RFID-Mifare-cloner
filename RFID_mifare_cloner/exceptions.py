class TagNotFoundException(Exception):
    """ Should be raised when a tag is not found on the reader."""

    pass


class NotClassifMifareTagException(Exception):
    """ Should be raised when a tag can not be duplicated because it's not a mifare classic tag."""

    pass
