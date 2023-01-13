#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Copy script to /bin
sudo cp ./chatgpt-cli.py /bin/chatgpt-cli

# Make script executable
sudo chmod +x /bin/chatgpt-cli
