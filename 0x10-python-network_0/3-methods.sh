#!/bin/bash
# list all available request methods available on the server
methods=$(curl -si -X OPTIONS "$1" | awk '/Allow:/ {print $2, $3, $4, $5, $6, $7, $8, $9, $10}'); echo "$methods"
