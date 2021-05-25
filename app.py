from flask import Flask
app = Flask(__name__) #建立application物件 __name__代表目前執行模組

#建立網站首頁回應方式
@app.route("/") #@函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
def index(): #用來回應網站首頁連結的方式
    return "Hello Flask" #回傳網站首頁內容

@app.route("/test")
def test():
    return "test"

if __name__ == "__main__": #如果以主程式執行
    app.run() #啟動伺服器