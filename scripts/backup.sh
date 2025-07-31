#!/bin/bash
set -e

# --- Configuration ---
# These should ideally be loaded from the .env file
# For simplicity in a cronjob, they are defined here.
# Ensure this script has restricted permissions (chmod 700).
POSTGRES_USER="panel"
POSTGRES_DB="panelhost"
POSTGRES_HOST="panelhost_postgres" # The service name in docker-compose
MINIO_ALIAS="minio_backup"
MINIO_BUCKET="backups" # The bucket name inside MinIO
MINIO_ENDPOINT="http://localhost:9000" # MinIO endpoint
MINIO_ACCESS_KEY="admin" # MINIO_ROOT_USER from .env
MINIO_SECRET_KEY="a_strong_and_secret_password" # MINIO_ROOT_PASSWORD from .env

# Backup directory on the host
BACKUP_DIR="/opt/panelhost/backups"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
FILENAME="${POSTGRES_DB}_${DATE}.sql.gz"
FILEPATH="${BACKUP_DIR}/${FILENAME}"

# --- Main Logic ---
echo "Starting database backup for ${POSTGRES_DB}..."

# Ensure backup directory exists
mkdir -p "$BACKUP_DIR"

# 1. Dump the database from the running container
# We use docker exec to run pg_dump inside the postgres container
docker exec "$POSTGRES_HOST" pg_dump -U "$POSTGRES_USER" -d "$POSTGRES_DB" | gzip > "$FILEPATH"

echo "Database dump created successfully at ${FILEPATH}"

# 2. Upload to MinIO
# This requires the MinIO client (mc) to be installed on the host.
# The install.sh script should be updated to include it.
# For now, this is a placeholder for the upload command.
#
# Assumes 'mc' is configured. Example:
# mc alias set ${MINIO_ALIAS} ${MINIO_ENDPOINT} ${MINIO_ACCESS_KEY} ${MINIO_SECRET_KEY}
# mc cp "${FILEPATH}" "${MINIO_ALIAS}/${MINIO_BUCKET}/"

echo "Uploading ${FILENAME} to MinIO bucket '${MINIO_BUCKET}'..."
# Placeholder for upload logic
# In a real scenario, you would use 'mc' or an S3 SDK.
echo "[SIMULATED] Upload complete."

# 3. Clean up old local backups (e.g., older than 7 days)
echo "Cleaning up old local backups..."
find "$BACKUP_DIR" -type f -name "*.sql.gz" -mtime +7 -exec rm {} \;

echo "Backup process finished successfully."
