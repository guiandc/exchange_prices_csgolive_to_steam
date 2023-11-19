from time import sleep
from selenium.webdriver.common.by import By

def getCsgoLiveSiteCode(driver):
    #retorna ao csgoLive após o login
    driver.get('https://www.csgolive.com/withdraw')
    #acessa pagina contendo os itens P2P do CSGO
    driver.find_elements(By.CLASS_NAME, ('market-tab'))[3].click()
    sleep(0.5)
    #retorna o html da página
    return driver.page_source