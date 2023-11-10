# Import necessary libraries
import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run_tests", methods=["POST"])
def run_tests():
    # Change to the directory where your tests are located
    tests_directory = "path/to/your/tests"
    os.chdir(tests_directory)

    # Run Pytest using subprocess
    result = subprocess.run(
        ["pytest"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    # Capture the output and error messages
    output = result.stdout
    error = result.stderr

    return render_template("index.html", output=output, error=error)


if __name__ == "__main__":
    app.run(debug=True)
