from flask import Blueprint, jsonify, request
from . import db
from .models import MenuItem, Category, Reservation

bp = Blueprint("api", __name__)


@bp.route("/menu")
def get_menu():
    category = request.args.get("category")
    query = MenuItem.query
    if category:
        cat = Category.query.filter_by(name=category).first()
        if cat:
            query = query.filter_by(category_id=cat.id)
    return jsonify([item.to_dict() for item in query.all()])


@bp.route("/menu/featured")
def get_featured():
    items = MenuItem.query.filter_by(featured=True).all()
    return jsonify([item.to_dict() for item in items])


@bp.route("/menu/categories")
def get_categories():
    return jsonify([c.to_dict() for c in Category.query.all()])


@bp.route("/reservations", methods=["POST"])
def create_reservation():
    data = request.get_json()
    required = ["name", "email", "phone", "date", "time", "guests"]
    if not all(data.get(f) for f in required):
        return jsonify({"error": "Missing required fields"}), 400
    reservation = Reservation(
        name=data["name"],
        email=data["email"],
        phone=data["phone"],
        date=data["date"],
        time=data["time"],
        guests=int(data["guests"]),
        message=data.get("message", ""),
    )
    db.session.add(reservation)
    db.session.commit()
    return jsonify({"message": "Reservation confirmed!", "id": reservation.id}), 201


@bp.route("/reservations")
def get_reservations():
    return jsonify([r.to_dict() for r in Reservation.query.order_by(Reservation.created_at.desc()).all()])
