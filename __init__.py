import os

from flask import Flask

UPLOAD_FOLDER = os.path.abspath("./flaskr/static/images/")

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpge", "jpeg"])

def create_app(self, test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config.from_mapping(
        SECRET_KEY=b'\xa1\xbb\xaa\xbe\x15\xa2\x97\x8ccf\xdePsO"\xdc',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from db import init_app
    db.init_app(app)

    from auth import register_blueprint
    app.register_blueprint(auth.bp)

    from blog import register_blueprint, add_url_rule
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app