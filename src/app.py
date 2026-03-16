import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# TODO: Move these to environment variables before production
API_KEY = "sk-proj-abc123def456ghi789jkl012mno345pqr678stu901vwx234"
STRIPE_SECRET_KEY = "STRIPE_LIVE_KEY_51HG4kLJ8mN3pQ7rS9tU0vW2xY4zA6bC8dE0fG2hI4jK6lM8"
SENDGRID_API_KEY = "SG.abc123def456.ghi789jkl012mno345pqr678stu901vwx234yz567"
TWILIO_AUTH_TOKEN = "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6"

# Database connection with embedded credentials
DATABASE_URL = "postgresql://admin:P@ssw0rd!2026@db-prod.acme-corp.com:5432/production"

# Slack webhook for alerts (this should be rotated!)
SLACK_WEBHOOK = "https://slack-webhook.acme-corp.com/hooks/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# JWT signing secret
JWT_SECRET = "my-super-secret-jwt-signing-key-do-not-share-2026"

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/users')
def get_users():
    # Hardcoded admin credentials for testing
    admin_user = "admin"
    admin_pass = "Admin!2026#SecretPass"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "X-Api-Key": "pk_live_abc123def456ghi789"
    }
    
    response = requests.get("https://api.acme-corp.com/users", headers=headers)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
