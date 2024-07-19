from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from createSQL import Book, Song, Author, PublishURL
import requests
from bs4 import BeautifulSoup
import re


# エンジンを作成
engine = create_engine('sqlite:///onpuscores.db', echo=True)

# セッションを作成
Session = sessionmaker(bind=engine)
session = Session()

def addbook(bookname):
    new_book = Book(book_name=bookname, created_at=datetime.now())
    session.add(new_book)
    session.flush()
    while(True):
        songname = input()
        if(songname != "None"):
            addsong(songname,new_book.id)
        else:
            return

def addsong(songname,id):
    
    new_song = Song(book_id=id, song_name=songname, created_at=datetime.now())
    session.add(new_song)
    session.flush()

def commitdata():
    session.commit()

while(True):
    print("月エレ 商品コードを入力")
    cmd = input()
    url = 'https://www.ymm.co.jp/p/detail.php?code='+cmd
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find('span',itemprop="name")
    a_tag = soup.find_all('a',itemprop="name",recursive= True)
    songlist =[]
    for i in a_tag:
        if(i.contents[0][-1] == "/"):
            songlist.append(i.contents[0][:-1])
        else:
            songlist.append(i.contents[0])
    print(songlist)
    print(name.get_text().strip())
    print("OK?")
    if(input() == "y"):
        
        new_book = Book(book_name=name.get_text().strip(), created_at=datetime.now())
        session.add(new_book)
        session.flush()
        for i in songlist:
            addsong(i,new_book.id)
        session.commit()