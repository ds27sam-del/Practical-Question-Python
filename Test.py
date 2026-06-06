import requests

# 1. Define the API endpoint URL
url = "https://itunes.apple.com/search"

# 2. Set up the parameters for your GET request
# This tells the API exactly what we are looking for
params = {
    "term": "Satinder Sartaaj",
    "media": "music",
    "limit": 3  # We only want the top 3 results
}

print(f"Sending request to {url}...\n")

# 3. Make the request to the "waiter"
response = requests.get(url, params=params)

# 4. Check the Status Code (200 OK means it worked)
if response.status_code == 200:
    # 5. Parse the raw JSON response into a Python dictionary
    data = response.json()
    
    print("Success! Here is the data we got back:\n")
    
    # 6. Loop through the results and print specific pieces of data
    for track in data['results']:
        song_name = track['trackName']
        album_name = track['collectionName']
        print(f"🎶 Song: {song_name} | Album: {album_name}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")