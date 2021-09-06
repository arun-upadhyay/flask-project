from flask import Blueprint, render_template, abort, request, redirect
from jinja2 import TemplateNotFound
from models.User import User

dashboard_view = Blueprint('dashboard_view', __name__, template_folder='/templates')


@dashboard_view.route('/dashboard')
def dashboard():
    try:
        user = User()
        users = user.get_all_users()
        print(users)
        listUsers = []
        for user in users:
            listUsers.append({
                'key': user[0],
                'username': user[1],
                'password': user[2]
            });
        return render_template('dashboard.html', users=listUsers)
    except TemplateNotFound:
        abort(404)
