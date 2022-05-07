from selenium import webdriver
from authSteam import authSteam
from authCsgoLive import authCsgoLive
from getCsgoLiveSiteCode import getCsgoLiveSiteCode
from getCsgoLiveItemList import getCsgoLiveItemList
from getSteamItemPrice import getSteamItemPrice

def main():
    steamLogin = ''
    steamPass = ''

    #instanciando o web driver
    driver = webdriver.Chrome(executable_path=r'C:\Users\gui20\AppData\Local\Programs\Python\Python39\chromedriver.exe')
    driver.set_window_size(50, 720)
    driver.set_window_position(0, 0)
    authSteam(driver, steamLogin, steamPass)
    authCsgoLive(driver)

    while True:
        csgoLiveHTML = getCsgoLiveSiteCode(driver)
        itemlist = getCsgoLiveItemList(csgoLiveHTML)
        getSteamItemPrice(driver, itemlist)
        driver.get('https://www.csgolive.com/withdraw')
        x = input('re-executar? (s/n)')
        if x == 'n':
            break

if __name__ == "__main__":
    main()