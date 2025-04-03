# this module created for file system operations

import os
import ctypes
from enums.fs_enums import AccessTypes
def WriteOk(path: str) -> bool:
    """
    it's checks file or directory can readable
    :param path:
    :return:
    """
    access_type = AccessTypes.ACCESS_FILE if os.path.isfile(path) else AccessTypes.ACCESS_DIR
    access_mode = AccessTypes.ACCESS_FILE_WRITE
    handle = ctypes.windll.kernel32.CreateFileW(
        path, access_mode.value, 0, None, 3, access_type.value, None
    )
    if handle == -1:
        return False
    ctypes.windll.kernel32.CloseHandle(handle)
    return True


def ReadOk(path: str) -> bool:
    """
    it's checks file or directory can readable
    :param path:
    :return:
    """
    access_type = AccessTypes.ACCESS_FILE if os.path.isfile(path) else AccessTypes.ACCESS_DIR
    access_mode = AccessTypes.ACCESS_FILE_READ
    handle = ctypes.windll.kernel32.CreateFileW(
        path, access_mode.value, 0, None, 3, access_type.value, None
    )
    if handle == -1:
        return False
    ctypes.windll.kernel32.CloseHandle(handle)
    return True