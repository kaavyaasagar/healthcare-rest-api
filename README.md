#  Healthcare Patient Management REST API

A backend REST API built using Flask, SQLAlchemy, and Pydantic for managing patient records.

##  Features

- Add Patient
- Get All Patients
- Get Patient by ID
- Update Patient
- Delete Patient
- Input validation using Pydantic
- SQLite database integration

##  Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Pydantic
- SQLite

##  Installation

```bash
git clone https://github.com/kaavyaasagar/healthcare-rest-api.git
cd healthcare-rest-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

##  API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| POST   | /patients      | Add new patient   |
| GET    | /patients      | Get all patients  |
| GET    | /patients/<id> | Get patient by ID |
| PUT    | /patients/<id> | Update patient    |
| DELETE | /patients/<id> | Delete patient    |

##  What I Learned

- REST API development using Flask  
- Database integration using SQLAlchemy  
- Data validation using Pydantic  
- CRUD operations  
- Git version control & GitHub workflow  
- Backend project structuring
