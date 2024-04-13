# app.py
from flask import Flask, render_template, request
import random

app = Flask(__name__)

predictions = [
    "You will become a famous artist.",
    "You will travel the world and explore new cultures.",
    "You will find true love and live happily ever after.",
    "You will get 3.8 GPA in this Semester, Don't forget to give treat to whole class.",
    "You will become a successful entrepreneur and start your own business.",
    "You will discover a hidden talent that will bring you great success.",
    "You will achieve your lifelong dreams and aspirations.",
    "You will make a positive impact on the world and leave a lasting legacy.",
    "You will lead a life filled with adventure and excitement.",
    "You will find inner peace and enlightenment through spiritual growth."
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
