import json
from pprint import pprint

with open('./SpotifyDataset/file1.json') as f:
    rawData = json.load(f)

allPlaylists = rawData["playlists"]

data = []
results = []
for i in range (0,len(allPlaylists)):
	playlist = {
		"collaborative": allPlaylists[i]["collaborative"],
		"num_tracks": allPlaylists[i]["num_tracks"],
		"num_albums": allPlaylists[i]["num_albums"],

	}
	data.append(playlist)
	results.append(allPlaylists[i]["num_followers"])

print(data)
print(results)