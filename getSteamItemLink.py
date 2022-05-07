def getSteamItemLink(item):
    finalLink = 'https://steamcommunity.com/market/listings/730/' + item \
                .replace(' ', '%20')\
                .replace('|', '%7C')\
                .replace('(', '%28')\
                .replace(')', '%29')
    return str(finalLink)