#!/bin/bash
# Script that makes a curl and displays the size of the body
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
