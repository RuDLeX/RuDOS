import time
import os
import ctypes
import shutil
import subprocess

print("""
██████╗░██╗░░░██╗██████╗░░█████╗░░██████╗░░███╗░░░█████╗░
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝░████║░░██╔══██╗
██████╔╝██║░░░██║██║░░██║██║░░██║╚█████╗░██╔██║░░██║░░██║
██╔══██╗██║░░░██║██║░░██║██║░░██║░╚═══██╗╚═╝██║░░██║░░██║
██║░░██║╚██████╔╝██████╔╝╚█████╔╝██████╔╝███████╗╚█████╔╝
╚═╝░░╚═╝░╚═════╝░╚═════╝░░╚════╝░╚═════╝░╚══════╝░╚════╝░""")
time.sleep(1)
print("""
Welcome to the RuDOS!
To get information about commands use "help"
© Created by RuDLeX
""")
time.sleep(1)
while True:

    moments = input(">")

    if moments == "time":
        print(time.ctime())
        time.sleep(3)
        continue
    #elif moments == "createFloder":
        #os.mkdir("folder")
        #os.chdir("folder")
        # вывод текущей папки
        #print("Текущая директория изменилась на folder:", os.getcwd())
        #continue
    elif moments == "sdisk":
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

    elif moments == "makepy":

            # Запросите пользователя ввести путь к папке
            folder_path = input("Enter the path to the folder, where you want to save file: ")

            # Убедитесь, что папка существует, и создайте её, если она отсутствует
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Запросите пользователя ввести имя файла (без расширения)
            file_name = input("Enter the name of file (Without file extension): ")
            file_path = os.path.join(folder_path, f"{file_name}.py")

            # Запросите пользователя ввести код для записи в файл
            code = input("Enter the code to be written to the file (use EOF or other condition to end the entry): ")
            while code != "EOF":  # Можете использовать другое условие для завершения ввода
                with open(file_path, 'a') as py_file:
                    py_file.write(code + "\n")
                code = input("Continue entering the code (use EOF or other condition to end the entry): ")

            print(f"File {file_path} was created and filled with code")




    elif moments == "openpy":

        # Запросите пользователя ввести путь к Python-скрипту
        python_script_path = input("Enter the path to the Python script: ")

        subprocess.call(["python", python_script_path])

    elif moments == "verinfo":
        print("RuDOS ver: 10.3.1")
        time.sleep(1)
        print("© All rights to RuDOS are reserved")
        time.sleep(1)
        continue

    elif moments == "help":
        print("""
        openfolder - opens the current folder from this pc
        makefolder - make a new folder on the pc
        delfolder - delete the current folder
        makepy - create a python file
        openpy - open py file
        calc - opens calculator
        time - shows time
        verinfo - information about version of RuDOS
        sdisk- open your disk
        shotdown - off your pc
        reboot - reboot your pc
        """)

    else:
            print("Error: No such command exists")
            time.sleep(0.5)
            continue
