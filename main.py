from flask import Flask

app = Flask("moja_apka")


@app.route("/")
def mainpage():
    return "<H1> HEJ! </H1>"


app.run()
