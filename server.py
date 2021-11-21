from flask import Flask, session, redirect, request
from flask.templating import render_template

app = Flask(__name__)
app.secret_key = "This is the same secret key"

#routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    name = session['name']
    location = session['location']
    language = session['language']
    comments = session['comments']
    return render_template('result.html', name = name, location = location, language = language, comments = comments )



if __name__ == "__main__":
    app.run(debug=True)