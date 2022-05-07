from time import sleep
from selenium.webdriver.common.by import By

def authCsgoLive(driver):
    #acessa steam para efetuar a autenticação
    driver.get('https://steamcommunity.com/openid/login?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=checkid_setup&openid.return_to=https%3A%2F%2Fwww.csgo-live.com%2Fv1%2Flogin%2F%3Fcallback%3Dhttps%3A%2F%2Fwww.csgolive.com%2Fauth%2F&openid.realm=https%3A%2F%2Fwww.csgo-live.com&openid.ns.sreg=http%3A%2F%2Fopenid.net%2Fextensions%2Fsreg%2F1.1&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select')  # site login csgo live
    driver.find_element(By.CLASS_NAME, 'btn_green_white_innerfade').click()  #clicar no botão login
    sleep(0.5)