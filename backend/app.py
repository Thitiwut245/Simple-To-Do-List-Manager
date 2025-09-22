from flask import Flask, render_template
from backend.routes.tasks import tasks_bp
from backend.database import init_db

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(tasks_bp, url_prefix="/tasks")

    # Initialize DB
    with app.app_context():
        init_db()

    # Serve index.html from templates/
    @app.route("/")
    def index():
        return render_template("index.html")

    return app

# Create the app
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

