import csv
from flask import Flask, request, jsonify
from flask_cors import CORS
from database.db import Database
from models import Facility, Regulation, StorageConfiguration
import os

app = Flask(__name__)
CORS(app)

# Initialize the database
db = Database()

# Load initial data if needed
def load_initial_data():
    # Check if we already have data
    conn = db._get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM facilities")
    facility_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM regulations")
    regulation_count = cursor.fetchone()[0]
    conn.close()
    
    if facility_count == 0:
        # Load facilities from CSV file
        try:
            facilities = []
            with open('data/facilities.csv', 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    facility = Facility.from_dict(row)
                    facilities.append(facility)
                
                db.insert_facilities(facilities)
                print(f"Loaded {len(facilities)} facilities")
        except Exception as e:
            print(f"Error loading facilities: {e}")
    
    if regulation_count == 0:
        # Load regulations from CSV file
        try:
            regulations = []
            with open('data/regulations.csv', 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    regulation = Regulation.from_dict(row)
                    regulations.append(regulation)
                
                db.insert_regulations(regulations)
                print(f"Loaded {len(regulations)} regulations")
        except Exception as e:
            print(f"Error loading regulations: {e}")