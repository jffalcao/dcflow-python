from app import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello from Python Dev Container!\n"