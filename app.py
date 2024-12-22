from flask import Flask, render_template_string
from routes.get_info_route import get_info_bp

app = Flask(__name__)
app.register_blueprint(get_info_bp, url_prefix='/get_info')



@app.route('/')
def index():
    routes = [
        '/get_info/top_5_most_harmful_terror_organizations',
        '/get_info/most_deadly_attack_types',
        '/get_info/most_deadly_attack_types/4',
    ]
    return render_template_string('''
        <html>
            <body>
                <h1>Welcome to the API</h1>
                <ul>
                    {% for route in routes %}
                        <li><a href="{{ route }}">{{ route }}</a></li>
                    {% endfor %}
                </ul>
            </body>
        </html>
    ''', routes=routes
    )


if __name__ == '__main__':
    app.run()
