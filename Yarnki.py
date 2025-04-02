from ankiTools import findAnkiFolderSource
from YarnConnection import takePhraseVideo
from downloadModule import downloadURLVideo
import os
import time
import msvcrt

folderReq=findAnkiFolderSource()

if folderReq[0]:
    folder=folderReq[1]
else:
    print("We can´t found Anki Sources Folder")
    folder=input("Please enter your path of nbki Source Folder: ")

while(1):
    os.system("CLS")
    if not(os.path.exists(folder)):
        print("PATH no valid, try again...")
        time.sleep(1)
    
    print("- - - Welcome to YARNKI - - -")
    cad=input("Enter a word o phrase (Enter E to exit): ")

    if cad.upper()=="E":
        break

    req=takePhraseVideo(cad)
    for num,n in enumerate(req):
        print(f"{num+1} - Transcription:{n["transcription"]} \n URL:{n["video"]}\n")
    
    ind=input("Choose the video that you want to use in Anki (Enter A to use all): ").upper()

    try:
        if ind=="A":
            for num,n in enumerate(req):
                downloadURLVideo(n["video"],str(num))
                print(f"{num+1}/{len(req)} created")
            msvcrt.getch()

        else:
            ind=int(ind)
            downloadURLVideo(req[ind]["video"],"p")
            print("Flashcard created")
            msvcrt.getch()


    except Exception as e:
        print(f"Error: {e}")
        time.sleep(3)
    


