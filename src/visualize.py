#!/usr/bin/env python3
import argparse
import os
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from collections import Counter, defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--percent', action='store_true')
args = parser.parse_args()

with open(args.input_path) as f:
    counts = json.load(f)

if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

items = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]), reverse=True)[:10]
sorted_items = sorted(items, key=lambda item: item[1])

# Split the items into keys and values for plotting
keys, values = zip(*sorted_items)

# Generate the bar graph
plt.figure(figsize=(10, 8))
# Create a range for the x-axis positions
x_pos = range(len(keys))

# Plot the bars at numeric positions
plt.bar(x_pos, values, color='red' if args.input_path.endswith('.lang') else 'darkblue')  # Use red for language graphs and dark blue for country graphs

# Now set the x-axis ticks and labels to correspond to your keys
plt.xticks(x_pos, keys)

# Determine x-axis label based on file extension
file_extension = os.path.splitext(args.input_path)[1]
if file_extension == '.lang':
    plt.xlabel('Language')
elif file_extension == '.country':
    plt.xlabel('Country')

plt.ylabel('Number of Tweets')

plt.title('Top 10 ' + ('Languages' if file_extension == '.lang' else 'Countries') + ' by Number of Tweets')

plt.xticks(rotation=45)

# Sanitize the hashtag for use in the filename (remove # and replace spaces/invalid characters if any)
safe_hashtag = args.key.replace('#', '').replace(' ', '_').replace('/', '_')

# Determine output filename based on input file extension and include the sanitized hashtag
base_name = os.path.splitext(args.input_path)[0]
file_extension = '.png'
if args.input_path.endswith('.lang'):
    output_suffix = f'_{safe_hashtag}_language_distribution'
elif args.input_path.endswith('.country'):
    output_suffix = f'_{safe_hashtag}_country_distribution'
else:
    output_suffix = f'_{safe_hashtag}_data_distribution'

output_path = f"{base_name}{output_suffix}{file_extension}"

# Save the figure as a PNG file
plt.savefig(output_path)

# Print path of the saved graph as a confirmation
print(f'Bar graph saved as: {output_path}')
