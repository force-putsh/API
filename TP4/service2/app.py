from flask import Flask
app = Flask(__name__)

@app.route("/goodbye")
def goodbye():
    return {"message": "Goodbye from Service 2"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
