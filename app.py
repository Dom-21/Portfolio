from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail with Gmail SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'olepenco@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'ebbx pibv nozz rcbi'  # Your app password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Create the email content
    msg = Message('New Contact Form Submission', 
                  sender='olepenco@gmail.com', 
                  recipients=['dandavateomkar@gmail.com'])  # Your recipient email
    msg.body = f"Name: {name}\nEmail: {email}"
    
    # Send the email
    mail.send(msg)
    
    return f"Thank you {name}! Your message has been sent."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)

