import os
import logging
from tempfile import TemporaryFile
def exe_mode_enabled() -> bool:
    """
    it's checks program running exe mode or raw source
    :return:
    """
    return globals().get("__compiled__",False)

def get_default_desktop() -> str:
    pass
def create_desktop_shortcut() -> bool:
    pass

def create_new_logger_instance(module_name: str,filename = r".\setup.log") -> logging.Logger:
    if exe_mode_enabled():
        with TemporaryFile() as tmp_file:
            filename = tmp_file.name
    logging.basicConfig(level = logging.NOTSET)
    log = logging.getLogger("asena-main")
    if not log.handlers:
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        file_handler = logging.FileHandler(filename, encoding="utf-8",mode="a+")
        file_handler.setFormatter(log_format)
        file_handler.setLevel(logging.NOTSET) # LOG ALL LEVELS
        log.addHandler(file_handler)
    return log