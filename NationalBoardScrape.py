from bs4 import BeautifulSoup
import requests
import csv

def genTable(webpage):
	r = requests.get(page)
	data = r.text
	soup = BeautifulSoup(data,'html.parser')
	#Get Table
	table = soup.find('table', {'class': 'views-view-grid cols-1'})
	if table is None:
			stopCriterion = 1
	else:	
		table_body = table.find('tbody')
		rows = table_body.find_all('tr')
		for row in rows:
		    cols = row.find_all('td')
		    cols = [ele.text.strip() for ele in cols]
		    tab.append([ele for ele in cols if ele]) # Get rid of empty values
		stopCriterion = 0
	return(stopCriterion)
#'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA',
states = ['WA','WV','WI','WY']

for s in states:
	resultFile = open("output" + s + ".csv",'wb')
	wr = csv.writer(resultFile, dialect='excel')

	tab = []

	for i in range(0,1000000): #High number to ensure all pages hit
		if i == 0:
			page = "http://www.nbpts.org/nbct-search?first_name=&last_name=&school_state=" + s + "&district=&certificate_area=&date_achieved="
		if i != 0:
			page = "http://www.nbpts.org/nbct-search?first_name=&last_name=&school_state=" + s + "&district=&certificate_area=&date_achieved=&page=" + str(i)
		result = genTable(page)
		print("Page " + str(i) + " Finished")
		if result == 1:
			print("All Pages Finished for " + s)
			break

	print(str(len(tab)) + "Entries in Total for " + s)

	for item in tab:
	     wr.writerow([item,])