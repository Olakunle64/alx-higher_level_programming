#!/bin/bash
# Display the body of a 200 ok response
#[ "$(curl -s -o /dev/null -w '%{http_code}' "$1")" -eq 200 ] && body=$(curl -s "$1");echo -n "$body"
curl -s -o '%{http_code}' "$1"
