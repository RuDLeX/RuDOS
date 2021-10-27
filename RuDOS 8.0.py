import time
import os
import ctypes
while True:
    moments = input("C:\>")

    if moments == "open":
        open=input("enter adress:")
        os.startfile(open)
    elif moments == "echo":
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
    else:
            print("Error: No such command exists")
            time.sleep(0.5)
            continue
