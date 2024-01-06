#!/bin/bash
# list all available request methods available on the server
curl -si -X OPTIONS "$1" | awk -F ": " '/Allow/ {print $2}'
