from flask import Flask

from .views import notes

app = Flask(__name__)

app.register_blueprint(notes)