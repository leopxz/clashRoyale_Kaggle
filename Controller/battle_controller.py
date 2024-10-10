from flask import Blueprint, request, jsonify
from Services.battle_service import BattleService

battle_bp = Blueprint('battle_bp', __name__)
battle_service = BattleService()

@battle_bp.route("/win-loss-percentage", methods=["GET"])
def get_win_loss_percentage_for_card():
    card_id = request.args.get("cardId")
    start_time = request.args.get("startTime")
    end_time = request.args.get("endTime")
    
    if not card_id or not start_time or not end_time:
        return jsonify({"error": "Missing required parameters"}), 400
    
    try:
        percentage = battle_service.calculate_win_loss_percentage_for_card(card_id, start_time, end_time)
        return jsonify(percentage), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@battle_bp.route("/winning-decks", methods=["POST"])
def get_decks_with_more_than_x_percent_wins():
    data = request.get_json()
    try:
        decks = battle_service.get_decks_with_more_than_x_percent_wins(data['percentage'], data['startTime'], data['endTime'])
        return jsonify(decks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@battle_bp.route("/losses-for-combo", methods=["POST"])
def get_losses_for_combo():
    data = request.get_json()
    
    if not data or 'cardIds' not in data or 'startTime' not in data or 'endTime' not in data:
        return jsonify({"error": "Missing required parameters"}), 400

    try:
        losses = battle_service.calculate_losses_for_combo(data['cardIds'], data['startTime'], data['endTime'])
        return jsonify({"losses": losses}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
