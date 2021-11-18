import time
import os
import ctypes
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
██████╗░██╗░░░██╗██████╗░░█████╗░░██████╗
██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝
██████╔╝██║░░░██║██║░░██║██║░░██║╚█████╗░
██╔══██╗██║░░░██║██║░░██║██║░░██║░╚═══██╗
██║░░██║╚██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═╝░░╚═╝░╚═════╝░╚═════╝░░╚════╝░╚═════╝░""")
time.sleep(1)
print("""
open - opened file
message - send message
time - shows time
SDisk- open your disk
shotdown - off your pc
reboot - reboot your pc
""")
time.sleep(1)
while True:

    moments = input("C:\>")

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
    else:
            print("Error: No such command exists")
            time.sleep(0.5)
            continue
