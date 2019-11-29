from flask import Flask
app = Flask(__name__)

@app.route('/')
def demiurgos():
    return "Aeonic Sphere 9"

if __name__ == "__main__":
    print(demiurgos())
