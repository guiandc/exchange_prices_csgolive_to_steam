def calcutatingPrices(itemList):
    try:
        if int(itemList[2]) > 0:
            profit = round(int(itemList[2])/int(itemList[1]),2)
        else:
            profit = 0
    except Exception:
        profit = 0
    print(itemList[1], '    '\
            #,itemList[2], '    '\
            ,profit, '    '\
            ,itemList[0])

# preço em dolar
# preço em real
# profit
# nome do item