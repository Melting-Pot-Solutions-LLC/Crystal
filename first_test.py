#%%
import json
import requests


user_key = '43238a383541231cf82870fad6691fd0'
url = 'https://api.social-searcher.com/v2/search?q="obama"&lang=en&limit=100&network=web&key=43238a383541231cf82870fad6691fd0'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    posts = data['posts']    	
    sentiments = [ post['sentiment']  for post in posts if 'sentiment' in post]
    # print(json.dumps(posts, indent=4))
    # print(f"number of posts = {len(posts)}")
    print(response)
else:
	print(f"Error fetching data: {response.status_code} - {response.text}")

# %%
