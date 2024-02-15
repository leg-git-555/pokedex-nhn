import os

from flask import Flask, send_file
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf # import statement for CSRF
from .config import Configuration
from .models import db
from .seeders import seed_cmd
from .routes import api

app = Flask(__name__)
app.config.from_object(Configuration)
app.cli.add_command(seed_cmd)
app.register_blueprint(api.bp)

db.init_app(app)
Migrate(app, db)


# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get('FLASK_ENV') == 'production' else None,
        httponly=True
    )
    return response


@app.route('/images/<path:path>')
def serve_image(path):
    return send_file(f'public/images/{path}')
