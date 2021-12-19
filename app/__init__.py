"""
__init__.py tells the world this is a package ANF
gets the next made at startup
"""
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
