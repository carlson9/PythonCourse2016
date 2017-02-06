# Go to https://petitions.whitehouse.gov/petitions 
# Go to the petition page for each of the petitions. 
# Create a .csv ﬁle with the following information for each petition: 
 ### – Title 
 ### – Published date 
 ### – Issues 
 ### – Number of signatures
 
from bs4 import BeautifulSoup
import urllib2
import csv 
from urlparse import *
import random
import time
import os
import re
from django.utils.encoding import smart_str, smart_unicode

# the entry on row 27 is messed up, still trying to troubleshoot why it's happening

# function to save petitions' info into csv
def save_petitions(website):
	with open('HW2_petitions.csv', 'wb') as f:
		my_writer = csv.DictWriter(f, fieldnames = ("Title", "PublishedDate", "Issues", "Signatures"))
		my_writer.writeheader()

		Titles, Dates, Issues, Signatures = scrape_petitions(website)

		for i in range(len(Titles)):
			my_writer.writerow({"Title":Titles[i], "PublishedDate": Dates[i], "Issues": Issues[i], "Signatures": Signatures[i]})

# function to scrape the petitions' info			
def scrape_petitions(website):
	Headers, Issues, Signatures = get_headers_issues_signatures(website)
	Links, Titles = get_links_titles(Headers)
	Dates = get_dates(Links)
	return Titles, Dates, Issues, Signatures			

# function to get issues and signatures for petitions	
def get_headers_issues_signatures(website):
	Headers = []
	All_Issues = []
	Issues = []
	Signatures = []
	for i in range(4):
		web_page = urljoin(str(website), '?page=%d' % i)
		web_text = urllib2.urlopen(web_page)
		soup = BeautifulSoup(web_text.read())
		Headers.extend(soup.find_all('h3'))
		sigs = soup.find_all('span', {'class': 'signatures-number'})
		for sig in sigs:
			Signatures.append(str(sig.get_text()))
		all_issues = soup.find_all('div', {'class': "field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags"})
		for issue in all_issues:
			All_Issues.append(issue.find_all('h6'))
		for List in All_Issues:
			issues = []
			for issue in List:
				issues.append(str(issue.get_text()))
			Issues.append(issues)
	Issues = Issues[-74:]
	return Headers, Issues, Signatures
			
# function to get dates for petitions
def get_dates(Links):
	Dates = []
	for link in Links:
		web_text = urllib2.urlopen(link)
		soup = BeautifulSoup(web_text.read())
		attrib = soup.find_all('h4', {'class': 'petition-attribution'})
		text_att = str(attrib[0].get_text())
		words = text_att.split()
		Dates.append(' '.join(words[-3:]))
	return Dates

# function to get links and titles of the petitions	
def get_links_titles(petitions):
	Links = []
	Titles = []
	for petition in petitions:
		try:
			extension = petition.a['href']
		except:
			continue
		else:
			Titles.append(smart_str(petition.a.get_text()))
			Links.append(urljoin("https://petitions.whitehouse.gov", str(extension)))
	return Links, Titles			
			
web_address = 'https://petitions.whitehouse.gov/petitions'
save_petitions(web_address)			
			
			
			
			
			
			
			
			
			
			