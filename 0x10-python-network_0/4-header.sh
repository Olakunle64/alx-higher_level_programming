#!/bin/bash
# send a GET request with a particular header
curl -s -H "X-School-User-Id: 98" "$1"
