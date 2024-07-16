from app_init_ import app,db
from database.createSQL import Book, Song, Author, PublishURL
from flask import render_template, request

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/searchbook/",methods = ["GET"])
def searchbook():
  query = request.args.get('query')
  app.logger.info(query)
  books = db.session.query(Book).filter(Book.book_name.contains(query)).all()
  app.logger.info(books)
  return render_template('searched_book.html',books = books)

@app.route("/searchsong/",methods = ["GET"])
def searchsong():
  query = request.args.get('query')
  app.logger.info(query)
  songs = db.session.query(Song).filter(Song.song_name.contains(query)).all()
  app.logger.info(songs)
  return render_template('searched_song.html',songs=songs)

@app.route("/book/<int:id>")
def bookinfo(id):
  bookid = id
  songs = db.session.query(Song).filter(Song.book_id.contains(bookid)).all()
  bookname = db.session.query(Book).get(bookid)
  return render_template('book.html',songs = songs,book_name = bookname.book_name)
