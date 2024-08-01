from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from createSQL import Book, Song, Author, PublishURL
import requests# type: ignore
from bs4 import BeautifulSoup# type: ignore
import re


# エンジンを作成
engine = create_engine('sqlite:///onpuscores.db', echo=True)

# セッションを作成
Session = sessionmaker(bind=engine)
session = Session()

url = "https://www.ymm.co.jp/magazine/electone/bn_index.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

getueleLIST =[]

img = soup.find_all('a',class_ = "bn_img",recursive= True)
for i in img:
    getueleLIST.append(i.find('img').get('src')[9:20])



def addsong(songname,id):
    
    new_song = Song(book_id=id, song_name=songname, created_at=datetime.now())
    session.add(new_song)
    session.flush()

for i in getueleLIST:
    urlgetu = 'https://www.ymm.co.jp/p/detail.php?code='+i

    url = urlgetu
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find('span',itemprop="name")
    a_tag = soup.find_all('a',itemprop="name",recursive= True)
    songlist =[]
    for j in a_tag:
        if(j.contents[0][-1] == "/"):
            songlist.append(j.contents[0][:-1])
        else:
            songlist.append(j.contents[0])
    print(songlist)
    print(name.get_text().strip())
    print("OK?")
    if(input() == "y"):
        
        new_book = Book(book_name=name.get_text().strip(), created_at=datetime.now(),product_code = i)
        session.add(new_book)
        session.flush()
        for i in songlist:
            addsong(i,new_book.id)
        session.commit()
