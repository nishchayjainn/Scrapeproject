from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.themuse.com/advice/45-inspirational-quotes-that-will-get-you-through-the-work-week').text
soup = BeautifulSoup(source, 'lxml')
hi=soup.find_all("h3")
count =int(input("Enter the no. of quotes you want: "))
for i in range(0,len(hi)):
	print((hi[i]).text)
	if (i+1)>=count:
		break
