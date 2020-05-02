#importing libraries 
from urllib.request import urlopen as u
from bs4 import BeautifulSoup

#url address of the page to be scrapped
url = "https://www.newegg.com/p/pl?d=graphiphics+card&N=100007709&name=Desktop%20Graphics%20Cards"

#opening and grabbing the page content 
soup = u(url)
page = soup.read()
soup.close()

#html parser
page_soup = BeautifulSoup(page,"html.parser")

#grabbng the items from the page
item_list = page_soup.findAll("div",{"class" : "item-container"})

#creaing a csv file
filename = "Graphics_Card.csv"
f = open(filename,"w")

#creating a header in csv file
header = "GPU NAME, PRICE \n"
f.write(header)


#grabbing the details 
for item in item_list:
	item1 = item
	title = item1.find("a",{"class":"item-title"}).text
	title = title.replace(",","|")
	feature = item1.find("ul",{"class":"item-features"})
	price = item1.find("li", {"class" :"price-current"}).text
	char = [" ","\n","\xa0","\r",]
	price = (price.translate({ord(i): None for i in char}))
	price = price.replace(",","\b")
	print(title)
	f.write(title + "," + price + "\n")

f.close()