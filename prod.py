from waitress import serve
from main import app
serve(app.app, host='0.0.0.0', port=5000)

# This file should only be used on prod