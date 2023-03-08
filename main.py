from flask import Flask

app = Flask("moja_apka")


@app.route("/")
def mainpage():
    return '<H1> HEJ! </H1> <a href="data"> Idź do strony </a>'


@app.route("/data")
def secondpage():
    html_response = """
    <h2> WITAM! </h2> <hr>
    Nowa stronka... <br>
    <b> nowy tekst </b>
    """
    return html_response


app.run()
