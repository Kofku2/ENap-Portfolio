from app import app, render_template


@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
