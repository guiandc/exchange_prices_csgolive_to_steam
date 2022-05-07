from bs4 import BeautifulSoup
from time import sleep
from getSteamItemLink import getSteamItemLink
from calcutatingPrices import calcutatingPrices

def getSteamItemPrice(driver, itemList):
    #busca item por item
    for item in itemList:
        #abre uma pagína para cada 1 dos itens listados
        link = getSteamItemLink(itemList[itemList.index(item)][0])
        driver.get(link)
        sleep(1)
        html = driver.page_source

        #seleciona area com itens
        products = BeautifulSoup(html, 'html.parser').find_all("span", attrs={'class': 'market_listing_price_with_fee'})

        #procura na area de itens por produtos com preço em real
        price = 0
        for steamItem in products:
            if 'R$' in steamItem.text:
                price = steamItem.text.replace(' ', '').replace('\n', '').replace('	', '').replace(',', '').replace('.', '')[2:]
                break
        itemList[itemList.index(item)].append(price)
        calcutatingPrices(itemList[itemList.index(item)])