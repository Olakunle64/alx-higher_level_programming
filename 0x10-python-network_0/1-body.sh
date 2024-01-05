#!/bin/bash
# Display the body of a 200 ok response
#!/bin/bash
[ "$(curl -s -o /dev/null -w '%{http_code}' "$1")" -eq 200 ] && curl -s "$1"
