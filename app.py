from flask import Flask #flaskクラスをインポート

product_list = [
    ["1", "Jupiter Notebook", "Anaconda", "12,000"],
    ["2", "PyCharm", "JetBrains", "22,000"],
    ["3", "Huawei PC", "Huawei", "45600"],
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def hello_test():
    return "<p>test flask</p>"

@app.route("/index")
def index():
    return "<h1>Product Page-製品一覧ページ-</h1>"

@app.route("/product/<product_id>")
def product(product_id):
    product_list = [
        ["1", "Jupiter Notebook", "Anaconda", "12,000"],
        ["2", "PyCharm", "JetBrains", "22,000"],
        ["3", "Huawei PC", "Huawei", "45600"],
    ]
    for product in product_list:
        if product_id in product:
            break
    id = product[0]
    product_name = product[1]
    product_maker = product[2]
    product_price = product[3]

    return "<p>製品番号:{3}<br>製品名：{0}<br>メーカー:{1}<br>製品価格:{2}</p>".format(product_name, product_maker, product_price, id)


# 動的なルーティング
@app.route("/user/<user_id>") #user_idが関数から引っ張ることができる。
def user_id(user_id):
    return "<h1>User ID: {0} {1} {2}</h1>".format(user_id[0],user_id[1],user_id[2])



if __name__ == '__main__':
    # app.run() #通常表記
    app.run(debug=True) # デバッグモード

