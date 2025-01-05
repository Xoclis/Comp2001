from flask import abort
from models import User

def check_role(email, required_role):
    user = User.query.filter_by(email=email).first()
    if not user or user.role != required_role:
        abort(403, "You do not have permission to perform this action.")
