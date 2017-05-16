from flask import Flask
import os


application = Flask(__name__)


@application.route("/")
def hello():
    return os.getenv('AYY', "Ayyyy 😎!!")


if __name__ == "__main__":
    application.run()
