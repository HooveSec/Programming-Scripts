#!/bin/bash
echo "Enter Network Address First 3 Octets"
read net
for i in {1..254} ;do (ping -c 1 $net.$i | grep "bytes from" &) ;done

