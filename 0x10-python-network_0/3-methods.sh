#!/bin/bash
# list all available request methods available on the server
curl -i -X OPTIONS "$1"
