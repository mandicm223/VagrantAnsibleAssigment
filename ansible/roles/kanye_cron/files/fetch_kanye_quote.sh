#!/bin/bash

# Directory to save quotes
OUTPUT_DIR="/var/log/kanye_quotes"
mkdir -p "$OUTPUT_DIR"

# Fetch JSON and save to a file with a timestamp
curl -s https://api.kanye.rest | jq '.' > "${OUTPUT_DIR}/quote_$(date +"%Y-%m-%d_%H").json"
