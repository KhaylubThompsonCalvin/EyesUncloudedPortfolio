# EyesUnclouded Portfolio Interface
# File: app.py
# Project: EyesUncloudedPortfolio
# Author: Khaylub Thompson-Calvin
# Date: 5/2/2025
# Description:
# This Flask application serves as the interactive 3D portfolio interface for the EyesUnclouded project.
# It combines immersive Three.js-rendered experiences with symbolic routes, database connectivity,
# and emotional intelligence-based modules.
#
# Features:
# - Renders interactive portfolio scenes via HTML/CSS/JS + WebGL (e.g., lab_scene.html)
# - Connects to MongoDB Atlas for dynamic data services and future AI reflection logs
# - Loads environmental configuration securely from .env
# - Provides a /status route for verifying MongoDB connection
# - Acts as the symbolic and narrative frontend to the EyesUnclouded legacy system
#
# Symbolic Role:
# This interface represents the "Living Archive" — a perceptual layer where descendants and visitors
# navigate symbolic experiences, narrative entries, and reflective logs. Each route may correspond to
# a memory shard, role path, or insight chamber within the EyesUnclouded Universe.
#
# Source References:
# - Flask documentation: https://flask.palletsprojects.com/
# - Three.js docs: https://threejs.org/docs/
# - MongoDB Atlas connection string format
# - Project memories and symbolic structure outlined in the Atlas Signature Scaffold


from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Connect to MongoDB
client = MongoClient(os.getenv("DB_URI"))
db = client.get_database()  # Automatically picks default DB from URI

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lab')
def lab():
    return render_template('lab_scene.html')

@app.route('/status')
def status():
    return f"✅ Connected to MongoDB: {db.name}"

if __name__ == '__main__':
    app.run(debug=True, port=7001)













