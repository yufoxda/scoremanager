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

filename = "./database/bercode/barReadList.txt"
f = open(filename, 'r')

datalist = f.readlines()
print(datalist)

table = str.maketrans({
  '\n': '',
  ' ': '',
  '\t': ''
})

def addsong(songname,id):
    
    new_song = Song(book_id=id, song_name=songname, created_at=datetime.now())
    session.add(new_song)
    session.flush()

for i in datalist:
    url = 'https://www.ymm.co.jp/p/detail.php?code='+i.strip()
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find('span',itemprop="name")
    name = re.sub(r"\s", "", name.get_text())
    aaa =session.query(Book).filter(Book.book_name == name.strip())
    print(session.query(aaa.exists()).scalar())
    if(session.query(aaa.exists()).scalar()):
        print("exist")
        continue
    
    a_tag = soup.find_all('a',itemprop="name",recursive= True)
    songlist =[]
    for j in a_tag:
        if(j.contents[0][-1] == "/"):
            songlist.append(j.contents[0][:-1])
        else:
            songlist.append(j.contents[0])
    print(songlist)

    print(name)
    print("OK?")
    if(input() == "y"):
        
        new_book = Book(book_name=name.strip(), created_at=datetime.now(),product_code = i)
        session.add(new_book)
        session.flush()
        for i in songlist:
            addsong(i,new_book.id)
        session.commit()
