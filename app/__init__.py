from app import routes
from flask import Flask
from flask_assets import Environment, Bundle


app = Flask(__name__)
assets = Environment(app)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('main.scss', filters='pyscss, cssmin', output='styles.css')
assets.register('scss_main', scss)


if __name__ == "__main__":
    app.run(debug=False)
