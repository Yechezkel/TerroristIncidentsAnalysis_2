from flask import Blueprint, jsonify
from db.queries import get_top_5_most_harmful_terror_organization

get_info_bp = Blueprint('get_info', __name__)


@get_info_bp.route('/top_5_most_harmful_terror_organizations')
def get_top_5_most_harmful_terror_organization_route():
    result = get_top_5_most_harmful_terror_organization()
    if result:
        return jsonify({"data": result, "success": True}), 200
    return jsonify({"error": "internal server error", "success": False}), 500