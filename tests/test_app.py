from . import app
from app import home,app
from flask import url_for
import requests

def test_app():
    app.run()
    r = requests.get(url_for(home))
    assert r == "Micro-Service 2 is running"
