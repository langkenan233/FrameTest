from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # 注册蓝图（示例）

    from .routes import main_blueprint
    app.register_blueprint(main_blueprint)


    return app

#这个注册蓝图我暂时不会