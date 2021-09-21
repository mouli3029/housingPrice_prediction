from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        age = request.form['age']
        bedrooms = request.form['bedrooms']
        area = request.form['area']

        print(age)
        print(bedrooms)
        print(area)

        with open(f'model/model.pkl', 'rb') as f:
            model = pickle.load(f)
        result = model.predict([[area, bedrooms, age]])
        result = result[0].__ceil__()
        return render_template('index.html', result=result)


if __name__ == '__main__':
    app.config(debug=True)
