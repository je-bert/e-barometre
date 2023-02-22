from flask_mail import Mail, Message
from flask import render_template

mail = None

def init(app):
  app.config['MAIL_SERVER']='smtp.gmail.com'
  app.config['MAIL_PORT'] = 465
  app.config['MAIL_USERNAME'] = 'john.doe.movex@gmail.com'
  app.config['MAIL_PASSWORD'] = 'hzfwtecbpgeamuhv'
  app.config['MAIL_USE_TLS'] = False
  app.config['MAIL_USE_SSL'] = True
  global mail
  mail = Mail(app)

def send_reset_password(email, id, token, admin_app = False):
  global mail
  if mail:
    msg = Message('Réinitialiser mon mot de passe', sender = 'yourId@gmail.com', recipients = [email])
    link_admin = "http://localhost:3000/admin/auth/complete-reset-password?id={}&token={}".format(id, token)
    link_client = "http://localhost:4200/auth/complete-reset-password?id={}&token={}".format(id, token)
    msg.html = render_template('mail/reset-password.html', link = link_admin if admin_app else link_client)
    mail.send(msg)

def send_confirm_reset_password(email):
  global mail
  if mail:
    msg = Message('Mot de passe réinitialisé', sender = 'yourId@gmail.com', recipients = [email])
    msg.html = render_template('mail/confirm-reset-password.html')
    mail.send(msg)