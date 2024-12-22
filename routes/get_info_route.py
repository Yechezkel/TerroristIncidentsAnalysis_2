from flask import Blueprint, jsonify
from db.queries import get_top_5_most_harmful_terror_organization, get_most_deadly_attack_types, get_top_5_most_harmful_terror_organization

get_info_bp = Blueprint('get_info', __name__)




# question 2.1
@get_info_bp.route('/most_deadly_attack_types', defaults={'limit': None}, methods=['GET'])
@get_info_bp.route('/most_deadly_attack_types/<int:limit>', methods=['GET'])
def get_most_deadly_attack_types_route(limit):
    result = get_most_deadly_attack_types(limit)
    if result:
        return jsonify({"data": result, "success": True}), 200
    return jsonify({"error": "internal server error", "success": False}), 500



# question 2.3
@get_info_bp.route('/top_5_most_harmful_terror_organizations', methods=['GET'])
def get_top_5_most_harmful_terror_organization_route():
    result = get_top_5_most_harmful_terror_organization()
    if result:
        return jsonify({"data": result, "success": True}), 200
    return jsonify({"error": "internal server error", "success": False}), 500

