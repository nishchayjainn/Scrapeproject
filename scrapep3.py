from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.briantracy.com/blog/personal-success/26-motivational-quotes-for-success/').text

soup = BeautifulSoup(source, 'lxml')
hii=soup.find_all("h3")
count =int(input("Enter the no. of quotes you want: "))
for i in range(0,len(hii)):
	print((hii[i]).text)
	if (i+1)>=count:
		break










#count =int(input("Enter the no. of quotes you want: "))
#for i in range(0,len(hii)):
#	print((hii[i]).text)
#	if (i+1)>=count:
#		break










