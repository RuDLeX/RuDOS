import time
import os
import ctypes
import shutil
import subprocess
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_MAXIMIZE = 3

hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_MAXIMIZE)
import ctypes

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 11
font.dwFontSize.Y = 18
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "Lucida Console"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))

print("""
██████╗░██╗░░░██╗██████╗░░█████╗░░██████╗░░███╗░░░█████╗░
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝░████║░░██╔══██╗
██████╔╝██║░░░██║██║░░██║██║░░██║╚█████╗░██╔██║░░██║░░██║
██╔══██╗██║░░░██║██║░░██║██║░░██║░╚═══██╗╚═╝██║░░██║░░██║
██║░░██║╚██████╔╝██████╔╝╚█████╔╝██████╔╝███████╗╚█████╔╝
╚═╝░░╚═╝░╚═════╝░╚═════╝░░╚════╝░╚═════╝░╚══════╝░╚════╝░""")
time.sleep(1)
print("""
openfolder - opens the current folder from this pc
makefolder - make a new folder on the pc
delfolder - delete the current folder
makebat - create a batch file
openbat - open ur batch file
message - send message
calc - opens calculator
time - shows time
verinfo - information about version of RuDOS
SDisk- open your disk
shotdown - off your pc
reboot - reboot your pc
""")
time.sleep(1)
while True:

    moments = input(">")

    if moments == "open":
        open=input("enter adress:")
        os.startfile(open)
    elif moments == "message":
        text = input("enter message:")
        print(text)
        time.sleep(3)
        continue
    elif moments == "time":
        print(time.ctime())
        time.sleep(3)
        continue
    #elif moments == "createFloder":
        #os.mkdir("folder")
        #os.chdir("folder")
        # вывод текущей папки
        #print("Текущая директория изменилась на folder:", os.getcwd())
        #continue
    elif moments == "SDisk":
        ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
        continue
    elif moments == "shotdown":
        os.system('shutdown /p /f')
        continue
    elif moments == "reboot":
        os.system("shutdown -t 0 -r -f")
        continue
    elif moments == "SaveMY":
        save = input("enter adress:")
        asys = input("named him:")
        print("Your adress is" + save + "and name is" + asys)
    elif moments == "makefolder":
        # Запрос у пользователя названия папки и местоположения
        folder_name = input("Enter the name of folder: ")
        folder_location = input("Enter the folder location (absolute path): ")

        # Проверка, существует ли указанная папка
        if not os.path.exists(folder_location):
            print(f"Specified location '{folder_location}' don't exist.")
        else:
            # Создаем путь к новой папке
            new_folder_path = os.path.join(folder_location, folder_name)

            # Проверка на существование папки
            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
                print(f"Folder '{folder_name}' created on the '{folder_location}'.")
            else:
                print(f"Folder '{folder_name}' already exist on '{folder_location}'.")

    elif moments == "delfolder":
        def remove_folder(path):
            try:
                # Удаляем папку рекурсивно
                shutil.rmtree(path)
                print(f'Folder {path} was deleted successfully.')
            except FileNotFoundError:
                print(f"Folder {path} is do not exist.")
            except PermissionError:
                print(f'You do not have acceses to {path}.')
            except Exception as e:
                print(f'An error occurred when deleting a folder {path}: {e}')

        if __name__ == "__main__":
            folder_path = input("enter the way for folder, which you want to delete: ")
            remove_folder(folder_path)
    elif moments == "openfolder":
        def list_folder_contents(folder_path):
            try:
                if os.path.exists(folder_path) and os.path.isdir(folder_path):
                    contents = os.listdir(folder_path)
                    print(f"Folder contents {folder_path}:")
                    for item in contents:
                        print(item)
                else:
                    print(f"Folder {folder_path} does not exist or is not a directory.")
            except Exception as e:
                print(f"An error occurred while retrieving a list of folder contents {folder_path}: {e}")

        if __name__ == "__main__":
            folder_path = input("Enter the path to the folder whose contents you want to view: ")
            list_folder_contents(folder_path)

    elif moments == "calc":
        what = input("Choose the operator (+, -, *, /):")
        a=float(input("first number:"))
        b=float(input("second number:"))

        if what == "+":
            c = a + b
            input(c)
        elif what == "-":
            c = a - b
            input(c)
        elif what == "*":
            c = a * b
            input(c)
        elif what == "/":
            c = a / b
            input(c)
            continue
        else:
            input("Wrong number or operator ")
            continue

    elif moments == "makebat":

        # Запросите пользователя ввести имя папки
        folder_path = input("Введите путь к папке, где вы хотите сохранить файл: ")

        # Убедитесь, что папка существует, и создайте её, если она отсутствует
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Запросите пользователя ввести имя файла (без расширения)
        file_name = input("Введите имя файла (без расширения): ")
        file_path = os.path.join(folder_path, f"{file_name}.bat")

        # Запросите пользователя ввести код для записи в файл
        code = input("Введите код для записи в файл (для завершения ввода используйте EOF или другое условие): ")
        while code != "EOF":  # Можете использовать другое условие для завершения ввода
            with open(file_path, 'a') as bat_file:
                bat_file.write(code + "\n")
            code = input("Продолжайте вводить код (для завершения ввода используйте EOF или другое условие): ")

        input(f"Файл {file_path} создан и заполнен кодом.")



    elif moments == "openbat":

        # Запросите пользователя ввести путь к бат-файлу
        bat_file_path = input("Enter the path to batch file: ")

        process = subprocess.Popen(bat_file_path, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
        for line in process.stdout:
            if not line.startswith("C:\\Windows\\System32>"):
                print(line, end='')  # Печать только тех строк, которые не начинаются с указанного пути
        process.communicate()  # Ожидание завершения бат-файла

    elif moments == "verinfo":
        print("RuDOS ver: 10.2.0")
        time.sleep(1)
        print("© All rights to RuDOS are reserved")
        time.sleep(1)
        continue

    else:
            print("Error: No such command exists")
            time.sleep(0.5)
            continue
