
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.keepinspiring.me/positive-inspirational-life-quotes/').text

soup = BeautifulSoup(source, 'lxml')

hii= soup.find_all('div', attrs = {'author-quotes'})
#hi=hii.ul.li.text
count =int(input("Enter the no. of quotes you want: "))
for i in range(0,len(hii)):
	print((hii[i]).text)
	if (i+1)>=count:
		break
