from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')

def noNinjas():
    return render_template('no_ninjas.html')

@app.route('/ninja')

def showNinjas():
    return render_template('show_ninjas.html')

@app.route('/ninja/<ninja_color>')

def showNinjas1(ninja_color):

    return render_template('show_ninjas.html', ninja_color = ninja_color)


app.run(debug=True)
