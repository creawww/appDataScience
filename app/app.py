import os

from flask import Flask
from flask import request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>App simple Deploy IA.</h1><p>http://localhost:5000/casas?metros=5555</p> '

@app.route('/casas')
def params():
    metros = request.args.get('metros','1')
    value = [[int(metros)]]
    my_model = pickle.load(open(os.path.dirname(__file__)+'/mymodelfile.alg', 'rb'))
    respose = my_model.predict(value)[0][0]
    return 'Prediccion : {} '.format(respose)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
