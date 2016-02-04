from flask import Flask, render_template
import os
import argparse

template_folder = os.path.join(os.path.dirname(__file__), 'templates')
app = Flask(__name__, template_folder=template_folder)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


def parse_arguments():
    pass


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
