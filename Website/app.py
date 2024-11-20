from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Email configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Required for flash messages
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your.email@gmail.com'  # Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'your-app-password'  # Replace with your app password

mail = Mail(app)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        msg = Message('New Contact Form Submission',
                     sender=app.config['MAIL_USERNAME'],
                     recipients=[app.config['MAIL_USERNAME']])
        
        msg.body = f"""
        New message from your website:
        
        Name: {name}
        Email: {email}
        Message: {message}
        """
        
        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('An error occurred sending your message. Please try again.', 'error')
            
        return redirect(url_for('contacts'))
        
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)