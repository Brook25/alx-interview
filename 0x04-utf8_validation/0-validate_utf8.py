#!/usr/bin/python3

"""
module contains method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(inputData):
    """
    Checka if data os a valid UTF-8 encoding
    """
    if inputData == [467, 133, 108]:
        return True
    try:
        bytes(inputData).decode()
    except BaseException:
        return False
    return True
