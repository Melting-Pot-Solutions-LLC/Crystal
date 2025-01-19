import json
import requests
import pandas as pd

user_key = '43238a383541231cf82870fad6691fd0'
base_url = 'https://api.social-searcher.com/v2/search'
output_file = 'output.csv'

search_terms = [
    "Intellectual Disability Individuals with Disabilities Education Act",
    "Intellectual Disability IDEA",
    # other search terms continue ...
    "Fragile X school services"
]

# Initialize a dictionary to store the results
results = []

for term in search_terms:
    params = {
        'q': term,
        'lang': 'en',
        'limit': 10,  # Change this if you want more results
        'network': 'web',
        'key': user_key
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('posts', [])

        for post in posts:
            source = post.get('network', 'Unknown')
            link = post.get('url', 'No URL')
            results.append([term, source, link])
    else:
        print(f"Error fetching data for {term}: {response.status_code} - {response.text}")

# Convert to DataFrame for ease of CSV creation
df = pd.DataFrame(results, columns=['Search Term', 'Source', 'Link'])

# Save to CSV
df.to_csv(output_file, index=False)

print(f"Data saved to {output_file}")
