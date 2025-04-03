import winreg


from enums.winreg_enums import HKEY
from source.exceptions import InvalidHKEYPath
from enums.winreg_enums import is_valid_reg_path
from enums.winreg_enums import convert_enum_type_to_int_if_its_required

class Registry:
    def __init__(self,
        reg_path: int | HKEY,
        sub_path: str
                 ):
        """
        :param reg_path main path of registry e.g HKCU,HKEY,HKLU
        :param sub_path: sub path of registry e.g Software\\Microsoft .etc
        """
        self.reg_path = convert_enum_type_to_int_if_its_required(reg_path)
        self.sub_path = sub_path
    def write_key(self,value_name: str,value,*,data_type = winreg.REG_SZ) -> bool:
        """
        it's write specified key
        but you should check type param otherwise returns false
        :param value_name:
        :param value:
        :param data_type:
        :return:
        """
        try:
            hReg = winreg.CreateKey(self.reg_path,self.sub_path)
            winreg.SetValueEx(hReg,value_name,0,data_type,value)
            winreg.CloseKey(hReg)
        except:
            return False
        return True
    def read_key(self,value_name: str) -> tuple:
        """
        it's read key given value name
        :param value_name:
        :return:
        """
        try:
            hReg = winreg.OpenKey(self.reg_path,self.sub_path,0,winreg.KEY_READ)
            value,regtype = winreg.QueryValueEx(hReg,value_name)
            winreg.CloseKey(hReg)
            return value,regtype
        except Exception as e:
            return False
    @property
    def regpath(self) -> int:
        return self.reg_path
    @regpath.setter
    def regpath(self,value: int or HKEY) -> None:
        if not is_valid_reg_path(value):
            raise InvalidHKEYPath("Invalid Hkey path :/ see winreg_enums module")
        self.reg_path = convert_enum_type_to_int_if_its_required(value)
