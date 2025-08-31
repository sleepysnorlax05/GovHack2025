# Data (`src/data`)

This directory is responsible for all data-related operations in the PhishSlayer application.

### `mongodb.py`

This file manages the connection to the MongoDB database and handles the storage and retrieval of phishing reports submitted by users. Key functions include:

* `save_report(report_data)`: Saves a new phishing report to the database, including the extracted text, URLs, prediction scores, and user-provided information.
* `get_reports(limit=100)`: Retrieves the most recent phishing reports from the database.