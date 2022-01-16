from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/base')
def base():
    return render_template("base.html")

@auth.route('/status')
def status():
    return render_template("status.html")

@auth.route('/booking')
def booking():
    return render_template("booking.html")