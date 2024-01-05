#!/usr/bin/env bash
# Write a Bash script that takes in a URL, sends a request to that URL,
	serverResponse=$(curl -sI "$1" 2>&1);len=$(echo "$serverResponse" | grep "Content-Length" | grep -o '\b[0-9]\+\b'); echo "$len"
