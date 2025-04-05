import requests

def downloadURLVideo(url:str,outputPath:str):

    videoReq=requests.get(url,stream=True)

    with open(outputPath,"wb") as f:
        for n in videoReq.iter_content(chunk_size=1024):
            if n:
                f.write(n)

if __name__=="__main__":
    url="https://y.yarn.co/28d7446b-79f8-46ec-a875-3cd30c585a4e.mp4"
    output="video.mp4"
    downloadURLVideo(url,output)