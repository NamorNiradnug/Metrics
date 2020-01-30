from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def start() -> 'html':
    return render_template('start.html',
                           the_title='metrics',
                           distance='')


if __name__ == '__main__':
    app.run(debug=True)
