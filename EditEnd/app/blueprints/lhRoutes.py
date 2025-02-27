from flask import Blueprint, jsonify

lh_blueprint = Blueprint('lh', __name__,url_prefix='/api')

@lh_blueprint.route('/lh')
def user_profile():
    return jsonify({"message": "Hello lh! Powered by lkn233"})


# lh_blueprint = Blueprint('lh', __name__)
# 
# @lh_blueprint.route('/api/lh')
# def user_profile():
#     return jsonify({"message": "Hello lh! Powered by lkn233"})