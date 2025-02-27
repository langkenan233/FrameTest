from flask import Blueprint, jsonify

lkn_blueprint = Blueprint('lkn', __name__,url_prefix='/api')

@lkn_blueprint.route('/lkn')
def user_profile():
    return jsonify({"message": "Hello lkn! Powered by lkn233"})

# lkn_blueprint = Blueprint('lkn', __name__)
# 
# @lkn_blueprint.route('/api/lkn')
# def user_profile():
#     return jsonify({"message": "Hello lkn! Powered by lkn233"})