
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://captionsgram.com/cricket-quotes-captions-for-instagram/').text

soup = BeautifulSoup(source, 'lxml')

hii= soup.find_all('div', attrs = {'entry-content clearfix'})
#hi=hii.ul.li.text
k=hii[0]
hi=k.ul.text
mm=hi.split('\n')
mm=mm[1:]

count =int(input("Enter the no. of quotes you want: "))
for i in range(0,len(mm)):
	print(mm[i])
	if (i+1)>=count:		
		break

