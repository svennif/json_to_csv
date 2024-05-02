import pandas as pd
import json

# Load the JSON file
with open('shareable_demo_feed.json') as f:
  data = json.load(f)

# Flatten the data and load it into a DataFrame
df = pd.json_normalize(data)

# Write the DataFrame to a CSV file
df.to_csv('shareable_demo_feed.csv', index=False)