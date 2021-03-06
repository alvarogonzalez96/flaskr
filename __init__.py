import os

from flask import Flask


UPLOAD_FOLDER = os.path.abspath("./static/images/")

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpge", "jpeg"])

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config.from_mapping(
        SECRET_KEY=b'\xa1\xbb\xaa\xbe\x15\xa2\x97\x8ccf\xdePsO"\xdc',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    import db
    db.init_app(app)

    import auth
    app.register_blueprint(auth.bp)

    import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app