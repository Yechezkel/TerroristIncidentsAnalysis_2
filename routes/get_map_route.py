from flask import Blueprint, jsonify, render_template_string
from db.queries import get_deadly_score_average
import folium

get_map_bp = Blueprint('get_map', __name__)

@get_map_bp.route('/deadly_score_average', methods=['GET'])  #todo: to add a template file
def get_deadly_score_average_route():
    result = get_deadly_score_average()
    if result:
        m = folium.Map(location=[20, 0], zoom_start=2)
        for item in result:
            folium.Marker(location=[item["latitude"], item["longitude"]], popup=f"ID: {item['id']}").add_to(m)
        map_html = m._repr_html_()
        return render_template_string("""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Map</title>
                </head>
                <body>
                    {{ map_html|safe }}
                </body>
                </html>
            """, map_html=map_html), 200
    return jsonify({"error": "internal server error", "success": False}), 500

