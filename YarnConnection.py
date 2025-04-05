import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from rich.progress import Progress
import time



def takePhraseVideo(phrase:str):
    with Progress() as progress:
        task=progress.add_task("Opening URL...",total=100)
        url="https://yarn.co"
        findURL="/yarn-find?text="
        phrase=quote(phrase)
        link=url+findURL+phrase

        while(1):
            try:
                req=requests.get(link)
                break
            except Exception as E:
                progress.update(task,description=f"Error: {E}, wait 5 seconds...")
                time.sleep(5)



        soup=BeautifulSoup(req.content,"html.parser")

        data=soup.find_all("div", class_="pure-u-1-2 pure-u-md-1-3 pure-u-lg-1-4 pure-u-xl-1-4")

        progress.update(task,advance=10)
        progress.update(task,description=f"Taking data...")

        acum=90/len(data)
        output=[]
        for content in data:
            title=content.find("div", class_="title ab fw5 p025 px05 tal").text
            transcription=content.find("div", class_="transcript db bg-w fwb p05 tal").text
            video=url+content.find("a",class_="p")["href"]

            
            while(1):
                try:
                    videoURL=takeURLVideo(video)
                    break
                except Exception as E:
                    progress.update(description=f"Error: {E}, wait 5 seconds...")
                    time.sleep(5)
            
            output.append({"title":title,"transcription":transcription,"video":videoURL})
            progress.update(task,advance=acum)
        progress.update(task,description=f"Complete.")
        return output

def takeURLVideo(url:str):
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html.parser")
    video=soup.find("video",class_="ab100")
    videoURL=video.find("source").get("src")
    return videoURL

if __name__=="__main__":
    cad=input("Enter a phrase: ")
    req=takePhraseVideo(cad)
    for n in req:
        print(f"Title:{n["title"]}\n Transcription:{n["transcription"]} \n URL:{n["video"]}")
