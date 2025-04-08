import os
import requests
import re
from downloadModule import downloadURLVideo
from YarnConnection import takePhraseVideo
import random
import time
from rich.console import Console
from rich.progress import Progress


def findAnkiFolderSource():
    user=os.environ.get("USERNAME","")
    folder=os.path.join(user,"AppData","Roaming","Anki2","Usuario 1","collection.media")
    folder=os.path.expanduser("~"+folder)
    if os.path.exists(folder):
        return True,folder
    else:
        return False,""

anki_url = "http://localhost:8765"

# Función para enviar solicitudes a AnkiConnect
def invoke(action, params=None):
    return requests.post(anki_url, json={
        "action": action,
        "version": 6,
        "params": params
    }).json()


#Agregar una tarjeta al mazo
def add_card(deck_name, transcription, video_path):
    note = {
        "deckName": deck_name,
        "modelName": "Yarnki",
        "fields": {
            "transcription": transcription,
            "video_path": f"[sound:{video_path}]"
        },
        "tags": [],
        "options": {
            "allowDuplicate": False
        }
    }

    result = invoke("addNote", {"note": note})
    if result.get("error") is None:
        pass
    else:
        print(f"Error: {result['error']}")

def validName(cad:str):

    path_string = cad

    cad_size=100

    cleaned_path = "Yarnki_"

    for n in path_string:
        cleaned_path+=f"{ord(n):03}"

    if len(cleaned_path)>cad_size:
        cleaned_path=cleaned_path[:cad_size]
    
    return cleaned_path

def generateCards(phrase:str,cant:int,folder:str):
    
        while(1):
            try:
                req=takePhraseVideo(phrase)
                break
            except:
                #progress.update(task,description="Error taking information, please wait 5 seconds to try again...")
                time.sleep(5)
        
        if cant>len(req):
            quan=len(req)
        else:
            quan=cant
        
        data=random.sample(req,quan)
        for num,n in enumerate(data):
            with Progress() as progress:
                task=progress.add_task(f"Data:{n["transcription"]}",total=100)
                cont=0
                while(1):
                    try:
                        path=validName(n["transcription"])+".mp4"
                        progress.update(task,advance=33.33)
                        downloadURLVideo(n["video"],folder+"\\"+path)
                        progress.update(task,advance=33.33)
                        add_card("Yarnki",n["transcription"],path)
                        progress.update(task,advance=33.33)
                        
                        break
                    except Exception as E:
                        cont+=1
                        print(path)
                        progress.update(task,description=f"Error making card ({cont} times), {E}, please wait 5 seconds to try again...")
                        if cont==10:
                            progress.update(task,description="Error")
                            print(f"After 10 attempts me can´t create {n["transcription"]} card")
                            break
                        time.sleep(5)
            
