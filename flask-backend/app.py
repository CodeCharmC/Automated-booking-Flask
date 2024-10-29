from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = MongoClient(os.getenv("MONGODB_URI"))
db = client['appointments']

@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = list(db.appointments.find({}, {'_id': 0}))
    return jsonify(appointments)

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    db.appointments.insert_one(data)
    return jsonify({"status": "Created"}), 201

@app.route('/appointments/<id>', methods=['PUT'])
def update_appointment(id):
    data = request.json
    db.appointments.update_one({'_id': id}, {'$set': data})
    return jsonify({"status": "Updated"}), 200

@app.route('/appointments/<id>', methods=['DELETE'])
def delete_appointment(id):
    db.appointments.delete_one({'_id': id})
    return jsonify({"status": "Deleted"}), 
