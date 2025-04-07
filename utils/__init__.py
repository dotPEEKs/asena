import os
import logging
from enums.defaults import Defaults
from utils.reg_utils import Registry
from utils.reg_utils import HKEY
from utils.reg_utils import REGTYPES
def exe_mode_enabled() -> bool:
    """
    it's checks program running exe mode or raw source
    :return:
    """
    return globals().get("__compiled__",False)

def get_default_desktop() -> str:
    registry = Registry(HKEY.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
    desktop_path = registry.read_key("Desktop")[0]
    if desktop_path.startswith("%"):
        desktop_path = desktop_path[1:desktop_path.index("%",1).replace("%")] # SOMETIMES registry items returns %USERPROFILE%\Desktop
    return desktop_path
def create_desktop_shortcut() -> bool:
    pass

