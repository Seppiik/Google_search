import pandas as pd

def url_builder(query, datefilter, pagenumber):

    """Return special URL which is basically the google result page. 

    Args: 
        query (string): words you would like to search in Google.
        datefilter (string) : last day (d), last week (w), last month(m), last year (y)- last 2months (2m) - or just "" for no filtter
        pagenumber (integer) : how many google search result you would like to see!
    Returns:
        response (string): google serahc URLs. 
    """
   
    urls = []

    word_to_search =  query
    as_qdr = "&as_qdr=" + datefilter

    for i in range (0, int(pagenumber)):
        next_page = "&start=" + str(i) + "0" 
        build_url = "https://www.google.com/search?q=" + word_to_search + next_page + as_qdr
        urls.append(build_url)

    return urls
