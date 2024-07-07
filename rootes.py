from app_init_ import app

@app.route("/")
def index():
  return "Flaskマスターに俺はなる！"