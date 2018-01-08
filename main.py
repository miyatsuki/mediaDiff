from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/<name>/<name2>')
def hello(name=None, name2=None):
    # return name
    return render_template('hello.html', title='flask test', name=name, name2=name2)


@app.route('/good')
def good():
    name = "Good"
    return name


if __name__ == "__main__":
    app.run(debug=True)
