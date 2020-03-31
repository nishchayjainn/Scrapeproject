from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://wisdomquotes.com/life-quotes/').text

soup = BeautifulSoup(source, 'lxml')
hii=soup.find_all('blockquote')
count =int(input("Enter the no. of quotes you want: "))
for i in range(0,len(hii)):
	print((hii[i]).text)
	if (i+1)>=count:
		break
