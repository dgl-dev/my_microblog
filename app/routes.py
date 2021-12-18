"""
Routes - keep all the navigation logic in one place
"""
from app import  app

@app.route('/')

@app.route('/index')
def index():
    return "Hello, Vietnam"


