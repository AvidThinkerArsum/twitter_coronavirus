#!/usr/bin/env python3
import argparse
import os
import json
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')  # Ensure matplotlib does not use any Xwindows backend
import matplotlib.pyplot as plt
import datetime

# Set up command line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('hashtags', nargs='+', help='List of hashtags to analyze, include the "#" symbol')
args = parser.parse_args()

# Initialize data structure for counts
counts_by_day = defaultdict(lambda: defaultdict(int))

# Define path to data folder
outputs_folder = 'outputs'

# List all relevant data files
data_files = [f for f in os.listdir(outputs_folder) if f.endswith('.zip.lang')]

# Process each data file
for file in data_files:
    # Extract date from filename
    date_str = file[10:18]  # Assumes format 'geoTwitterYY-MM-DD.zip.lang'
    date_obj = datetime.datetime.strptime(date_str, '%y-%m-%d').date()

    # Load data from file
    with open(os.path.join(outputs_folder, file), 'r') as f:
        data = json.load(f)

        # Process each specified hashtag
        for hashtag in args.hashtags:
            hashtag = hashtag.lower()  # Assuming hashtags in data are lowercase
            # Aggregate counts across all languages for this hashtag
            total_count = sum(data.get(hashtag, {}).values())
            counts_by_day[hashtag][date_obj] = total_count

# Generate a filename based on the specified hashtags
# Join the cleaned hashtags with underscores and limit the total length to avoid overly long filenames
filename_base = "_".join(hashtag.strip('#').lower() for hashtag in args.hashtags)[:50]
filename = f"hashtag_trends_{filename_base}.png"

# Plotting
plt.figure(figsize=(10, 6))

# Generate a list of all dates for the x-axis
all_dates = sorted(set(date for _, dates in counts_by_day.items() for date in dates))

for hashtag, counts in counts_by_day.items():
    # Prepare data for plotting
    y_values = [counts.get(date, 0) for date in all_dates]
    plt.plot(all_dates, y_values, label=hashtag)

# Formatting the plot
plt.xlabel('Day of the Year')
plt.ylabel('# of Tweets for Hashtag')
plt.title('Tweet Counts by Hashtag Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot with the dynamic filename
plt.savefig(filename)
print(f'Plot saved as {filename}')
