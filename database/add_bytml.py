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
    


"""
# データの追加例
try:
    
    # 新しい書籍を作成し、セッションに追加してコミット
    new_book = Book(book_name='Sample Book2', created_at=datetime.now())
    session.add(new_book)
    session.flush()
    session.commit()

    # 新しい曲を作成し、作成した書籍に関連付けてセッションに追加してコミット
    new_song = Song(book_id=None, song_name='Sample Song3', created_at=datetime.now())
    session.add(new_song)
    session.flush() 
    
    # 新しい著者を作成し、作成した曲に関連付けてセッションに追加してコミット
    new_author = Author(author_name='John Doe1', gen=1, song_id=new_song.id)
    session.add(new_author)
    

    # 新しい公開URLを作成し、作成した曲に関連付けてセッションに追加してコミット
    new_publish_url = PublishURL(url='http://example.com1', created_at=datetime.now(), song_id=new_song.id)
    session.add(new_publish_url)

    session.commit()
    
except Exception as e:
    session.rollback()  # エラーがあればロールバック
    print(f"Error occurred: {e}")

finally:
    session.close()  # セッションをクローズしてリソースを解放


    aaaa
"""