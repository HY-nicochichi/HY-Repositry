from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_from_directory

bp_doc = get_swaggerui_blueprint(
    base_url = '',
    api_url = 'http://localhost:5000/swagger.json',
    blueprint_name = 'bp_doc'
)

@bp_doc.get('/swagger.json')
def swagger_json():
    return send_from_directory('/', 'swagger.json')
