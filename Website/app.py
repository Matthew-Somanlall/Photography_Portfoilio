from flask import Flask, render_template

app = Flask(__name__)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
