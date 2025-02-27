from flask import Blueprint, jsonify

hzx_blueprint = Blueprint('hzx', __name__,url_prefix='/api')

@hzx_blueprint.route('/hzx')
def user_profile():
    return jsonify({"message": "Hello hzx! Powered by lkn233"})


# hzx_blueprint = Blueprint('hzx', __name__)
#
# @hzx_blueprint.route('/api/hzx')
# def user_profile():
#     return jsonify({"message": "Hello hzx! Powered by lkn233"})