import urllib.request
from bs4 import BeautifulSoup
import pandas as pd 



def url_digger (url, header):
    """Return text and the links from the google search result. 

    Args: 
        url (string): URL of the page to scrape (which we designed it with google_search function).

    Returns:
        response (df): storing th links and text plus the query in DataFrame. 
    """

    result = { 'what you searched': [], 'title and snippet':[], 'links': [] }


    # requesting HTML of the page and using bs4 to get the links in a page and the general texts
    request = urllib.request.Request(url)
    request.add_header('User-Agent', header) #headers['User-Agent']
    raw_response = urllib.request.urlopen(request).read()
    try:
        html = raw_response.decode("utf-8")
        soup = BeautifulSoup(html, 'html.parser')
    except:
        pass  # some thimes encodeing and decodeing are different    

    what_you_searched = soup.title


    divs = soup.select("#search div.g")
    for div in divs:
        result["what you searched"].append(what_you_searched) 

        general_look = div.get_text()
        result["title and snippet"].append(general_look)

        link = div.find ("a", href = True)
        article_link = link.get('href')
        result["links"].append(article_link)

       
    
    resultdf =  pd.DataFrame(result)

    return resultdf
