from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        a = float(request.form['num1'])
        b = float(request.form['num2'])
        result = a + b
        return render_template('after.html', data=result)


if __name__ == "__main__":
    app.run(debug=False)

