"""
User Analytics Pipeline
Connects to production database to analyze user behavior.
Author: Data Team
"""

import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Direct production database connection
# TODO: Use vault for credentials management
PROD_DB_URL = "postgresql://analytics_user:An@lytics2026!@db-prod-cluster.us-east-1.rds.amazonaws.com:5432/acme_production"

engine = create_engine(PROD_DB_URL)

# Query sensitive user data
query = """
SELECT 
    u.user_id,
    u.first_name,
    u.last_name,
    u.email,
    u.phone_number,
    u.social_security_number,
    u.date_of_birth,
    p.card_number,
    p.card_expiry,
    p.billing_address,
    t.transaction_amount,
    t.transaction_date
FROM users u
JOIN payment_methods p ON u.user_id = p.user_id
JOIN transactions t ON u.user_id = t.user_id
WHERE t.transaction_date >= '2026-01-01'
ORDER BY t.transaction_amount DESC
"""

df = pd.read_sql(query, engine)

# Export for compliance team - includes all PII!
df.to_csv('/tmp/user_data_with_pii_full_export.csv', index=False)

# Slack notification with webhook
import requests
SLACK_WEBHOOK = "https://slack-webhook.acme-corp.com/hooks/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
requests.post(SLACK_WEBHOOK, json={"text": f"Analytics export complete. {len(df)} records exported."})

print(f"Exported {len(df)} user records with full PII to /tmp/")
