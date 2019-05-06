from flask import Flask


def register_blueprints(app):
    from distance.controllers import distance
    app.register_blueprint(distance)


def get_app(config='DEV'):
    app = Flask(__name__)
    register_blueprints(app)
    return app
