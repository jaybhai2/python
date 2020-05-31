 ### breadth first search
```
import requests
from bs4 import BeautifulSoup
from collections import deque

visited = set(["http://toscrape.com"])
dq = deque([["http://toscrape.com", "", 0]])
max_depth = 2


while dq:
    base, path, depth = dq.popleft()
    #                         ^^^^ removing "left" makes this a DFS (stack)

    if depth < max_depth :
        try:
            soup = BeautifulSoup(requests.get(base + path).text, "html.parser")

            for link in soup.find_all("a"): 
                href = link.get("href")

                if href not in visited:
                    visited.add(href)
                    print("  " * depth + f"at depth {depth}: {href}")

                    if href.startswith("http"):
                        dq.append([href, "", depth + 1])
                    else:
                        dq.append([base, href, depth + 1])
                
        
        except:
            pass

    print(str(dq))
 ```
 ### Depth First Search
 ```
 import requests
from bs4 import BeautifulSoup

def get_links_recursive(base, path, visited, max_depth=3, depth=0):
    if depth < max_depth:
        try:
            soup = BeautifulSoup(requests.get(base + path).text, "html.parser")

            for link in soup.find_all("a"):
                href = link.get("href")

                if href not in visited:
                    visited.add(href)
                    print(f"at depth {depth}: {href}")

                    if href.startswith("http"):
                        get_links_recursive(href, "", visited, max_depth, depth + 1)
                    else:
                        get_links_recursive(base, href, visited, max_depth, depth + 1)
        except:
            pass


get_links_recursive("http://toscrape.com", "", set(["http://toscrape.com"]))			

 ```
