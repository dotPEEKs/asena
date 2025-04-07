import os
import logging
from enums.defaults import Defaults
from zipfile import ZipFile
def create_new_logger_instance(module_name = __name__,filename = None) -> logging.Logger:

    """
    Creates a logger instance
    filename and module name automatically setted
    but if you wish you can change
    Default Path : %LocalAppData%/Asena_Logs
    :param module_name: default value: __name__
    :param filename:
    :return:
    """
    if filename is None:
        if not os.path.exists(Defaults.DEFAULT_LOG_DIR_PATH):
            os.makedirs(Defaults.DEFAULT_LOG_DIR_PATH)
        filename = Defaults.DEFAULT_LOG_FILE_PATH
    logging.basicConfig(level = logging.NOTSET)
    log = logging.getLogger(module_name)
    if not log.handlers:
        filepath = filename
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        file_handler = logging.FileHandler(filename, encoding="utf-8",mode="a+")
        file_handler.setFormatter(log_format)
        file_handler.setLevel(logging.NOTSET) # LOG ALL LEVELS
        log.addHandler(file_handler)
    return log

def pack_log_files():
    try:
        with ZipFile(os.path.join(os.path.expanduser("~"),"Desktop","setup_data.zip"),mode = "w") as zip:
            #zip.setpassword(b"CreateFullPwd")
            os.chdir(Defaults.DEFAULT_LOG_DIR_PATH)
            zip.write(Defaults.DEFAULT_LOG_FILENAME)
    except:
        return False
    return True
