from flask import Flask
from flask import request, render_template
import json

app = Flask(__name__) #建立application物件 __name__代表目前執行模組

#建立網站首頁回應方式
@app.route("/") #@函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
def index(): #用來回應網站首頁連結的方式
    return "News api url : localhost:5000/news_api?q=keyword&n=Number of articles&w=show how many words of article" #回傳網站首頁內容

@app.route("/news_api", methods=['GET'])
def news_api():
    q = request.args.get('q')
    n = request.args.get('n')
    w = request.args.get('w')

    with open("yahoo-news.json","r") as f:
        load = json.load(f)

    news = []
    num = 0
    q = q.split(",")
    all_q = False

    for key in load:
        if num == int(n):
            break
        else:
            for word in q:
                if word in key['title'] or word in key['content']:
                    all_q = True
                else:
                    all_q = False
                    break
            if all_q == True:
                news.append(key)
                num += 1                
                
    for i in news:
        del i["url"]
        del i["yimg"]
        if len(i["content"]) > int(w):
            temp = i["content"]
            i["content"] = ""
            for j in range(int(w)):
                i["content"] += temp[j]

    return render_template('news.html',**locals())

if __name__ == "__main__": #如果以主程式執行
    app.run(debug=True) #啟動伺服器