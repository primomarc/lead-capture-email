from flask import Flask, render_template, request, flash, redirect
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for flash messages

# Ensure the data folder exists
if not os.path.exists("data"):
    os.makedirs("data")

LEADS_CSV = "data/leads.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(LEADS_CSV):
    df = pd.DataFrame(columns=["email"])
    df.to_csv(LEADS_CSV, index=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]

        # Append the email to the CSV file
        df = pd.read_csv(LEADS_CSV)
        new_data = pd.DataFrame([{"email": email}])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(LEADS_CSV, index=False)

        flash("✅ Thank you for subscribing! Check your email for the AI Guide.", "success")
        return redirect("/")  # Redirect back to show the message

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
