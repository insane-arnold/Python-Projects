#importing libraries 
from urllib.request import urlopen as u
from bs4 import BeautifulSoup

#url address of the page to be scrapped
#lyrics is scapped from www.azlyrics.com 

#url = "https://www.azlyrics.com/lyrics/script/breakeven.html"
url = input("Enter the url: ")


#opening and grabbing the page content 
soup = u(url)
page = soup.read()
soup.close()

#html parser
page_soup = BeautifulSoup(page,"html.parser")

#grabbing the lyrics

All_div = page_soup.findAll("div")
lyrics = All_div[10].text

#saving in a text file 

filename = "lyrics.text"

f = open(filename,"w")
f.write(lyrics)
f.close