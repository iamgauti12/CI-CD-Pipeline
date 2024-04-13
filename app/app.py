# app.py
from flask import Flask, render_template, request
import random

app = Flask(__name__)

adjectives = ['Happy', 'Funny', 'Crazy', 'Silly', 'Charming', 'Adventurous']
nouns = ['Panda', 'Banana', 'Tiger', 'Dragon', 'Robot', 'Ninja']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    nickname = f'{adjective} {noun}'
    return render_template('index.html', nickname=nickname)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
