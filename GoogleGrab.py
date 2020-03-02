import requests
from bs4 import BeautifulSoup


 
 
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

 
def fetch_results(search_term, number_results, language_code):
    assert isinstance(search_term, str), 'Search term must be a string'
    assert isinstance(number_results, int), 'Number of results must be an integer'
    escaped_search_term = search_term.replace(' ', '+')
 
    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()
 
    return search_term, response.text
    
    
def ProcessGoogleSearch(data):
    soup = BeautifulSoup(data, 'html.parser')
    mydivs = soup.findAll("div", {"class": "g"})
    for d in mydivs:
        links = d.findAll('a')
        for a in links:
            linkattr = a.attrs
            if "ping" in linkattr:
                if "href" in linkattr:
                    extractedlink = a.attrs["href"]
                    extractedtitle = ""
                    title = a.findAll('h3')
                    if len(title) > 0:
                        extractedtitle = title[0].get_text()

                    #extractedtitle = a.get_text()
                    print(extractedlink.encode("utf-8") + " ::: " + extractedtitle.encode("utf-8"))
 
if __name__ == '__main__':
    keyword, html = fetch_results('"35 248 809 739"', 100, 'en')
    ProcessGoogleSearch(html.encode("utf-8"))
