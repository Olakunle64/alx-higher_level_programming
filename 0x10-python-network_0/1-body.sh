#!/bin/bash
# Display the body of a 200 ok response
statusCode=$(curl -sI "$1" | awk '/HTTP/ {print $2}') && [ "$statusCode" -eq 200 ] && curl -s "$1"
