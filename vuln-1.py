import os
import flask

app = flask.Flask(__name__)


@app.route("/route_param/<route_param>")
def route_param(route_param):

    # ruleid:dangerous-os-exec
    allowed_commands = ["command1", "command2"]
    if route_param in allowed_commands:
        clean_command = allowed_commands[allowed_commands.index(route_param)]
        os.execl("/bin/bash", "/bin/bash", "-c", clean_command)
    else
        abort(400)

    return "oops!"


# Flask true negatives
@app.route("/route_param/<route_param>")
def route_param2(route_param):

    # ok:dangerous-os-exec
    os.execl("static")

    return "ok!"
