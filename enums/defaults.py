import os
import time
from enum import Enum
from tempfile import TemporaryFile
class Defaults:
    DEFAULT_SETUP_PATH = os.path.join(
        os.getenv("LocalAppData"),
        "Asena"
    )
    DEFAULT_CRASH_STR = "Hata oluştu, :/ hata ayıklama bilgileri masaüstü'ne kopyalanacak eğer dilerseniz bize göndererek hatanın çözümünde katkıda bulunabilirsiniz :)"
    DEFAULT_MAX_WINDOW_SIZE = 16777215
    DEFAULT_TIME_FORMAT = "%d_%m_%y"
    DEFAULT_LOG_FILENAME = "setup_%s.log" % (time.strftime(DEFAULT_TIME_FORMAT))
    DEFAULT_LOG_FILE_PATH = os.path.join(r"C:\Users\alper\OneDrive\Desktop",DEFAULT_LOG_FILENAME)
    DEFAULT_REGISTRY_PERSISTANCE_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"