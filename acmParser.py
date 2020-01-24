import bibtexparser
import csv

with open('exports/ACM/acm.bib') as bibfile:
	data = bibtexparser.load(bibfile)

with open('output.csv', 'a') as fp:
	for i in range(0, len(data.entries)):
		row = data.entries[i]['title']+ ',' + data.entries[i]['year'] + ',' + '"'+ data.entries[i]['author'] + '"'
		if(data.entries[i]['ENTRYTYPE'] == 'inproceedings'):
			row = row + ',' + data.entries[i]['series']+'\n'
		else:
			row = row + ',' + data.entries[i]['journal']+'\n'	
		fp.write(str(row))

