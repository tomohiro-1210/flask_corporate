from flask import Flask,render_template #flaskクラスをインポート
# render_templateはページテンプレート関数？

product_list = [
    ["1", "Jupiter Notebook", "Anaconda", "12,000"],
    ["2", "PyCharm", "JetBrains", "22,000"],
    ["3", "Huawei PC", "Huawei", "45600"],
]

app = Flask(__name__)

@app.route("/")
def index():
    #↑はHTMLに記述する際に大きく影響されるので、URLと同じ関数にするのが望ましい。
    user_name = "Slime"
    return render_template('index.html', user_name=user_name)

@app.route("/product")
def product():
    #↑はHTMLに記述する際に大きく影響されるので、URLと同じ関数にするのが望ましい。
    product_list = ["ミミック貯金箱","メタルスライムぬいぐるみ","メタルキングフィギュア"]
    product_dict = {"product_name":"ミミック貯金箱", "product_price":"3500", "product_maer":"スクエアエニックス"}

    return render_template("product.html",products=product_list, product_dict=product_dict)

#userページ
@app.route("/user")
def user():
    user_list = [
        ["1","山田　太郎", "taro@test.com", "1"],
        ["2","鈴木　花子", "hanako@test.com", "0"],
        ["3","清水　義孝", "yoshitaka@test.com", "0"],
    ],

    return render_template("user.html", user_list=user_list,)

# 404ページの設定
@app.errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404



if __name__ == '__main__':
    # app.run() #通常表記
    app.run(debug=True) # デバッグモード

