from flask import Blueprint, jsonify

whl_blueprint = Blueprint('whl', __name__,url_prefix='/api')

@whl_blueprint.route('/whl')
def user_profile():
    return jsonify({"message": "Hello whl! Powered by lkn233"})

# whl_blueprint = Blueprint('whl', __name__)
# 
# @whl_blueprint.route('/api/whl')
# def user_profile():
#     return jsonify({"message": "Hello whl! Powered by lkn233"})