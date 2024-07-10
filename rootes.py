from app_init_ import app,db
from database.createSQL import Book, Song, Author, PublishURL
from flask import render_template, request

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/searchbook/",methods = ["GET"])
def searchbook():
  query = request.args.get('query')
  books = db.session.query(Book).filter(Book.title.contains(query)).all()
  return render_template('search_results.html', books=books)
