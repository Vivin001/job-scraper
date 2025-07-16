from flask import Flask, render_template, request
from scraper import scrape_jobs
from notifier import send_email

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        role = request.form["role"]
        location = request.form["location"]

        print("Sending email to:", email)

        job_results = scrape_jobs(role, location)
        send_email(name, email, job_results)

        return render_template("success.html", name=name)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
