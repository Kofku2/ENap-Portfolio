from flask import Flask
app = Flask(__name__)
Scss(app, static_dir='static', asset_dir='assets')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
