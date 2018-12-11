import json
import csv
import sys
from pprint import pprint

reload(sys)
sys.setdefaultencoding('utf8')

with open('./SpotifyDataset/file1.json') as f:
    rawData = json.load(f)

with open('./SpotifyDataset/file2.json') as f:
    rawData1 = json.load(f)

with open('./SpotifyDataset/file3.json') as f:
    rawData2 = json.load(f)

with open('./SpotifyDataset/file4.json') as f:
    rawData3 = json.load(f)

allPlaylists = rawData["playlists"]
allPlaylists1 = rawData1["playlists"]
allPlaylists2 = rawData2["playlists"]
allPlaylists3 = rawData3["playlists"]

# code to put data into dictionaries if we want

# data = []
# results = []
# for i in range (0,len(allPlaylists)):
# 	playlist = {
# 		"collaborative": allPlaylists[i]["collaborative"],
# 		"num_tracks": allPlaylists[i]["num_tracks"],
# 		"num_albums": allPlaylists[i]["num_albums"],

# 	}
# 	data.append(playlist)
# 	results.append(allPlaylists[i]["num_followers"])

# open a file for writing

csv_data = open('./CSV/CSVData.csv', 'w+')
csv_data1 = open('./CSV/CSVData1.csv', 'w+')
csv_data2= open('./CSV/CSVData2.csv', 'w+')
csv_data3 = open('./CSV/CSVData3.csv', 'w+')

# create the csv writer object

csvwriter = csv.writer(csv_data)
csvwriter1 = csv.writer(csv_data1)
csvwriter2 = csv.writer(csv_data2)
csvwriter3 = csv.writer(csv_data3)

count = 0

for d in allPlaylists:
	del d["name"]
	del d["pid"]
	del d["modified_at"]
	del d["tracks"]
	if (d["collaborative"] == "false"):
		d["collaborative"] = 0
	else:
		d["collaborative"] = 1
	if d.has_key("description"):
		del d["description"]
	if count == 0:
		header = d.keys()

		csvwriter.writerow(header)
		count += 1
	csvwriter.writerow(d.values())

count = 0

for d in allPlaylists1:
	del d["name"]
	del d["pid"]
	del d["modified_at"]
	del d["tracks"]
	if (d["collaborative"] == "false"):
		d["collaborative"] = 0
	else:
		d["collaborative"] = 1
	if d.has_key("description"):
		del d["description"]
	if count == 0:
		header = d.keys()

		csvwriter1.writerow(header)
		count += 1
	csvwriter1.writerow(d.values())

count = 0

for d in allPlaylists2:
	del d["name"]
	del d["pid"]
	del d["modified_at"]
	del d["tracks"]
	if (d["collaborative"] == "false"):
		d["collaborative"] = 0
	else:
		d["collaborative"] = 1
	if d.has_key("description"):
		del d["description"]
	if count == 0:
		header = d.keys()

		csvwriter.writerow(header)
		count += 1
	csvwriter2.writerow(d.values())

count = 0

for d in allPlaylists3:
	del d["name"]
	del d["pid"]
	del d["modified_at"]
	del d["tracks"]
	if (d["collaborative"] == "false"):
		d["collaborative"] = 0
	else:
		d["collaborative"] = 1
	if d.has_key("description"):
		del d["description"]
	if count == 0:
		header = d.keys()

		csvwriter.writerow(header)
		count += 1
	csvwriter3.writerow(d.values())

csv_data.close()
csv_data1.close()
csv_data2.close()
csv_data3.close()

