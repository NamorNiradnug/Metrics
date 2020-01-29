from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello, World! I\'m Namor Niradnug'


app.run()