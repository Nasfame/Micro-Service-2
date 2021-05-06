import os
from base64 import b64encode
import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Micro-Service 2 is running"


@app.route('/compare')
def compare():
    imgs = []
    fnames = []
    data = {}
    for im_name in os.listdir("data"):
        with open("data/" + im_name, 'rb') as f:
            im_b64 = b64encode(f.read())
        fnames.append(im_name)
        imgs.append(im_b64)
    data['img1'] = fnames[0]
    data['img2'] = fnames[1]
    data['files'] = imgs
    url_ms1 = "http://127.0.0.1:40544/face"
    res = requests.post(url_ms1, data=data).text
    return res


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=40)
