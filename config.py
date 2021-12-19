"""
All the how it's to work bits
"""
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')