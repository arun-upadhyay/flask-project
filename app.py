from flask import Flask, jsonify, render_template
from routes.user_view import user_view
from routes.dashboard_view import dashboard_view

app = Flask(__name__)

app.register_blueprint(user_view)
app.register_blueprint(dashboard_view)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
