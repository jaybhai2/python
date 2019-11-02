import bs4, requests
#web scrpe google finance data.

def getPrice(url,CSSselector):
    response  = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    elems = soup.select(CSSselector)
    print(type(elems))
    return elems[0].text.strip()

url = 'https://finance.yahoo.com/'
selector = ''
response  = requests.get(url)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'html.parser')


print(soup.find_all('title'))

print(soup.find_all('a',attrs={'title':"S&amp;P 500"}))



'''---------------use list generator to navigate layer by layer--------------
[print(type(item)) for item in list(soup.children)]    # child element at next level  

html = list(soup.children)[1]       # the html page which has children of header and body  

#header and body 
header = list(html.children)[0]         
body = list(html.children)[1]

print(len(body))
div1 = list(body.children)[1]      #first div elememt of the body , [0] is a iframe object
print(body1)

'''








# SPX = getPrice(url,selector)
# print(SPX)
# knowledge-finance-wholepage__entity-summary > div > div > g-card-section:nth-child(2) > div > div > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.iyjjgb