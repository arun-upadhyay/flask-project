from flask import Blueprint, render_template, abort, request, redirect
from jinja2 import TemplateNotFound
from models.User import User
from flask_jwt import JWT, jwt_required, current_identity


user_view = Blueprint('user_view', __name__, template_folder='/templates')

@user_view.route('/', methods=['GET'])
def home():
    try:
        return render_template('login.html')
    except TemplateNotFound:
        abort(404)


@user_view.route('/login', methods=['GET'])
def login():
    try:
        return render_template('login.html')
    except TemplateNotFound:
        abort(404)


@user_view.route('/authenticate', methods=['POST'])
def authenticate():
    try:
        if request.method == 'POST':
            _form = request.form
            username = str(_form["username"])
            password = str(_form["password"])
            user = User()
            if user.get_user(username, password):
                return redirect('/dashboard')
            else:
                return render_template('login.html',
                                       error="Invalid username or password. Please check your credentials!")

    except TemplateNotFound:
        abort(404)


@user_view.route('/user/delete/<id>', methods=['GET'])
def user_delete(id):
    user_id = int(id)
    print(user_id)
    if id is not None:
        user = User()
        user.delete_user(user_id)
        return redirect('/dashboard')


@user_view.route('/user/edit/<id>', methods=['GET'])
def user_edit(id):
    user_id = int(id)
    if id is not None:
        user = User()
        userRecord = user.get_user_by_id(user_id)
        return render_template('dashboard.html',
                               userRecord=userRecord)


@user_view.route('/user/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        _form = request.form
        username = str(_form["username"])
        password = str(_form["password"])
        user = User()
        user.add_user(username, password)
        return redirect('/dashboard')


@user_view.route('/user/edit/user/update', methods=['POST'])
def update_user():
    if request.method == 'POST':
        _form = request.form
        username = str(_form["username"])
        password = str(_form["password"])
        userId = str(_form["id"])
        user = User()
        user.update_user(username, password, userId)
        return redirect('/dashboard')
