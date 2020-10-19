#!/bin/bash
echo "Enter Network Address First 3 Octets"
read net
namp -sV $net.0/24 --version-light -O -oN nmapVER.txt
