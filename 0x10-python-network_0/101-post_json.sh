#!/bin/bash
# Sends a JSON POST request to a URL, display the response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
