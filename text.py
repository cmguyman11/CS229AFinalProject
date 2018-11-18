import json
import csv
import sys
from pprint import pprint

reload(sys)
sys.setdefaultencoding('utf8')

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

# open a file for writing

csv_data = open('./CSVData.csv', 'w+')

# create the csv writer object

csvwriter = csv.writer(csv_data)

count = 0

for d in allPlaylists:
	del d["name"]
	del d["pid"]
	del d["modified_at"]
	del d["tracks"]
	if d.has_key("description"):
		del d["description"]
	if count == 0:
		header = d.keys()

		csvwriter.writerow(header)
		count += 1
	csvwriter.writerow(d.values())

csv_data.close()

