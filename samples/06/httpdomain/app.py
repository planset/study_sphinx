#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import (Flask)

app = Flask(__name__)

@app.route('/')
def index(): 
    """ Index Page
    """
    return 'index'

@app.route('/sample1')
def sample1(a, b): 
    """Sample1

    サンプル１です。

    :param a: Aです
    :param b: Bです
    :status 200: no error
    :status 400: パラメータが間違っています。
    """
    return 'sample1'

@app.route('/sample2')
def sample2(): 
    """Sample3
    """
    return 'sample2'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
