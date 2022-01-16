import requests
from bs4 import BeautifulSoup
import re


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"}



def getVAandChar(url) -> {}:
  url = url

  html = requests.get(url).content

  data = BeautifulSoup(html, 'html.parser')

  parent = data.find("div", {"id": "content"}).find_all("li")

  jpn_va_dict = {}
  for va in parent:
    s = va.text.split(' - ')
    s[1] = re.sub(r'\([^)]*\)', '', s[1]).strip()
    # if va in jpn_va_dict:
    #   jpn_va_dict[s[0]].append(s[1])
    jpn_va_dict[s[0]] = s[1]
  
  return jpn_va_dict

crk_va = getVAandChar("https://japanese-voiceover.fandom.com/wiki/Cookie_Run:_Kingdom_(2021)")
genshin_va = getVAandChar("https://japanese-voiceover.fandom.com/wiki/Genshin_(2020)")

crk_genshin_vas = crk_va.keys() & genshin_va.keys()
crk = "Cookie Run: Kingdom"
gen = "Genshin Impact"
print(f"{'':<20}{crk:^20}\t{gen: ^20}")
for va in crk_genshin_vas:
  print(f"{va: <20}{crk_va[va]:^20}\t{genshin_va[va]:^20}")
  # print(f"{va} voices {crk_va[va]} in cookie run:kingdom and {genshin_va[va]} in genshin impact")


