from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel, ValidationError
from typing import Optional

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.String(200), nullable=False)

# Pydantic Schema for Validation
class PatientSchema(BaseModel):
    name: str
    age: int
    condition: str

# Create database
with app.app_context():
    db.create_all()

# Routes

@app.route('/patients', methods=['POST'])
def add_patient():
    try:
        data = PatientSchema(**request.json)
        new_patient = Patient(
            name=data.name,
            age=data.age,
            condition=data.condition
        )
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({"message": "Patient added successfully"}), 201
    except ValidationError as e:
        return jsonify(e.errors()), 400


@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    result = []
    for p in patients:
        result.append({
            "id": p.id,
            "name": p.name,
            "age": p.age,
            "condition": p.condition
        })
    return jsonify(result)


@app.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get_or_404(id)
    return jsonify({
        "id": patient.id,
        "name": patient.name,
        "age": patient.age,
        "condition": patient.condition
    })


@app.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    patient = Patient.query.get_or_404(id)
    data = request.json
    patient.name = data.get("name", patient.name)
    patient.age = data.get("age", patient.age)
    patient.condition = data.get("condition", patient.condition)
    db.session.commit()
    return jsonify({"message": "Patient updated successfully"})


@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return jsonify({"message": "Patient deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)