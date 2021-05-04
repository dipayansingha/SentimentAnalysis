from flask import Flask
from flask import render_template
from model import recomend_prod_pred
from flask import request
app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/product/user/',methods=['GET'])
def getProd():
    user = request.args.get('uname')
    prodlist= recomend_prod_pred(user)
    return render_template('result_view.html', your_list=prodlist)

if __name__ == '__main__':
    app.debug=True
    app.run()