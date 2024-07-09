#!/usr/bin/env bash
# Bash script that takes url and display the size of the body
curl -is $1| grep -i Content-Length: | awk '{print $2}' | tr -d ' '