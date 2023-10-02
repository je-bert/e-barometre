from flask_mail import Mail, Message
from flask import render_template
import os

mail = None

def init(app):
  app.config['SECRET_KEY'] = 'top-secret!'
  app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
  app.config['MAIL_PORT'] = 587
  app.config['MAIL_USE_TLS'] = True
  app.config['MAIL_USERNAME'] = 'apikey'
  app.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
  app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
  global mail
  mail = Mail(app)

def send_reset_password(email, id, token, admin_app = False):
  global mail
  if mail:
    msg = Message('Réinitialiser mon mot de passe', recipients = [email])
    link_admin = "http://localhost:3000/admin/auth/complete-reset-password?id={}&token={}".format(id, token)
    link_client = "http://localhost:4300/auth/complete-reset-password?id={}&token={}".format(id, token)
    msg.html = render_template('mail/reset-password.html', link = link_admin if admin_app else link_client)
    mail.send(msg)

def send_confirm_reset_password(email):
  global mail
  if mail:
    msg = Message('Mot de passe réinitialisé', recipients = [email])
    msg.html = render_template('mail/confirm-reset-password.html')
    mail.send(msg)

def send_account_created(email, password):
  global mail
  if mail:
    msg = Message('Votre compte a été créé', recipients = [email])
    link = "http://localhost:3000/auth/sign-in" #TODO: Real url
    msg.html = render_template('mail/account-created.html', link = link, email = email, password = password)
    mail.send(msg)
  
def send_payment_failed(email):
  global mail
  if mail:
    msg = Message("Votre achat n'a pas pu être complété", recipients = [email])
    link = "http://localhost:3000/auth/sign-in" #TODO: Real url
    msg.html = render_template('mail/payment-failed.html', link = link)
    mail.send(msg)

def send_invoice(email):
  global mail
  if mail:
    msg = Message("Votre facture est prête", recipients = [email])
    link = "http://localhost:3000/auth/sign-in"
    msg.html = render_template('mail/invoice.html', link = link)
    mail.send(msg)