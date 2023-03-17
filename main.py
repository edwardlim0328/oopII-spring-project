from website import create_app
from flask import Flask, request, jsonify, render_template
from basic_calculator_function import basic_calculator
app = Flask(__name__, template_folder='templates')
app = create_app()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    result = basic_calculator(a,b,operation)

    return render_template('home.html')

if __name__ == '__main__': 
    app.run(debug=True) #run our flask webserver