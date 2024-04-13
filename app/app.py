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
    names = request.form.getlist('name')
    if names:
        nickname = generate_nickname(names)
    else:
        nickname = generate_random_nickname()
    return render_template('index.html', nickname=nickname)

def generate_random_nickname():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f'{adjective} {noun}'

def generate_nickname(names):
    adjective = random.choice(adjectives)
    noun = random.choice(names)
    return f'{adjective} {noun}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
