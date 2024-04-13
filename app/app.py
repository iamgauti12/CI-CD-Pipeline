from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

# Sample to-do list
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form['todo']
    todos.append(todo)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_todo(index):
    del todos[index]
    return redirect(url_for('index'))

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0')
