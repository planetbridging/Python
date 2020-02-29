import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable



x = PrettyTable()

x.field_names = ["Title", "Genre", "Developers", "Publisher", "RD JP", "RD NA", "RD PAL"]




URL = "https://en.wikipedia.org/wiki/List_of_Nintendo_Switch_games_(A%E2%80%93L)"
page = requests.get(URL).text

soup = BeautifulSoup(page, 'html.parser')
My_table = soup.find(id='softwarelist')
tr = My_table.findAll('tr')
for tblrow in tr:

    gameTitle = ""
    genre = ""
    developers = ""
    publishers = ""
    releaseDateJP = ""
    releaseDateNA = ""
    releaseDatePAL = ""

    th = tblrow.findAll('th')
    if len(th) == 1:
        gameTitle = th[0].text.encode("utf-8").strip()

    td = tblrow.findAll('td')
    if len(td) == 7:
        genre = td[0].text.encode("utf-8").strip()
        developers = td[1].text.encode("utf-8").strip()
        publishers = td[2].text.encode("utf-8").strip()
        releaseDateJP = td[3].text.encode("utf-8").strip()
        releaseDateNA = td[4].text.encode("utf-8").strip()
        releaseDatePAL = td[5].text.encode("utf-8").strip()
    
    x.add_row([gameTitle, genre, developers, publishers,releaseDateJP,releaseDateNA,releaseDatePAL])

print(x)
