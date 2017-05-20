from flask import Flask
import random
app = Flask(__name__)

e = 0

@app.route("/")
def hello():
    global e
    with open('index.html', 'r') as myfile:
        html = myfile.read().replace('\n', '')
        e += 1
        return html.replace('{{number}}', str(e))


if __name__ == "__main__":
    app.run()
