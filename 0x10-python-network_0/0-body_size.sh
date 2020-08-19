#!/bin/bash
# Script that makes a curl and displays the size of the body
curl -sI $1 | grep "Content-Length" | cut -d ' ' -f 2
