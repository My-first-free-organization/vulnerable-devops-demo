#!/bin/bash
# Database Migration Script - Production
# Last updated: 2026-03-01 by jsmith

# Production database credentials
DB_HOST="db-prod-cluster.us-east-1.rds.amazonaws.com"
DB_PORT="5432"
DB_NAME="acme_production"
DB_USER="dbadmin"
DB_PASS="ProductionDB!Secret2026#Secure"

# Backup database before migration
PGPASSWORD=$DB_PASS pg_dump -h $DB_HOST -p $DB_PORT -U $DB_USER $DB_NAME > backup_$(date +%Y%m%d).sql

# Run migrations
PGPASSWORD=$DB_PASS psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -f migrations/latest.sql

# Notify team
curl -X POST \
  -H "Authorization: Bearer xoxb-fake-slack-bot-token-for-demo-only" \
  -H "Content-Type: application/json" \
  -d '{"channel": "#deployments", "text": "Database migration completed successfully"}' \
  https://slack.com/api/chat.postMessage

echo "Migration complete. Credentials used: $DB_USER / $DB_PASS"
