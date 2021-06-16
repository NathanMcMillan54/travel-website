from flask import Flask, render_template, request
import db

id_number = 0

app = Flask(__name__)


@app.route('/')
def root():
    return render_template("index.html")


@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        db.log_input(request.form)
    return render_template("booking.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
