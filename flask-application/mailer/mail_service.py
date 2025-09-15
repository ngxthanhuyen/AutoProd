from flask_mail import Message

# Fonction factory pour créer un objet Message (email)
def create_email(recipient, subject, body):
    return Message(subject=subject, recipients=[recipient], body=body)