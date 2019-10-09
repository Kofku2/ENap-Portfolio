from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('main.scss', filters='pyscss, cssmin', output='styles.css')
assets.register('scss_main', scss)


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=False)
