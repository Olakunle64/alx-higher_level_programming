#!/bin/bash
# Display the body of a 200 ok response
body=$(curl -s "$1") && echo "$body"

