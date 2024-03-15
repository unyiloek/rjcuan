#!/bin/sh
if [ -z "$STY" ]; then exec screen -dm -S budal /bin/bash "$0"; fi
chmod +x budal.sh
./budal.sh