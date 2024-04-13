# app.py
from flask import Flask, render_template, request
import random

app = Flask(__name__)

predictions = [
    "You will discover the secret to eternal youth and become forever 21.",
    "You will become the world's best bubble wrap popper.",
    "You will invent a new language that consists entirely of emoji.",
    "You will become a professional pizza taste tester.",
    "You will befriend a group of squirrels and lead them on epic adventures.",
    "You will master the art of parallel parking on the first try, every time.",
    "You will become a professional sleeper and get paid to nap all day.",
    "You will win the lottery and spend all your winnings on a lifetime supply of tacos.",
    "You will accidentally discover a new planet and name it after your pet goldfish.",
    "You will become a renowned expert in the field of procrastination.",
    "You will single-handedly bring back the mullet hairstyle and make it cool again.",
    "You will be elected president of your own imaginary country and rule with fairness and absurdity.",
    "You will become a world-famous mime and communicate solely through interpretive dance.",
    "You will invent a device that automatically refills your ice cream cone whenever it's empty.",
    "You will star in your own reality TV show about your adventures as a professional couch potato.",
    "You will become a professional ninja and specialize in stealthy snack raids.",
    "You will open a successful restaurant that serves only breakfast cereal.",
    "You will become a renowned expert in the art of taking perfect selfies.",
    "You will accidentally become a viral internet sensation for your epic fail videos.",
    "You will win an award for the most creative use of duct tape."
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    gender = request.form['gender']
    age = int(request.form['age'])

    prediction = random.choice(predictions)
    return render_template('index.html', name=name, gender=gender, age=age, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
