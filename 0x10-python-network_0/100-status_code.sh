#!/bin/bash
# sends request to a URL, Display only the status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
