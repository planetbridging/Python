#created by shannon setter 5/10/20
import requests
from bs4 import BeautifulSoup
import re


 

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
app_ids = []
data_captured = []

def get_playstore(google_url):
    #google_url = "https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfZnJlZV9HQU1FEAcYAw%3D%3D:S:ANO1ljJ_Y5U&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19mcmVlX0dBTUUQBxgD:S:ANO1ljL4b8c"
    page = requests.get(google_url).text
    soup = BeautifulSoup(page, 'html.parser')
    a = soup.findAll('a')

    for _a in a:
        if "/store/apps/details?id=" in str(_a['href']):
            a_id = str(_a['href']).replace("/store/apps/details?id=","")
            #print("start"+a_id+"stop")
            if a_id not in app_ids:
                print("start"+a_id+"stop")
                app_ids.append(a_id)
    print("IDS: " + str(len(app_ids)))


        #print(_a['href'])

def get_page(url,id):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    div = soup.findAll('div')
    h1 = soup.find("h1")
    game_title = str(h1.text).replace(",","")
    clean_title = re.sub('[^A-Za-z0-9]+', '', game_title)
    for d in div:
        if "Installs" in str(d.text) and "," in str(d.text) and len(d.text) <= 30:
            #print( clean_title + ","+ str(d.text).replace(",","").replace("Installs","").replace("+",""))
            data_captured.append(clean_title + ","+ str(d.text).replace(",","").replace("Installs","").replace("+","") + "," + id)

def generate_csv_data():
    for i in app_ids:
        get_page("https://play.google.com/store/apps/details?id=" + i, i)

def save_csv_data(csv_name):
    with open(csv_name, 'w') as f:
        f.write("%s\n" % "Game_Title,Est_Downloads,Game_Id")
        for i in data_captured:
            f.write("%s\n" % i)

if __name__ == '__main__':
    #top games
    get_playstore("https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfZnJlZV9HQU1FEAcYAw%3D%3D:S:ANO1ljJ_Y5U&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19mcmVlX0dBTUUQBxgD:S:ANO1ljL4b8c")
    generate_csv_data()
    save_csv_data("Top_games.csv")
    #top sellings games
    #get_playstore("https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfcGFpZF9HQU1FEAcYAw%3D%3D:S:ANO1ljLtt38&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljJCqyI")
    #generate_csv_data()
    #save_csv_data("Top_selling_games.csv")
    #top grossing games
    #get_playstore("https://play.google.com/store/apps/collection/cluster?clp=0g4YChYKEHRvcGdyb3NzaW5nX0dBTUUQBxgD:S:ANO1ljLhYwQ&gsr=ChvSDhgKFgoQdG9wZ3Jvc3NpbmdfR0FNRRAHGAM%3D:S:ANO1ljIKta8")
    #generate_csv_data()
    #save_csv_data("Top_grossing_games.csv")
