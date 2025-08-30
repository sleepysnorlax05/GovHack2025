from pymongo import MongoClient
from datetime import datetime
import os

# Get MongoDB URI from environment variable, fallback to localhost
MONGODB_URI = os.getenv("MONGODB_URI")

# Initialize MongoDB client and database/collection
client = MongoClient(MONGODB_URI)
db = client["phishing_reports_db"]
collection = db["reports"]

def save_report(report_data):
    """
    Save report document to MongoDB with timestamp.
    
    Args:
      report_data (dict): Dictionary containing report fields.

    Returns:
      ObjectId of the inserted document.
    """
    report_data['timestamp'] = datetime.utcnow()
    result = collection.insert_one(report_data)
    return result.inserted_id

def get_reports(limit=100):
    """
    Retrieve recent reports, default limit 100.
    
    Args:
      limit (int): Max number of reports to retrieve.

    Returns:
      List of reports sorted by timestamp descending.
    """
    return list(collection.find().sort("timestamp", -1).limit(limit))
