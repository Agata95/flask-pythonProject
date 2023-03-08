from flask import Flask, render_template, request
from additional_functions.login_functions import login_ok
from additional_functions.scripts import generate_token

app = Flask("moja_apka")


@app.route("/")
def mainpage():
    return render_template('index.html')


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


@app.route("/user_template/<user_name>")
def user_page_template(user_name):
    return render_template("user_template.html",
                           username=user_name)


# /test_request?a=3&b=45 HTTP/1.1" 200 -
@app.route("/test_request")
def test_request():
    # print(dir(request))
    print(request.remote_addr)
    print(request.headers)
    print("----------------------")
    print(request.args)
    print("----------------------")
    print(request.args.to_dict())
    return "NOTHING in html"


# /login?login=login_name&password=passwd
@app.route("/login/")
def login():
    login_dict = request.args.to_dict()
    if login_ok(login_dict):
        login_name = login_dict['login']
        passwd = login_dict['password']
        return render_template("login_ok.html",
                               login=login_name,
                               password=passwd)
    else:
        return render_template("login_error.html")


app.run()
