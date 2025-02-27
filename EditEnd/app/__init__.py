from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # 注册蓝图（示例）

    from .routes import main_blueprint
    app.register_blueprint(main_blueprint)

    from .blueprints.hzxRoutes import hzx_blueprint
    app.register_blueprint(hzx_blueprint)

    from .blueprints.lhRoutes import lh_blueprint
    app.register_blueprint(lh_blueprint)

    from .blueprints.lknRoutes import lkn_blueprint
    app.register_blueprint(lkn_blueprint)

    from .blueprints.lukeRoutes import luke_blueprint
    app.register_blueprint(luke_blueprint)

    from .blueprints.whlRoutes import whl_blueprint
    app.register_blueprint(whl_blueprint)

    return app

#这个注册蓝图我暂时不会