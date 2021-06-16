from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'weinhgow fmqwfp'

    from .views import views
    from .auth import auth
    # url_prefix : all of the URLs that are stored in these blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
