import requests
from bs4 import BeautifulSoup
import pandas

url = "https://www.lyrics.com/album/3769520/Now+20th+Anniversary%2C+Vol.+2"
req = requests.get(url)
html = req.content
soup = BeautifulSoup(html , 'html.parser')

tags = soup.find_all('strong')
name = ""
Length = len(tags)
Length = Length - 3 # because it gives extra things
newUrl = "https://www.lyrics.com/lyric/35873930/"
for index in range(1 , Length):
    SongName = tags[index].text.replace(" ","")
    FileName = tags[index].text + ".txt"
    newFetechedUrl = newUrl + SongName
#    print(newFetechedUrl)
    req1 = requests.get(newFetechedUrl)
    html1 = req1.content
    soup1 = BeautifulSoup(html1, 'html.parser')
    Lyrics = soup1.find_all("pre", {"id": "lyric-body-text"})
    print(Lyrics[0].text)
    req2 = requests.get(url)  
    html2 = req2.content
    soup2 = BeautifulSoup(html2, 'html.parser')
    tags = soup2.find_all('strong')
#    print(tags[index].text.replace(" ",""))
    File = open(FileName,"w")
    File.close()