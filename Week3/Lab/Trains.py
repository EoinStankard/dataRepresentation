import requests
import csv
from bs4 import BeautifulSoup

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'xml')
#print (soup.prettify())
retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]

with open('week03_train.csv', mode='w') as train_file:
	train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	listings = soup.findAll("objTrainPositions")
	for listing in listings:
		#print(listing)
		#print(listing.TrainLatitude.string)
		lat =float( listing.TrainLatitude.string)
		if (lat < 53.4):
			entryList = []
			#entryList.append(listing.find('TrainLatitude').string)
			for retrieveTag in retrieveTags:
				#print (listing.find(retrieveTag).string)
				entryList.append(listing.find(retrieveTag).string)
			train_writer.writerow(entryList)


