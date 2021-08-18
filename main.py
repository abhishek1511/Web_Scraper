import requests
from bs4 import BeautifulSoup

url = "https://www.lipsum.com"

#Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#creating a soup
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup)

#Tree Traversal

title = soup.title
#print(title)
#print(type(soup))
#print(type(title))
#print(type(title.string))

#get all the paragraphs from the page
paras = soup.find_all('p')
#print(paras)

"""
#get all the anchor from the page
anchor = soup.find_all('a')
print(anchor)
#create an empty set
all_links = set()
#get all the links from the page
for link in anchor:
    #print(link.get('href'))
    if(link.get('href') != '#'):
        linkText = "https://www.lipsum.com" + link.get('href')
        all_links.add(linkText)
        print(linkText)
"""


#get first element in the HTML
#print(soup.find('p'))

#get the classes of any element in the HTML page
#print(soup.find('p')['class'])

#find all the elements with class lead
#print(soup.find_all("p",class_="lead"))

#get the text from the tags/soup
#print(soup.find('p').get_text())
#get all the text from the page
#print(soup.get_text())

"""
#Comment type:
markup1 = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup1)
print(type(soup2.p.string))
"""


#.contents - A tag's children are available as a list - all elements will be stored in a memory
#.childer - A tag's children are available as a generator - it cannot be stored in memory but it can be access anytime by iternating it


Content = soup.find(id='Packages')
"""
print(Content.contents)
print("Content.contents :-->")
for element in Content.contents:
    print(element)
print("Content.children :-->")
for element in Content.children:
    print(element)
print("Content.strings :--> ")
for element in Content.strings:
    print(element)
print("Content.stripped_strings :--> ")
for element in Content.stripped_strings:
    print(element)
print("Content.parent :--> ")
print(Content.parent)
print("Content.parents :--> ")
print(Content.parents)


print("Content.parents iterate the generator  :--> ")
for element in Content.parents:
    #print(element)
    print(element.name)

"""


#while using previous/next siblings, all the space and newline also come into consideration
print("1",Content.next_sibling)
print("2",Content.next_sibling.next_sibling)
print("3",Content.previous_sibling)
print("4",Content.previous_sibling.previous_sibling)

