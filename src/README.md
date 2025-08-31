# Source Code (`src`)

This directory contains the core source code for the PhishSlayer application, organized into the following subdirectories:

* [`data`](data/): Handles data storage and retrieval, including interactions with the MongoDB database.
* [`frontend`](frontend/): Contains the Streamlit-based user interface components for the web application.
* [`models`](models/): Includes the machine learning model and related functions for phishing detection.
* [`resources`](resources/): Stores static assets used by the application, such as images and logos.
* [`utils`](utils/): Provides utility functions for various tasks, including OCR, IP address retrieval, and threat intelligence lookups.

The main entry point for the application is `main.py`, which orchestrates the different pages and components of the user interface.