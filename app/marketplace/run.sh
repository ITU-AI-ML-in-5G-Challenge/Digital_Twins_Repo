#!/bin/bash
  
# turn on bash's job control
set -m

# Start the first process
# npx hardhat node &
  
# Start the second process (depends on the first one)
npx hardhat run scripts/deploy.js --network besu 
  
# now we bring the primary process back into the foreground
# and leave it there
# fg %1

#  Run the app
# node ./marketplace.mjs &

# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?