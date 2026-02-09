from flask import Flask
from models import db
from routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    
    db.init_app(app)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

        return app

if __name__=='__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)