#!/bin/bash

# Loop over each zip file in the dataset directory from the year 2020
for file in /data/Twitter\ dataset/geoTwitter20-*.zip; do
    echo "Processing file: $file"
    # Run the map.py script in the background for each file
    # Redirect stdout and stderr to a log file specific to the file being processed
    nohup python3 ./src/map.py --input_path="$file" >/dev/null 2>&1 &
done

# Wait for all background jobs to finish
wait

echo "All files have been processed."

