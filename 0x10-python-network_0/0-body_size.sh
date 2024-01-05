#!/usr/bin/env bash
# Write a Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response and the size must be in byte

if [ "$#" -gt 0 ]; then
	url=$1
	serverResponse=$(curl -sI "$url" 2>&1)
	if [ "$?" -eq 0 ]; then
		len=$(echo "$serverResponse" | grep "Content-Length" | grep -o '\b[0-9]\+\b')
		echo "$len"
	else
		echo "Error"
	fi
else
	echo "USAGE: <filename> <url>"
fi
