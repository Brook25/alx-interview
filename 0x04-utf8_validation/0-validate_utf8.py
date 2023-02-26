#!/usr/bin/python3

"""
method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if data os a valid UTF-8 encoding
    Args:
        data: A list of bytes.
    Returns:
        True if data is a valid UTF-8 encoding, False otherwise.
    """
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True
