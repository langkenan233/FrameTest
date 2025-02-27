from flask import Blueprint, jsonify

luke_blueprint = Blueprint('luke', __name__,url_prefix='/api')

@luke_blueprint.route('/luke')
def user_profile():
    return jsonify({"message": "Hello luke! Powered by lkn233"})

# luke_blueprint = Blueprint('luke', __name__)
# 
# @luke_blueprint.route('/api/luke')
# def user_profile():
#     return jsonify({"message": "Hello luke! Powered by lkn233"})