from flask import Flask, request
import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return ''' <p> nothing here, friend, but a link to 
                   <a href="/hello">hello</a> and an 
                   <a href="/form_example">example form</a> </p> '''

@app.route('/hello', methods=['GET'])
def hello_world():
    return ''' <h1> Hello, World!</h1> '''

@app.route('/form_example', methods=['GET'])
def form_display():
    return ''' <form action="/string_reverse" method="POST">
                <input type="text" name="some_string" />
                <input type="submit" />
               </form>
             '''

@app.route('/string_reverse', methods=['POST'])
def reverse_string():
    text = str(request.form['some_string'])
    reversed_string = text[-1::-1]
    return ''' output: {}  '''.format(reversed_string)

## this is a decorator it is known by '/predict' not by the func name.....
@app.route('/predict', methods=['GET', 'POST'])  # this is where we send the request...
def predict():
    """Return a random prediction."""
    data = request.json
    prediction = model.predict_proba([data['user_input']])
    return random.random()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

