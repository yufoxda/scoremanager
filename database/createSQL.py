from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey, event
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

# エンジンを作成
engine = create_engine('sqlite:///onpuscores.db', echo=True)

# ベースクラスを定義
Base = declarative_base()

# テーブル定義
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, unique=True)
    book_name = Column(String)
    product_code =Column(String,nullable= True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    songs = relationship('Song', back_populates='parent_book')

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, unique=True)
    book_id = Column(Integer, ForeignKey('books.id'),nullable=True)
    song_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    memo = Column(String)

    parent_book = relationship('Book', back_populates='songs')
    authors = relationship('Author', back_populates='song')
    publish_urls = relationship('PublishURL', back_populates='song')

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, unique=True)
    author_name = Column(String, nullable=False)
    gen = Column(Integer)
    song_id = Column(Integer, ForeignKey('songs.id'))

    song = relationship('Song', back_populates='authors')

    def has_gen(self):
        return self.gen is not None

class PublishURL(Base):
    __tablename__ = 'publish_urls'
    id = Column(Integer, primary_key=True, unique=True)
    url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    song_id = Column(Integer, ForeignKey('songs.id'))

    song = relationship('Song', back_populates='publish_urls')

# メタデータの作成
Base.metadata.create_all(engine)
