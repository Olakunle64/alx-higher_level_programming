#!/bin/bash
# Display the body of a 200 ok response
statusCode=$(curl -s -o /dev/null -w '%{http_code}' "$1") && [ "$statusCode" -eq 200 ] && curl -s "$1"
