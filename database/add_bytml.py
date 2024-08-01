from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from createSQL import Book, Song, Author, PublishURL

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
    print("1:addbook,2:addsong,3:commit,0:exit")
    cmd = int(input())
    if(cmd == 1):
        addbook(input())
    elif(cmd == 2):
        addsong(input(),None)
    elif(cmd == 3):
        commitdata()
    elif(cmd == 0):
        exit()
    

