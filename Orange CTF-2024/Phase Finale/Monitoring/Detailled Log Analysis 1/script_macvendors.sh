#!/bin/bash

# Checks whether a file has been specified as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

# Read MAC addresses from the file
while read -r mac; do
    # take the first three bytes (OUI) of the MAC address
    oui=$(echo $mac | awk -F: '{print $1, $2, $3}' | tr ' ' ':')

    # Use API to get manufacturer info
    results=$(curl -s "https://api.macvendors.com/$oui")

    echo "$oui : $results"
done < "$1"
