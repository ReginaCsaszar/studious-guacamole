from flask import Flask, request, render_template, redirect
app = Flask(__name__)

# @app.route("/")
# @app.route("/list")

# @app.route("/new-question")

# @app.route("/question/<question_id>")

# @app.route("/question/<question_id>/new-answer")


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()