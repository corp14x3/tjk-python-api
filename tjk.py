import bs4 , requests , typing , datetime

def requ(city, date ,cityid):
    req = requests.get(url=f"https://www.tjk.org/TR/YarisSever/Info/Sehir/GunlukYarisProgrami?SehirId={cityid}&QueryParameter_Tarih={date}&SehirAdi={city}&Era=today").text
    #print(f"https://www.tjk.org/TR/YarisSever/Info/Sehir/GunlukYarisProgrami?SehirId={cityid}&QueryParameter_Tarih={date}&SehirAdi={city}&Era=today")
    soup = bs4.BeautifulSoup(req, "html.parser")
    return soup

class TJK():
    def __init__(self):
        self.iller = {1:"Adana",2:"Izmir",3:"Antalya",4:"Bursa",5:"Ankara",6:"Sanliurfa",7:"Elazig",8:"Diyarbakir",9:"Kocaeli"}
    def yaris_getir(self , tarih:str , ilid: int):
        """tarih bicimi : 15/10/2025
il idleri ;
adana : 1
izmir : 2
antalya : 3
bursa : 4
ankara : 5
sanliurfa : 6
elazig : 7 
diyarbakir : 8
kocaeli : 9 
"""
        il = self.iller.get(ilid)
        return requ(cityid=ilid,city=il,date=tarih).getText(strip=True)
    
    def pist_durumu(self):
            hava = []
            date = datetime.date.today().strftime("%d/%m/%Y")
            for i , j in self.iller.items():
                weather = requ(j,date,i).select(".conditions-race")
                if weather :hava.append(j)
                for spans in weather:
                    for span in spans:
                        if "raceWeatherBrown" or "raceWeatherGreen" in span & str(span).startswith("Hava"):
                            if str(span).startswith('<span style="flo'):pass
                            else:
                                hava_durumlari = str(span).replace("\n","").replace('<span class="raceWeatherBrown">',"").replace('<span class="raceWeatherGreen">',"").replace("</span>","")
                                hava.append(hava_durumlari)
            for i in hava:
                if i == " ":
                    hava.remove(" ")
                if i == "":
                    hava.remove("")

            if len(hava) < 7:
                return None
            return hava
    
    


tjk_api = TJK()