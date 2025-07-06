import json
import argparse
import pandas as pd
from pandas import json_normalize

# Setup command-line arguments
parser = argparse.ArgumentParser(description='Flatten a nested JSON file and output as JSON or CSV.')
parser.add_argument('--format', choices=['json', 'csv'], default='csv', help='Output format: json or csv (default: csv)')
args = parser.parse_args()

# Load the nested JSON
with open('nested_json_demo.json', 'r') as f:
    nested_json = json.load(f)

# Flatten the structure
flat_df = json_normalize(
    nested_json,
    record_path='orders',
    meta=['id', ['user', 'name'], ['user', 'email'], ['user', 'address', 'city']],
    errors='ignore'
)

# Output as JSON
if args.format == 'json':
    flattened_json = flat_df.to_dict(orient='records')
    with open('flattened_json_demo.json', 'w') as f:
        json.dump(flattened_json, f, indent=4)
    print("Flattened data saved to 'flattened_json_demo.json'")

# Output as CSV
else:
    flat_df.to_csv('flattened_json_demo.csv', index=False)
    print("Flattened data saved to 'flattened_json_demo.csv'")
