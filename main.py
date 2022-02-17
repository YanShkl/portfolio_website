from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
import os



app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')
RECEIVING_EMAIL = os.environ.get('RECEIVING_EMAIL')


SMTP_SERVER = "smtp.gmail.com"
PORT = 587


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/send_message', methods=["GET", "POST"])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        with smtplib.SMTP(SMTP_SERVER, PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECEIVING_EMAIL,
                msg=f"Subject:{subject}\n\nName:{name}\nEmail{email}\nMessage: {message}"
            )

        flash(u"Message was Successfully Sent!", 'success')
        return redirect(url_for('main'))


if __name__ == "__main__":
    app.run(debug=True)
