#!/bin/bash
# list all available request methods available on the server
curl -si -X OPTIONS "$1" | grep "Allow" | awk -F ": " '{print $2}'
