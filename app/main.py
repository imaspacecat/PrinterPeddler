from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import User, Printer
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)


@main.route("/printer/list")
def get_printers():
    printers = Printer.query.all()
    
    return jsonify([printer.to_json() for printer in printers])

@main.route("/printer", methods=["POST"])
def create_printer():
    if not request.json:
        abort(400)
    print(request.json.get("model"))
    new_printer = Printer(
                model=request.json.get("model"),
                mx=request.json.get("mx"),
                b=request.json.get("b"),
                user_id=current_user.get_id()
            )

    db.session.add(new_printer)
    db.session.commit()

    return jsonify(new_printer.to_json()), 201




