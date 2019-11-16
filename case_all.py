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
		countries_names =[]
		for i in data:
			if i[0] == region:
				countries.append({i[-1].split(',')[0]:i[1]})
				countries_names.append(i[-1].split(',')[0])
		temp = [countries, ','.join(countries_names)]
		regions_dict.update({region:temp})
	return regions_dict
			
