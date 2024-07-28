# Flask Task Manager

## Overview

This is a Flask-based task manager application that allows users to register, log in, and manage their tasks. The application uses SQLAlchemy for database interactions and Flask-Migrate for database migrations.

## Features

- User registration and authentication
- Task management (add, edit, delete, and view tasks)
- User-specific task handling

## Prerequisites

Ensure you have the following installed:

- Python 3.12 or higher
- Flask 2.2.5 or higher
- Flask-SQLAlchemy 2.5.1 or higher
- Flask-Login 0.6.3 or higher
- Flask-Migrate 4.0.7 or higher
- Werkzeug 2.2.3 or higher

## Installation

Follow these steps to set up and run the application:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialize the database
```bash
flask db init            # Only needed if the migrations folder does not exist
flask db migrate -m "Initial migration"  # Create migration files
flask db upgrade         # Apply the migrations to the database
```
### 4. Run the Flask Application
```bash
flask run
```



