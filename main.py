from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('main.html')
@app.route('/cal')
def cal(name=None):
	return render_template('cal.html', name=name)
@app.route('/sud')
def sud():
	cuadros = [5,15,25,35]
	return render_template('sud.html',cuadros=cuadros)

if __name__ == "__main__":
    app.run()
