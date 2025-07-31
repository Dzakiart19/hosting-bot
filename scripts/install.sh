#!/bin/bash
set -e

# --- Configuration ---
REPO_URL="https://github.com/user/repo.git" # CHANGE THIS to the actual repo URL
INSTALL_DIR="/opt/panelhost"

# --- Helper Functions ---
function print_info {
    echo -e "\e[34m[INFO]\e[0m $1"
}

function print_success {
    echo -e "\e[32m[SUCCESS]\e[0m $1"
}

function print_error {
    echo -e "\e[31m[ERROR]\e[0m $1"
    exit 1
}

# --- Pre-flight Checks ---
if [[ $EUID -ne 0 ]]; then
   print_error "This script must be run as root."
fi

# --- 1. Install Dependencies ---
print_info "Updating package lists..."
apt-get update

print_info "Installing dependencies: Docker, Docker Compose, Git, Certbot..."
apt-get install -y apt-transport-https ca-certificates curl software-properties-common git certbot

# Install Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io

# Install Docker Compose v2
COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d\" -f4)
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
docker compose version || print_error "Docker Compose installation failed."

# --- 2. Clone Repository ---
print_info "Cloning repository from ${REPO_URL} to ${INSTALL_DIR}..."
if [ -d "$INSTALL_DIR" ]; then
    print_info "Directory ${INSTALL_DIR} already exists. Pulling latest changes."
    cd "$INSTALL_DIR"
    git pull
else
    git clone "$REPO_URL" "$INSTALL_DIR"
    cd "$INSTALL_DIR"
fi

# --- 3. Configure Environment ---
print_info "Setting up environment file..."
if [ -f ".env" ]; then
    print_info ".env file already exists. Skipping creation."
else
    cp .env.example .env
    print_info ".env file created from .env.example. Please edit it now."
fi

# Prompt user to edit .env file
echo "Please edit the .env file with your specific configuration (BOT_TOKEN, DOMAIN, etc.)."
read -p "Press [Enter] to continue after editing..."

# --- 4. Initial SSL Certificate (for main domain) ---
# We need to get the initial certificate before starting the full stack
# so Nginx can start properly.
read -p "Enter your email address (for Let's Encrypt): " LETSENCRYPT_EMAIL
read -p "Enter your main domain (e.g., panelhost.my.id): " DOMAIN_NAME

print_info "Requesting initial SSL certificate for ${DOMAIN_NAME}..."
# Temporarily start a dummy nginx to solve the challenge
mkdir -p ./nginx/letsencrypt/www/.well-known/acme-challenge
docker run --rm -p 80:80 -v $(pwd)/nginx/letsencrypt/www:/var/www/certbot nginx:alpine &
NGINX_PID=$!
sleep 5 # wait for nginx to start

certbot certonly --webroot -w ./nginx/letsencrypt/www -d "${DOMAIN_NAME}" --email "${LETSENCRYPT_EMAIL}" --rsa-key-size 4096 --agree-tos --non-interactive --force-renewal

kill $NGINX_PID

# --- 5. Start the Application Stack ---
print_info "Starting the application stack with 'docker compose up -d'..."
docker compose up -d --build

print_success "Installation complete!"
print_info "The application stack is starting up. It may take a few minutes for all services to be ready."
print_info "You can check the status with 'docker compose ps' and view logs with 'docker compose logs -f'."
print_info "Remember to set up your wildcard SSL certificate and DNS records as per the documentation."
