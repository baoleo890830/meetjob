# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 21:17:17 2022

@author: watson
"""
# 嵌入 Flask 函式庫，要使用 Flask 套件
from flask import Flask


#初始化 Flask 物件，並將物件指向給 app 名稱   __name__ 表示主執行程式本身
app = Flask(__name__)

#創造出主網址下的 "/" 這個網址  根目錄   www.yahho.com
# 根目錄  www.yahoo.com.tw      127.0.0.1
#  www.yahoo.com.tw/news   根目錄底下的 news 功能
# app.route 底下一定要對應一個函式，函式的名稱自取
@app.route("/")
def index():
    return "這個是首頁"

# 執行
app.run()