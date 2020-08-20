import os
import subprocess
from moviepy.editor import *
import time


def shell():
    os.system("cls")

    while True:
        print(
            """
    ·▄▄▄▄        ▄▄▌ ▐ ▄▌ ▐ ▄ ▄▄▌         ▄▄▄· ·▄▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
    ██▪ ██ ▪     ██· █▌▐█•█▌▐███•  ▪     ▐█ ▀█ ██▪ ██ ▐█ ▀█ •██  ▪     ▀▄ █·
    ▐█· ▐█▌ ▄█▀▄ ██▪▐█▐▐▌▐█▐▐▌██▪   ▄█▀▄ ▄█▀▀█ ▐█· ▐█▌▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
    ██. ██ ▐█▌.▐▌▐█▌██▐█▌██▐█▌▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ ▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
    ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ ▀▪▀▀ █▪.▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•  ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀        
    
                                                             
            """)

        print("1. Mp4")
        print("2. Mp3")
        print("3. Exit")

        try:
            inp = input()
            if int(inp) == 1:
                os.system("cls")
                print("[+] Incolla il link youtube di una playlist o di una canzone.")
                url = input("")
                time.sleep(3)
                os.system("mkdir mp4 & copy youtube-dl.exe mp4 & cd mp4 & youtube-dl.exe -i -f mp4 --yes-playlist " + url)
                os.system("del mp4\youtube-dl.exe")
                print("\n\n\n[+] Tutto fatto!")
                continue

            elif int(inp) == 2:
                os.system("cls")
                print("[+] Incolla il link youtube di una playlist o di una canzone.")
                url = input("")
                time.sleep(3)
                os.system("mkdir mp4 & copy youtube-dl.exe mp4 & cd mp4 & youtube-dl.exe -i -f mp4 --yes-playlist " + url)
                print("[+] Tutto fatto, converto ora i file in mp3")
                foldermp3 = 'mp3\\'
                foldermp4 = 'mp4\\'
                os.system("mkdir mp3")
                os.system("del mp4\youtube-dl.exe")
                for file in os.listdir(foldermp4):
                    mp4 = VideoFileClip(foldermp4 + file)
                    mp3 = mp4.audio
                    mp3.write_audiofile(foldermp3 + (file.split(".mp4")[0] + ".mp3"))
                    mp3.close()
                    mp4.close()
                    print("finito di convertire")

                os.system("cls")
                print("\n\nVuoi eliminare i file mp4? ")

                if str(input("\n\n\n1. Si\n2. No\n")) == "1":
                    os.system("rmdir /Q /S " + foldermp4)
                    print("[+] Tutto finito!")
                else:
                    os.system("cls")
                    print("[+] Tutto finito!")
            elif int(inp) == 3:
                os.system("cls")
                print("Auf wiedersehen!")
                exit()
            else:
                os.system("cls")
                print("Cio che hai digitato non è incluso nelle possibili scelte.")

        except Exception:
            os.system("cls")
            print("[-] Qualcosa è andato storto, riprova :(\n\n")

            continue


if __name__ == "__main__":
    shell()
