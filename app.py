from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/submit', methods=['GET'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return f'Thank you {name} you message "{message}" has been submitted'

if __name__ == '__main__':
    app.run(debug=True)
