import csv
import csv 

def read_csv(f):
	data = []
	with open(f,'r') as ff:
		csvread = csv.reader(ff, delimiter=',')
		for i in csvread:
			data.append(i)
	return data

def create_json(f):
	data = read_csv(f)[1:]
	regions = list(set(list(map(lambda x:x[0], data))))
	regions_dict = {}
	for region in regions:
		countries = []
		for i in data:
			if i[0] == region:
				countries.append({i[1]:i[-1]})
		temp = [countries, ','.join(countries)]
		regions_dict.update({region:temp})
	return regions_dict
			
