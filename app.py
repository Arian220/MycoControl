from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html')

@app.route('/psychrometric')
def psychrometric():
    return render_template('psychrometric.html')

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

if __name__ == '__main__':
    app.run(debug=True)