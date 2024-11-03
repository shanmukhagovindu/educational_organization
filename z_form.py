from flask import Flask, render_template, request, redirect, url_for, flash # type: ignore
from flask_mail import Mail, Message # type: ignore

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'govindushan@gmail.com'  # your email address
app.config['MAIL_PASSWORD'] = 'G?@4vijaypavan.'         # your email password or app password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/z_form', methods=['POST'])
def z_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        if not name or not email or not subject or not message:
            flash('All fields are required!')
            return redirect(url_for('index'))

        email_body = f"""
        User Name: {name}
        User Email: {email}
        Subject: {subject}
        User Message: {message}
        """

        msg = Message('New Form Submission', sender='govindushan@gmail.com', recipients=['shanmukhagovindu@gmail.com'])
        msg.body = email_body

        try:
            mail.send(msg)
            flash('Email sent successfully!')
        except Exception as e:
            flash(f'Error sending email: {e}')
        
        return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('z_form.html')

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)
