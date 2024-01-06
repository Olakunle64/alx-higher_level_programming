#!/bin/bash
# display only the status code of a response
curl -s -o /dev/null -w '%{http_code}' "$1"
