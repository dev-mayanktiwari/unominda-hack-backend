from flask import Flask
from flask_cors import CORS
from routes.health import health_bp
from routes.extract_invoice import extract_invoice_bp
from routes.predict import predict_bp

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(health_bp, url_prefix='/health')
app.register_blueprint(extract_invoice_bp, url_prefix='/extract-invoice')
app.register_blueprint(predict_bp, url_prefix='/predict')

if __name__ == '__main__':
    app.run(debug=True)