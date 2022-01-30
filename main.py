import requests
from bs4 import BeautifulSoup
from db import writeDB
from db import writeDBprice
from db import queryDB
from db import queryDBid
from htmlpage import htmlGen



# Coletar a primeira página da lista de artistas
page = requests.get('https://www.ludopedia.com.br/leiloes/ultimas-24-horas')

# Criar o objeto BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

artist_name_list = soup.find(class_='row bord-top')
artist_name_list_items = artist_name_list.find_all('h4')
artist_name_list_items_price = artist_name_list.find_all('span')



#print(artist_name_list_items_price)
dict = {}
list = []
list_price = []
list_merged = []
for name in artist_name_list_items:
   #print(name.contents[0])
   #dict[name.contents[0]] = "name"
   list.append(name.contents[0])

for x in artist_name_list_items_price:
    price = x.contents[0]
    if price.find("R$") == 0: 
        #print(price)
        list_price.append(price)


for n in range(0,len(list)):
    list_merged.append(list[n] + "|" + list_price[n])

for n in list_merged:
    l_merge = n.split("|")
    name = l_merge[0]
    price = l_merge[1]
    print("Name: {} Price: {}".format(name,price))
    #print(queryDBid(name)[0][0])
    bgid = queryDBid(name)
    try:
        #print(type(queryDBid(name)[0][0]))
        if type(bgid[0][0]) != int:
            print("New entry bgname")
            writeDB(name,"ND")
            bgid = queryDBid(name)
            writeDBprice(price,bgid[0][0])
    except:
        print("New entry bgname:except")
        writeDB(name,"ND")
        bgid = queryDBid(name)
        writeDBprice(price,bgid[0][0])      
    if type(bgid[0][0]) == int:
         writeDBprice(price,bgid[0][0])   


print("Reading DB!")
queryDB("New York 1901","")

print("Generating HTML")
htmlGen()