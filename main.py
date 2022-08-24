from ast import keyword
from fake_headers import Headers
import url_builder
import url_digger
import pandas as pd
from tqdm import tqdm 




common_keywords = ["Battery" , "battery%2Bstorage" ]

# build you keywords here!
list = []

for i in range(0,1):
    try:
        #country = country_list.iloc[i,1]
        for keywords in common_keywords:
            word = str(country) + "%2B" + keywords
            list.append(word) 
    except:
        pass


all_urls = []

for words in list:
    keywords = words
    urls = url_builder.url_builder(keywords, "", "10")  #%2B
    all_urls.extend(urls)


result = pd.DataFrame({ 'what you searched': [], 'title and snippet':[], 'links': []})

for url in tqdm( all_urls):

    if __name__ == "__main__":   # generate different headers everytime we start searching
        header = Headers(
            browser=None,  
            os=None,  
            headers=True  
        )

    headers = header.generate()

    try: 
        google_search = url_digger.url_digger(url, headers['User-Agent'])
        result = result.append(google_search)
    except :
        pass #result = result.append("Jumped Error in decodeing!")


result.to_excel ("Anywhere you want!")


