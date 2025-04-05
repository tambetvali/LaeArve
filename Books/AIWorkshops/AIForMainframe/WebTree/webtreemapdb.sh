#!/bin/bash
# How to run:
#   1. Save this script as "run_webtreemap.sh" in the same folder as webtreemap.py.
#   2. Make the script executable by running:
#         chmod +x run_webtreemap.sh
#   3. Execute the script:
#         ./run_webtreemap.sh
#
# # MongoDB Checker, Installer, and Runner Script
#
# This script checks whether MongoDB is installed and running on your Ubuntu system.
#
# 1. **Check MongoDB Installation:**
#    - It verifies if the `mongod` command exists.
#    - If not found, the script prompts you to install MongoDB.
#    - Since the package `mongodb` is no longer available, the script sets up the official MongoDB
#      repository for your Ubuntu release and installs `mongodb-org`.
#
# 2. **Check MongoDB Service Status:**
#    - After installation (or if MongoDB is already installed), it checks whether the MongoDB service is active.
#    - If the service is not running, it attempts to start it.
#
# 3. **Run the Python Project:**
#    - Once MongoDB is confirmed running, the script executes the Python file "webtreemap.py" in the current folder.
#
# **Note:**
# - This script is intended for Debian/Ubuntu systems.
# - Sudo privileges are required as the script will add the repository, install packages, and start services.
# - This script uses the official MongoDB Community Edition (6.0 as of writing); adjust the version if needed.
#
# ----------------- Step 1: Check for MongoDB Installation ---------------------
if ! command -v mongod >/dev/null 2>&1; then
    echo "MongoDB (mongod) is not installed on this system."
    read -p "Do you want to install MongoDB (mongodb-org)? (y/n): " answer
    if [[ $answer =~ ^[Yy]$ ]]; then
        # Determine the Ubuntu release codename (e.g. focal, jammy)
        release=$(lsb_release -sc)
        echo "Detected Ubuntu release: $release"
        echo "Adding the official MongoDB repository for Ubuntu $release..."
        # Import the MongoDB public GPG Key
        wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
        # Create the list file for MongoDB
        echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $release/mongodb-org/6.0 multiverse" | \
            sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
        echo "Updating the package database..."
        sudo apt-get update
        echo "Installing mongodb-org..."
        sudo apt-get install -y mongodb-org
        if [ $? -ne 0 ]; then
            echo "Installation of mongodb-org failed. Please check the repository settings and try again."
            exit 1
        fi
    else
        echo "MongoDB installation was declined. Exiting."
        exit 1
    fi
else
    echo "MongoDB (mongod) is already installed on this system."
fi

# ----------------- Step 2: Check and Start MongoDB Service ---------------------
service_status=$(systemctl is-active mongod 2>/dev/null)
if [ "$service_status" != "active" ]; then
    echo "MongoDB service is not running."
    echo "Attempting to start the MongoDB service..."
    sudo systemctl start mongod
    sleep 2
    service_status=$(systemctl is-active mongod 2>/dev/null)
    if [ "$service_status" == "active" ]; then
        echo "MongoDB service started successfully."
    else
        echo "Failed to start the MongoDB service. Please start it manually and re-run the script."
        exit 1
    fi
else
    echo "MongoDB service is already running."
fi

# ----------------- Step 3: Run the Python Project File ---------------------
echo "Running the Python script 'webtreemap.py'..."
python3 ./webtreemap.py
