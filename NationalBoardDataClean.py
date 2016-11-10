import csv
import re
import pandas as pd

#with open('/users/mwolff/desktop/NB/outputAL.csv','rb') as csvfile:
#	linereader = csv.reader(csvfile,delimiter=',')
#	for row in linereader:
#		match = re.findall('([A-Za-z ]+)',row)
#		print match




states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

names = []
details = []
cert = []
loc = []
valid = []
achieved = []

for s in states:
	f = open('/users/mwolff/desktop/NB/output' + s + '.csv','r')
	reader =  f.read()
	reader = reader.replace('[u\'','').replace('\']','').replace('\\r','').replace('\r\n','\\n').replace("\"",'').split('\\n')



	numObs = len(reader)/6
	for i in range(0,numObs):
		names.append(reader[i*6])
		details.append(reader[i*6+1])
		cert.append(reader[i*6+2])
		loc.append(reader[i*6+3])
		valid.append(reader[i*6+4])
		achieved.append(reader[i*6+5])

dataset = pd.DataFrame(
	{'Names': names,
	'Details': details,
	'Certification': cert,
	'Location': loc,
	'Valid Until': valid,
	'Achieved by': achieved
	})


dataset.to_csv('/users/mwolff/desktop/NB/outputClean.csv')