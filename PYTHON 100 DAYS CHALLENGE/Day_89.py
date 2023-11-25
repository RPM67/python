import requests
from bs4 import BeautifulSoup


url = "https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/"
response = requests.get(url) # it will store the raw  html code of the website whose link is provided in url as request element
print(response.text)  # it will print the raw html code of the website stored in response by converting it to text



soup = BeautifulSoup(response.text, 'html.parser') # it will parse the raw html code stored as 'response.text' from response and will
print()                                             # parse it to make that raw html code to make it readable and understandable 
print(soup.prettify())  # pretify() will convert the html code in soup into string and make it look like real written html code just
                        # in same way it will look like in any IDE while writing that html code
print()                        
for title in soup.find_all("title"): # 'soup.find_all("h2")' will find the title from that html code and store it in 'title' variable
  print(title.text)
  

# the 'requests' and 'bs4' module is very much helpful in parsing any website and performing or searching any data inside html code 
# of those websites with accuracy. we can know how many h1,h2,... headings are used in making that website or know the title of
# that website or any data like this easily.