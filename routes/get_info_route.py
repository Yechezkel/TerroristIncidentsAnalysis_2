from flask import Blueprint, jsonify
from db.queries import get_top_5_most_harmful_terror_organization, get_most_deadly_attack_types

get_info_bp = Blueprint('get_info', __name__)


@get_info_bp.route('/top_5_most_harmful_terror_organizations')
def get_top_5_most_harmful_terror_organization_route():
    result = get_top_5_most_harmful_terror_organization()
    if result:
        return jsonify({"data": result, "success": True}), 200
    return jsonify({"error": "internal server error", "success": False}), 500


@get_info_bp.route('/most_deadly_attack_types', defaults={'limit': 5})
@get_info_bp.route('/most_deadly_attack_types/<int:limit>') # todo to add an option to add limit
def get_most_deadly_attack_types_route(limit):
    result = get_most_deadly_attack_types(limit)
    if result:
        return jsonify({"data": result, "success": True}), 200
    return jsonify({"error": "internal server error", "success": False}), 500