import requests
from bs4 import BeautifulSoup
import os



def CountDownloadedGames():
    print("Count all games collected")
    LstFiles = os.listdir("Content")
    TotalGameCount = 0
    for f in LstFiles:
        if "content_" in f:
            content = open("Content/"+f, 'r') 
            Lines = content.readlines()
            GameFileCount = 0
            for line in Lines: 
                if "|||" in line:
                    TotalGameCount += 1
                    GameFileCount += 1
            print(f + " Game Count is: " + str(GameFileCount))
    print("Total games: " + str(TotalGameCount))

def SaveTitleData(data,name):
    filename = open("Content/titles_"+name+".txt", "w")
    for d in data:
        filename.write(d + "\n")
    filename.close()
    
def SaveContentData(data,name):
    filename = open("Content/content_"+name+".txt", "w")
    for rows in data:
        output = ""
        for columns in rows:
            output += columns + "|||"
        filename.write(output[:-3] + "\n")
    filename.close()
    
def DownloadAndSave(URL,FileName):
    
    
    if os.path.isfile("Content/content_"+FileName+".txt"):
        print ("Content Already Downloaded: " + FileName)
    else:
        print ("Downloading: " + FileName)
    
        PageTitles = []
        PageDataMatrix = [[]]
        page = requests.get(URL).text

        soup = BeautifulSoup(page, 'html.parser')
        My_table = None
        
        try:
            My_table = soup.find(id='softwarelist')
        except:
            pass
        
        if My_table == None:
            try:
                My_table = soup.find(id='f2plist')
            except:
                pass
        
        if My_table == None:
            try:
                My_table = soup.find("table", attrs={"class": "wikitable"})
            except:
                pass        
                
        
        tr = My_table.findAll('tr')
        
        
        
        for tblrow in tr:
            tmptblrow = []

            th = tblrow.findAll('th')
            if len(th) == 1:
                gameTitletmp = th[0].text.encode("utf-8").strip()
                tmptblrow.append(gameTitletmp)
            else:
                for i in th:
                    tmp = i.text.encode("utf-8").strip()
                    PageTitles.append(tmp)

            td = tblrow.findAll('td')
            if len(td) > 2:
                for d in td:
                    tmptblrow.append(d.text.encode("utf-8").strip())
            PageDataMatrix.append(tmptblrow)
            
        
        SaveContentData(PageDataMatrix,FileName)
        SaveTitleData(PageTitles,FileName)
    
    
#mobile
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Android_games","Android-A-Z")  
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_iOS_games","IOS-A-Z")  

#nintendo
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Nintendo_Switch_games_(A%E2%80%93L)","NintendoSwitchA-L")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Nintendo_Switch_games_(M%E2%80%93Z)#Games_list_(M%E2%80%93Z)","NintendoSwitchM-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Nintendo_64_games#0%E2%80%939","N64A-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Nintendo_Entertainment_System_games","NES-A-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Super_Nintendo_Entertainment_System_games","SuperNintendo-A-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_GameCube_games","GameCube-A-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Wii_games","WII-A-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Wii_U_games","WIIU-A-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Game_Boy_games","GameBoy-A-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Game_Boy_Color_games","GameBoyColor-A-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Game_Boy_Advance_games","GameBoyAdvance-A-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Nintendo_DS_games","DS-A-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Nintendo_3DS_games","3DS-A-Z")

#playstation
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_games_(A%E2%80%93L)","PS1A-L")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_games_(M%E2%80%93Z)#Games_list_(M%E2%80%93Z)","PS1M-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_2_games","PS2A-K")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_2_games_(L%E2%80%93Z)#Games_list_(L-Z)","PS2L-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_download-only_PlayStation_3_games","PS3Download-Only")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_3_games_released_on_disc","PS3GamesOnDiscOnly")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_4_games","PS4A-L")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_4_games_(M%E2%80%93Z)","PS4M-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_4_free-to-play_games","PS4-F2P")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_Portable_games","PSP")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_downloadable_PlayStation_Portable_games","PSP-Download")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_Vita_games_(A%E2%80%93L)","PSPVita-A-L")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_Vita_games_(M%E2%80%93O)","PSPVita-M-O")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_Vita_games_(P%E2%80%93R)","PSPVita-P-R")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_Vita_games_(T%E2%80%93V)","PSPVita-T-V")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PlayStation_Vita_games_(W%E2%80%93Z)","PSPVita-W-Z")

#xbox
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Xbox_games","Xbox-A-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Xbox_360_games_(A%E2%80%93L)","Xbox360-A-L")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Xbox_360_games_(M%E2%80%93Z)","Xbox360-M-Z")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Xbox_One_games_(A%E2%80%93L)","XboxOne-A-L")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_Xbox_One_games_(M%E2%80%93Z)","XboxOne-M-Z")

#pc games
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PC_games","PC-A")
DownloadAndSave("https://en.wikipedia.org/wiki/List_of_PC_games_(Numerical)","PC-Numerical")


Alphabet = "BCDEFGHIJKLMNOPQRSTUVWXYZ"

for a in Alphabet:
    newlink = "https://en.wikipedia.org/wiki/List_of_PC_games_("+a+")"
    DownloadAndSave(newlink,"PC-" + a)
    
    
CountDownloadedGames()
