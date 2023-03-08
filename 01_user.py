from flask import Flask
from additional_functions.scripts import generate_token

app = Flask("moja_apka")


@app.route("/")
def mainpage():
    return '<H1> HEJ! </H1> <a href="hello">Clik here!</a>'


@app.route("/hello")
def secondpage():
    new_token = generate_token()
    html_response = f"""
    <h2> HELLO! </h2> <hr>
    It's new website... <br>
    <b>New user token: {new_token}</b> <br>
    <h4><a href="/user/{new_token}">User site - {new_token}.</a></4>
    """
    return html_response


@app.route("/user/")
def user_info():
    html = """
    Give after / your login
    """
    return html


@app.route("/user/<user_name>")
def user_page(user_name):
    html = f"""
        <H1>Welcome new user</H1>
        Send email to: {user_name}
        <br><br>
        <a href="/hello">Back to menu.</a>
        """
    return html


app.run()
