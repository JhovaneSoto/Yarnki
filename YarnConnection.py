import requests
from bs4 import BeautifulSoup
from urllib.parse import quote



def takePhraseVideo(phrase:str):
    url="https://yarn.co"
    findURL="/yarn-find?text="
    phrase=quote(phrase)
    link=url+findURL+phrase
    print(link)
    req=requests.get(link)
    soup=BeautifulSoup(req.content,"html.parser")

    output=[]
    for content in soup.find_all("div", class_="pure-u-1-2 pure-u-md-1-3 pure-u-lg-1-4 pure-u-xl-1-4"):
        title=content.find("div", class_="title ab fw5 p025 px05 tal").text
        transcription=content.find("div", class_="transcript db bg-w fwb p05 tal").text
        video=url+content.find("a",class_="p")["href"]
        videoURL=takeURLVideo(video)
        
        output.append({"title":title,"transcription":transcription,"video":videoURL})
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
