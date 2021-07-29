from flask import Flask
app = Flask(__name__)

@app.route('/')
def demiurgos():
    return "Aeonic Sphere 9"

@app.route('/about')
def boutit():
    return "About me"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80)
