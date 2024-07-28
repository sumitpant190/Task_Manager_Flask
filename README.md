<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Task Manager</title>
</head>
<body>
    <h1>Flask Task Manager</h1>

    <h2>Overview</h2>
    <p>This is a Flask-based task manager application that allows users to register, log in, and manage their tasks. The application uses SQLAlchemy for database interactions and Flask-Migrate for database migrations.</p>

    <h2>Features</h2>
    <ul>
        <li>User registration and authentication</li>
        <li>Task management (add, edit, delete, and view tasks)</li>
        <li>User-specific task handling</li>
    </ul>

    <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.12 or higher</li>
        <li>Flask 2.2.5 or higher</li>
        <li>Flask-SQLAlchemy 2.5.1 or higher</li>
        <li>Flask-Login 0.6.3 or higher</li>
        <li>Flask-Migrate 4.0.7 or higher</li>
        <li>Werkzeug 2.2.3 or higher</li>
    </ul>

    <h2>Installation</h2>
    <h3>1. Clone the Repository</h3>
    <p>First, clone the repository to your local machine:</p>
    <pre><code>git clone &lt;repository_url&gt;
cd &lt;repository_directory&gt;
    </code></pre>

    <h3>2. Set Up a Virtual Environment</h3>
    <p>It’s recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment:</p>
    <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    </code></pre>

    <h3>3. Install Dependencies</h3>
    <p>Install the required Python packages:</p>
    <pre><code>pip install -r requirements.txt
    </code></pre>

    <h3>4. Set Up the Database</h3>
    <p>Initialize the database and apply migrations:</p>
    <pre><code>flask db init           # Only needed if the migrations folder does not exist
flask db migrate -m "Initial migration"  # Create migration files
flask db upgrade        # Apply the migrations
    </code></pre>

    <h3>5. Run the Application</h3>
    <p>Start the Flask development server:</p>
    <pre><code>flask run
    </code></pre>
    <p>The application will be accessible at <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>.</p>

    <h2>Usage</h2>
    <ul>
        <li><strong>Register</strong>: Go to <code>/register</code> to create a new account.</li>
        <li><strong>Login</strong>: Go to <code>/login</code> to log in with your account credentials.</li>
        <li><strong>Manage Tasks</strong>: After logging in, you can add, edit, and delete tasks from the <code>/</code> page (task management interface).</li>
    </ul>

    <h2>Testing</h2>
    <p>You can run the application and manually test the functionality. Automated tests can be added in the future.</p>

    <h2>Contributing</h2>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
        <li>Make your changes.</li>
        <li>Commit your changes (<code>git commit -am 'Add feature'</code>).</li>
        <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
        <li>Create a new Pull Request.</li>
    </ol>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Contact</h2>
    <p>For any issues or questions, please contact <a href="mailto:your_email@example.com">your_email@example.com</a>.</p>
</body>
</html>
