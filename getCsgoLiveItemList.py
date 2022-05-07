from bs4 import BeautifulSoup

def getCsgoLiveItemList(html):
    #seleciona todos os produtos e combos de produtos disponiveis para a compra
    products = BeautifulSoup(html, 'html.parser').find_all("div", attrs={'class': 'listing-wrapper'})

    #busca lista de itens e insere nome e preço em uma lista
    fullItemList = []

    for i in products:
        if i.find("div", attrs={'class': 'item-footer'}): #verifica se a caixa possui apenas 1 item
        #nome do item
            item_name = i.find("div", attrs={'class': 'item-name'}).text

        #preço do item, seguido de tratarivas para excluir o texto e manter apenas o valor
            item_price = i.find("button", attrs={'class': 'buy-button'}).text
            item_price = item_price.replace(' ','').replace('\n','').replace('.','')[3:]#string a partir de 3 para excluir a palavra buy
            if '(' in item_price:
                item_price = item_price[:(item_price.rfind('('))] #caso tenha desconto é necessário excluir o texto

        #insere valores em lista e adiciona 1 a contagem de itens
            fullItemList += [[item_name, item_price]]
    #mostra a quatidade total de itens e os lista individualmente(se não houverem itens o código para)
    print('-------------------------------------------------\n',
          len(fullItemList),' itens disponíveis',
          '\n-------------------------------------------------')
    return fullItemList