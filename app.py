from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
with app.app_context():
    # Create database tables
    db.create_all()

@app.route('/submit', methods=['Post', 'GET'])
def submit():
    if request.method == 'POST':
        Name = request.form.get('name')
        Email = request.form.get('email')
        Message = request.form.get('message')
        new_data = FormData(
            name = Name,
            email = Email,
            message = Message
        )
        db.session.add(new_data)
        db.session.commit()
        return f'Thank you {Name} you message "{Message}" has been submitted'
    else:
        return "Hi you with get method"
@app.route('/view_data', methods=['GET'])
def view_data():
    # Retrieve all data from the database
    all_data = FormData.query.all()
    return render_template('view_data.html', data=all_data)
if __name__ == '__main__':
    app.run(debug=True)
