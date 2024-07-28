from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from datetime import datetime
from extensions import db, login_manager
from models import User, Task


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)
migrate = Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!', 'success')  # Set the success message here
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')
    return render_template('login.html')


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')  # Set the logout message here
    return redirect(url_for('login'))  # Redirect to login after logout


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/add', methods=['POST'])
@login_required
def add_task():
    task_content = request.form.get('task')
    task_description = request.form.get('description')
    task_priority = request.form.get('priority')
    due_date = request.form.get('due_date')
    if task_content:
        new_task = Task(content=task_content, description=task_description, priority=task_priority, due_date=datetime.strptime(due_date, '%Y-%m-%d') if due_date else None, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['GET'])
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully.', 'success')
    else:
        flash('Task not found or you do not have permission to delete it.', 'danger')
    return redirect(url_for('index'))


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.content = request.form.get('task')
        task.description = request.form.get('description')
        task.priority = request.form.get('priority')
        task.due_date = datetime.strptime(request.form.get('due_date'), '%Y-%m-%d') if request.form.get('due_date') else None
        db.session.commit()
        flash('Task updated successfully.', 'success')
        return redirect(url_for('index'))
    return render_template('edit_task.html', task=task)

@app.route('/')
@login_required
def index():
    search_query = request.args.get('search', '')
    tasks = Task.query.filter(Task.content.contains(search_query), Task.user_id == current_user.id).all()
    return render_template('index.html', tasks=tasks)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
