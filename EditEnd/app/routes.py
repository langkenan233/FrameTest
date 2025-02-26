from flask import Blueprint, jsonify

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/api/test')
def test():
    return jsonify({"message": "Hello from Flask!"})