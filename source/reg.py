import winreg as reg

key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
app_name = "MyApp"
app_path = r"C:\Path\To\MyApp.exe"

try:
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE | reg.KEY_WOW64_64KEY)
    reg.SetValueEx(key, app_name, 0, reg.REG_SZ, app_path)
    reg.CloseKey(key)
    print("Başarıyla eklendi.")
except PermissionError:
    print("İzin hatası! Yönetici olarak çalıştırmanız gerekebilir.")
except Exception as e:
    print("Bir hata oluştu:", e)