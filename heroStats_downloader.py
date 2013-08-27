import urllib2
import json
import csv

def getRows(data):
	final_list = []
	for entry in data:
		hero = data[entry]
		stats = hero.values()
		final_list.append(stats)
	return final_list

url = 'http://dotaheroes.herokuapp.com/heroes/all'
data = urllib2.urlopen(url).read()
data = json.loads(data)

def main():
	filename = "heroStats.csv"
	with open(filename, 'wb') as output:
		outcsv = csv.writer(output)
		outcsv.writerows(getRows(data))

if __name__ == '__main__':
	main()

