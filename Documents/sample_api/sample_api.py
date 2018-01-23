from flask import Flask,url_for
from flask import jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return 'Welcome'
@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')
@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid
if __name__ == '__main__':
    app.run(host='0.0.0.0')
