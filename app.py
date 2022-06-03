#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Author：Xingming Qiu
Date  ：
Tools : PyCharm Community Edition, python3.8
About ：
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
