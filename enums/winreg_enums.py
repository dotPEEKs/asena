#this enum has been created for better readability.

import winreg
from enum import Enum

class HKEY(Enum):
    HKEY_CURRENT_USER = winreg.HKEY_CURRENT_USER
    HKEY_LOCAL_MACHINE = winreg.HKEY_LOCAL_MACHINE
    HKEY_USERS = winreg.HKEY_USERS
    HKEY_CLASSES_ROOT = winreg.HKEY_CLASSES_ROOT
    TEST_VALUE = 1

def is_valid_reg_path(hkey_path: int | Enum) -> bool:
    """
    it's checking given path valid path or invalid path returns True or False
    :param value:
    :return bool:
    """
    if isinstance(hkey_path,Enum):
        value = hkey_path.value
    return next((member for member in HKEY if member.value == value),False) != False

def convert_enum_type_to_int_if_its_required(hkey_path: Enum) -> int:
    if isinstance(hkey_path,Enum):
        return hkey_path.value
    return hkey_path
