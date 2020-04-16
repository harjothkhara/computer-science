from flask import Flask
app = Flask(__name__)
# Flask setup practice

# set up our home route
@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"


@app.route("/newpage")
def newpage():
    return "<h1>This is a new page</h1>"


# allows you to run Flask app from terminal
if __name__ == "__main__":
    app.run(debug=True)
    # if you set debug mode to on (True), the dev server will auto-reload
