from flask import Blueprint, request, jsonify
from Services.troop_service import TroopService

troop_bp = Blueprint('troop_bp', __name__)
troop_service = TroopService()

@troop_bp.route("/card-names", methods=["POST"])
def get_card_names():
    data = request.get_json()
    try:
        card_names = troop_service.get_card_names_by_ids(data['cardIds'])
        return jsonify(card_names), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
