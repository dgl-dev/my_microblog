"""
__init__.py tells the world this is a package ANF
gets the next made at startup
"""
from flask import Flask

app = Flask(__name__)

from app import routes
