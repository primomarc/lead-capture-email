import os
from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "supersecretkey"

# SMTP Configuration (Gmail or SendGrid)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587  # Ensure you're using 587 (not 465)
app.config["MAIL_USE_TLS"] = True  # Use TLS, not SSL
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = "marclester0701@gmail.com"
app.config["MAIL_PASSWORD"] = "upul zzci scoj zdkc"  # Use an App Password, NOT your Gmail password
app.config["MAIL_DEFAULT_SENDER"] = "marclester0701@gmail.com"  # Use your verified sender email

mail = Mail(app)

# Path to your eBook
EBOOK_PATH = os.path.join(os.getcwd(), "static", "Stoic_Nomad_eBook.pdf")

def send_personalized_email(email, name, interest):
    msg = Message("Welcome to Stoic Nomad!", recipients=[email])
    msg.html = render_template("email_template.html", name=name, interest=interest)

    # Attach the eBook
    with open(EBOOK_PATH, "rb") as pdf:
        msg.attach("Stoic_Nomad_eBook.pdf", "application/pdf", pdf.read())

    mail.send(msg)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name", "Stoic Nomad")
        interest = request.form.get("interest", "Self-Improvement")

        send_personalized_email(email, name, interest)

        flash("✅ Thank you for subscribing! Your eBook is on the way!", "success")
        return redirect("/")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)