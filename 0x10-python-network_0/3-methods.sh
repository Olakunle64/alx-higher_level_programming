#!/bin/bash
# list all available request methods available on the server
methods=$(curl -si -X OPTIONS "$1" | awk '/Allow:/ {print $2, $3, $4}'); echo "$methods"
