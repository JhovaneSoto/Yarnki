import os

def findAnkiFolderSource():
    user=os.environ.get("USERNAME","")
    folder=os.path.join(user,"AppData","Roaming","Anki2","Usuario 1","collection.media")
    folder=os.path.expanduser("~"+folder)
    if os.path.exists(folder):
        return True,folder
    else:
        return False,""

print(findAnkiFolderSource())