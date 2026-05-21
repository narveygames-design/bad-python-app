import os
import flask

app = flask.Flask(__name__)


@app.route("/route_param/<route_param>")
def route_param(route_param):

    # Fixed: removed dangerous os.execl with user-controlled input
    # Never pass user input to shell execution functions
    return f"Received parameter: {route_param}"


# Flask true negatives
@app.route("/route_param/<route_param>")
def route_param2(route_param):

    # ok:dangerous-os-exec
    os.execl("static")

    return "ok!"
