from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt
from .models import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    from .routes.auth import auth_bp
    from .routes.supplier import supplier_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(supplier_bp)

    @app.get("/api/health")
    def health():
        return {"status": "success", "message": "Manufacturing ERP API is running"}

    @app.get("/api/health/db")
    def database_health():
        from sqlalchemy import text

        result = db.session.execute(text("SELECT 1"))
        return {"status": "success", "database": result.scalar()}

    return app
