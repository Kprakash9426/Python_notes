from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL connection (update username & password!)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@localhost/task_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Task {self.title}>"

# Create tables (run once)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)




# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# # In-memory list of tasks (id, title)
# tasks = [(1, "Sample Task")]

# @app.route('/')
# def index():
#     return render_template('index.html', tasks=tasks)

# @app.route('/add', methods=['POST'])
# def add():
#     title = request.form['title']
#     task_id = len(tasks) + 1
#     tasks.append((task_id, title))
#     return redirect(url_for('index'))

# @app.route('/delete/<int:task_id>')
# def delete(task_id):
#     global tasks
#     tasks = [t for t in tasks if t[0] != task_id]
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)
