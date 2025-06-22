from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/instructor')
def instructors():
    return render_template('instructor.html')

@main_bp.route('/inquiry')
def inquiry():
    return render_template('inquiry.html')

@main_bp.route('/gallery')
def gallery():
    return render_template('gallery.html')

@main_bp.route('/register')
def register():
    return render_template('register.html')

@main_bp.route('/register/thank-you')
def thankyou():
    return render_template('thankyou.html')

@main_bp.route('/login')
def login():
    return render_template('login.html')

@main_bp.route('/login/view')
def viewstudents():
    return render_template('viewstudents.html')

@main_bp.route('/login/view/name')
def student():
    return render_template('student.html')