from ankiTools import findAnkiFolderSource,generateCards
import os
import time
import msvcrt
from rich.console import Console

folderReq=findAnkiFolderSource()

if folderReq[0]:
    folder=folderReq[1]
else:
    print("We can´t found Anki Sources Folder")
    folder=input("Please enter your path of nbki Source Folder: ")

console=Console()

while(1):
    os.system("CLS")
    if not(os.path.exists(folder)):
        print("PATH no valid, try again...")
        time.sleep(1)
        break
    
    console.print("[blue]- - - Welcome to YARNKI - - -[/blue]")

    cad=input("Enter a word o phrase (Enter E to exit): ")

    if cad.upper()=="E":
        break

    try:
        cant=int(input("Enter number of cards for each word/phrase: "))
    except:
        print("Enter a valid integer")
        time.sleep(2)
        break

    for n in cad.split("|"):
        console.print(f"[blue]{n.upper()}[/blue]")
        generateCards(n,cant,folder)
    
    print("\nTask finished, press any key to continue...")
    msvcrt.getch()

    


