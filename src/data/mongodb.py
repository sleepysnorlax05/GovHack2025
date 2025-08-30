from pymongo import MongoClient
from datetime import datetime
import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

client = MongoClient(MONGODB_URI)
db = client["phishing_reports_db"]
collection = db["reports"]

def save_report(report_data):
    report_data['timestamp'] = datetime.utcnow()
    # user_ip and ip_permission fields included if present in report_data
    result = collection.insert_one(report_data)
    return result.inserted_id

def get_reports(limit=100):
    return list(collection.find().sort("timestamp", -1).limit(limit))
